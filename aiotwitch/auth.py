import aiohttp
import datetime as dt


class AuthToken:
    """
    Represents a Twitch OAuth Client Credentials Flow

    """
    def __init__(self, client, secret):
        self.client = client
        self.secret = secret
        self.token = None
        self.expires = dt.datetime.utcnow()
        self.url = 'https://id.twitch.tv/oauth2/token'

    async def get(self):
        if self.expires > dt.datetime.utcnow():
            return self.token
        data = {
            'client_id': self.client,
            'client_secret': self.secret,
            'grant_type': 'client_credentials'
        }
        now = dt.datetime.utcnow()
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, data=data) as resp:
                r = await resp.json()

        if 'status' in r:
            return None

        self.expires = now + dt.timedelta(seconds=r['expires_in'])
        self.token = r['access_token']

        return self.token

    def __repr__(self):
        return self.token

    def __str__(self):
        return self.token
