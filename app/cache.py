import os
import aioredis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", decode_responses=True)

async def get_cached_response(key: str):
    return await redis.get(key)

async def set_cached_response(key: str, value: str, ttl: int = 3600):
    await redis.set(key, value, ex=ttl)