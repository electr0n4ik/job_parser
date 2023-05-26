import os


class HeadHunter:
    """hh.ru"""

    @classmethod
    def get_api_key(cls):
        """Возвращает HH API"""
        api_secret: str = os.getenv('API_HH_SECRET')
        return api_secret

    def __init__(self):
        pass

