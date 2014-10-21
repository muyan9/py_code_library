import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# for i in dir(r):
#     print i
    
    
# r.set('foo', 'bar')
# print  r.get('foo')   
# print r.dbsize()
# r.lpush("foo1", [1,2])
# r.lpush("foo1", "2")
# r.lpush("foo1", "3")
# print r.rpop('foo1')
# r.save()
# print r.scan("foo")

# for i in range(10):
#     r.rpush("t2", i)
#     
# print r.lpop("t2")
# print r.rpop("t2")

# print r.blpop("t1")
# for i in range(9999):
#     r.rpush("t1",i)
# r.save()

# r.flushall()
# print r.lrange("t1",0,-1)
# print len(range(9999))

# print r.hset("hash", "h2", 'v2')
print r.hget("hash", "h1")
print r.hgetall("hash")
print r.hvals("hash")
print r.hlen("hash")
