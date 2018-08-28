import aiohttp
import asyncio
import json
import logging
import sys
from urllib.parse import quote as _uriquote
from . import __version__
from .auth import AuthToken
from .errors import BadRequest, Unauthorized, Forbidden, NotFound


logger = logging.getLogger('aiotwitch')


async def json_or_text(response):
    text = await response.text(encoding='utf-8')
    # Twitch appends a character set to the content-type, so startswith is necessary
    if response.headers['content-type'].startswith('application/json'):
        return json.loads(text)
    return text


class Route:
    BASE_URL = 'https://api.twitch.tv/helix'

    def __init__(self, method, path, **parameters):
        self.path = path
        self.method = method
        url = (self.BASE_URL + self.path)
        if parameters:
            self.url = url.format(**{k: _uriquote(v) if isinstance(v, str) else v for k, v in parameters.items()})
        else:
            self.url = url


class HTTPClient:
    def __init__(self, client_id, client_secret, loop=None):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self._session = aiohttp.ClientSession(loop=loop)
        self.auth = AuthToken(client_id, client_secret)
        version = sys.version_info
        self.user_agent = f'aiotwitch (https://github.com/kelwing/aiotwitch {__version__}) ' \
                          f'Python/{version[0]}.{version[1]} aiohttp/{aiohttp.__version__}'

    def __del__(self):
        self.loop.run_until_complete(self._session.close())

    async def request(self, route, **kwargs):
        """
        Send a request to Twitch
        :param route: A :class:Route object that represents the API call
        :param kwargs: Any additional arguments to pass to the aiohttp request call
        :return: A dictionary representing the data
        """
        method = route.method
        url = route.url

        headers = {
            'User-Agent': self.user_agent,
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {await self.auth.get()}"
        }

        kwargs['headers'] = headers

        async with self._session.request(method, url, **kwargs) as r:
            data = await json_or_text(r)

            if 300 > r.status >= 200:
                logger.debug('%s %s has received %s', method, url, data)
                return data

            if r.status == 400:
                raise BadRequest

            if r.status == 401:
                raise Unauthorized

            if r.status == 403:
                raise Forbidden

            if r.status == 404:
                raise NotFound
