import redis
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

for x in range(100, 0, -1):
  key = "mykey"+str(x)
  val=redis_db.get(key)
  keyval = key +":"+val
  print(keyval)
