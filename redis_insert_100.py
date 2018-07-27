import redis
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

for x in range(1, 101):
  key = "mykey"+str(x)
  value = x
  redis_db.set(key, value)
  print(key + "," + str(value))

