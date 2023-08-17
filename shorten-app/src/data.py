from src.config import redis_host,redis_port
import redis

_redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def set(short_token,origin_url):
    return _redis_client.set(short_token,origin_url)

def get(short_token):
    return _redis_client.get(short_token)