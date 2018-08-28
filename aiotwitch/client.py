import asyncio
from .http import HTTPClient, Route
from .subscription import Subscription
from .user import User


class Client:
    """Represents a connection to the Twitch API"""
    def __init__(self, *, loop=None, **options):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.http = HTTPClient(options.get('client_id'), options.get('client_secret'), loop=self.loop)

    async def get_users_by_id(self, *ids):
        """
        Get a list of users by ID
        :param ids: Twitch user IDs
        :return: A list of :class:.user.User
        """
        params = [('id', i) for i in ids]
        route = Route("GET", "/users")
        data = await self.http.request(route, params=params)
        return [User(d) for d in data['data']]

    async def get_users_by_login(self, *logins):
        """
        Get a list of users by login
        :param logins: Twitch user logins
        :return: A list of :class:.user.User
        """
        params = [('login', l) for l in logins]
        route = Route("GET", "/users")
        data = await self.http.request(route, params=params)
        return [User(d) for d in data['data']]

    async def get_webhook_subscriptions(self):
        """
        Get a list of webhook subscriptions
        :return: A list of :class:.subscription.Subscription
        """
        route = Route("GET", '/webhooks/subscriptions')
        data = await self.http.request(route)
        return [Subscription(d) for d in data['data']]
