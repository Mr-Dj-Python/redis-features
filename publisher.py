import time
import redis

redis_client = redis.Redis()

for n in range(1, 10):
    redis_client.publish('serviceStatus', n)
    pubsub = redis_client.pubsub()
    print(f"--> publish state {n=}")
    time.sleep(1)