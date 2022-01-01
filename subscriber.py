import redis

redis_obj = redis.Redis()
pubsub = redis_obj.pubsub()
pubsub.subscribe(['serviceStatus'])
for item in pubsub.listen():
    print(item)
