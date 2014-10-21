# import gevent
# from gevent import monkey
# # monkey.patch_all()
# import time
# 
# 
# def test1():
#     while True:
#         time.sleep(01)
#         print 1
# def test2():
#     while True:
#         time.sleep(0.01)
#         print 2
# def test3():
#     while True:
#         time.sleep(0.01)
#         print 3
#         
#     
#     
# 
# gevent.joinall([gevent.spawn(test1),gevent.spawn(test2),gevent.spawn(test3)])
#TODO: not complete
import time
import gevent
from gevent import select
import random

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)
def get_random():
    return random.randint(1,10)

# while True:
#     print get_random()

def gr1():
    # Busy waits for a second, but we don't want to stick around...
    select.select([], [], [], get_random())
    print('Started Polling: ', tic())
    select.select([], [], [], get_random())
    print('Ended Polling: ', tic())

def gr2():
    # Busy waits for a second, but we don't want to stick around...
    select.select([], [], [], get_random())
    print('Started Polling: ', tic())
    select.select([], [], [], get_random())
    print('Ended Polling: ', tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, at", tic())
    gevent.sleep(1)


gevent.spawn(gr1,3)
gevent.joinall([
    gevent.spawn(gr1,3),
#     gevent.spawn(gr2),
#     gevent.spawn(gr3),
])
# gevent.