# python code

from redlock import RedLock
import redis


redis_obj = redis.Redis()
name_lock = RedLock('last_name')
name_lock.acquire()

print(f"setting value redis key last_name")

redis_obj.set('last_name', 'Ocean11')

print("new value set")
name_lock.release()

