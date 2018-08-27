

class User:
    """Represents a Twitch user."""
    __slots__ = ('broadcaster_type', 'description', 'display_name', 'email', 'id',
                 'login', 'offline_image_url', 'profile_image_url', 'type', 'view_count')

    def __init__(self, data):
        self.broadcaster_type = data['broadcaster_type']
        self.description = data['description']
        self.display_name = data['display_name']
        self.email = data['email'] if 'email' in data else ""
        self.id = data['id']
        self.login = data['login']
        self.offline_image_url = data['offline_image_url']
        self.profile_image_url = data['profile_image_url']
        self.type = data['type']
        self.view_count = data['view_count']
