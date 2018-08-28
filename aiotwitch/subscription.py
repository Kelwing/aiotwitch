import datetime as dt


class Subscription:
    """Represents a Twitch webhook subscription"""
    __slots__ = ('topic', 'callback', 'expires_at')

    def __init__(self, data):
        self.topic = data['topic']
        self.callback = data['callback']
        self.expires_at = dt.datetime.strptime(data['expires_at'], '%Y-%m-%dT%H:%M:%SZ')
