from redlock import RedLock
import redis

redis_obj = redis.Redis()
lock = RedLock('last_name')
lock.acquire()

retry_time = 100
lock.retry_times=retry_time
print("reading value of last name")
current_value = redis_obj.get('last_name')
print(current_value)
lock.release()