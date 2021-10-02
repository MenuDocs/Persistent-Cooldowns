from ..commands import Bot

from .abc import Datastore
from .datastore import JsonStore


class Store:
    bot_id: int = None
    datastore: Datastore = JsonStore

    @staticmethod
    async def save_cooldowns(bot: Bot):
        bucket_list = []
        for c in bot.walk_commands():
            x = c._buckets
            print(c.name, x._cache, x._cooldown, x._verify_cache_integrity)

    @staticmethod
    async def load_cooldowns(bot: Bot):
        pass

    @staticmethod
    async def get_saved_cooldowns(bot: Bot):
        pass
