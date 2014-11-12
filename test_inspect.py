import inspect
import os

class test:
    def __init__(self):
        print 'init'
         
    def tt(self):
        print "tt"
         
print inspect.getsource(test)