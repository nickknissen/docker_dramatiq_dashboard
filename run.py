import os

import dramatiq

from dramatiq_dashboard import DashboardApp
from dramatiq.brokers.redis import RedisBroker

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")

QUEUES = os.getenv("QUEUES", "default,")

broker = RedisBroker(url=REDIS_URL)

[broker.declare_queue(queue) for queue in list(filter(None, QUEUES.split(",")))]

dramatiq.set_broker(broker)
app = DashboardApp(broker=broker, prefix="")
