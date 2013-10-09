import time

from system.thread import thread_task

class thread_pool():
    _max_thread_num = 0
    _pool_thread = []
    
    def __init__(self, max_thread_num = 1):
        if max_thread_num < 1:
            return False
        
        self._max_thread_num = max_thread_num
        
        for i in range(max_thread_num):
            self._pool_thread.append(thread_task.thread_task())
        
    def set_max_thread_num(self, max_thread_num):
        self._max_thread_num = max_thread_num
        self.check_thread_num()
        
    def get_max_thread_num(self):
        return self._max_thread_num
        
    def check_thread_num(self):
        if self._pool_thread.__len__() > self._max_thread_num:
            for t_thread in self._pool_thread:
                while self._pool_thread.__len__() != self._max_thread_num:
                    if t_thread.get_stopflag()==False :
                        self._pool_thread.__delitem__(t_thread)
        elif self._pool_thread.__len__() < self._max_thread_num:
            while self._pool_thread.__len__() != self._max_thread_num:
                t_thread = thread_task.thread_task()
                self._pool_thread.append(t_thread)
                
    def get_thread(self):
        self.check_thread_num()
        for t_thread in self._pool_thread:
            if t_thread.get_stopflag() == True:
                return t_thread
        else:
            return None
                
            
num = 2
a = thread_pool(num)
#a.set_resource_lock(True)
list = []
for i in range(num+4):
    thread1 = a.get_thread()
    if thread1:
        thread1.set_runflag(True)
        thread1.set_thread_name("t %s" % i)
        thread1.set_stopflag(False)
        thread1.start()
        list.append(thread1)
    else:
        print "no valid thread in pool"
#a.set_resource_lock(False)

#thread2 = a.get_thread()
#if thread2:
#    thread2.set_runflag(True)
#    thread2.set_thread_name("t2")
#    thread2.start()
