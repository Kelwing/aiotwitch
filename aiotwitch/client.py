import asyncio
from .http import HTTPClient, Route
from .user import User


class Client:
    """Represents a connection to the Twitch API"""
    def __init__(self, *, loop=None, **options):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.http = HTTPClient(options.get('client_id'), options.get('client_secret'), loop=self.loop)

    async def get_user(self, ids: list=None, logins: list=None):
        """
        Get a list of users by ID
        :param ids: User IDs to include in the search
        :param logins: Logins to include in the search
        :return: A list of :class:.user.User
        """
        query_string = None
        if ids or logins:
            query_string = "?"
            if ids:
                query_string += '&'.join(ids)
            if logins:
                if ids:
                    query_string += '&'
                query_string += '&'.join(logins)
        route = Route("GET", "/users")
        data = self.http.request(route, query_string=query_string)
        return [User(d) for d in data['data']]
