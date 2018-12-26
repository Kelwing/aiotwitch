
class Stream:
    """Represents a twitch stream"""
    __slots__ = ['community_ids', 'game_id', 'id', 'language', 'started_at', 'thumbnail_url', 'title', 'type',
                 'user_id', 'user_name', 'viewer_count']

    def __init__(self, data):
        self.community_ids = data.get('community_ids')
        self.game_id = data.get('game_id')
        self.id = data.get('id')
        self.language = data.get('language')
        self.started_at = data.get('started_at')
        self.thumbnail_url = data.get('thumbnail_url')
        self.title = data.get('title')
        self.type = data.get('type')
        self.user_id = data.get('user_id')
        self.user_name = data.get('user_name')
        self.viewer_count = data.get('viewer_count')
