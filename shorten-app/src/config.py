from dotenv import load_dotenv
import os

def load_redis_env(env_file: str='env/redis.env') -> tuple[str,str]:
    load_dotenv(dotenv_path=env_file)    
    return (os.getenv('REDIS_HOST'),os.getenv('REDIS_PORT'))

# Set host
host = os.environ['HOSTNAME']

# Get redis infos
redis_host, redis_port = load_redis_env()