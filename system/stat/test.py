#!/usr/bin/python

import threading
import time
import os
import string
import sys
import system


class aa(threading.Thread):
    t1 = 0

    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
        
    def run(self):
        self.t1 = self.t1 + 1
        print self.t1
        

a1 = aa("a1")
a1.setDaemon(False)
a1.start()
a2 = aa("a2")
a2.start()

print 


