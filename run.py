import os
import dramatiq

from dramatiq_dashboard import DashboardApp
from dramatiq.brokers.redis import RedisBroker

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")

broker = RedisBroker(url=REDIS_URL)
dramatiq.set_broker(broker)
app = DashboardApp(broker=broker, prefix="")
