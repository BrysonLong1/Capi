import rq
from redis import Redis
from app.config import settings

redis = Redis.from_url(settings.REDIS_URL)
queue = rq.Queue("trovix", connection=redis, default_timeout=15)
