import time
import threading

from system.thread import thread_task

class thread_task_a(thread_task):
    def __init__(self, thread_name = ""):
#        self._thread_name = thread_name
        thread_task.__init__(self)
#        self.set_stopflag(True)
        
    def run(self):
        self.set_stopflag(False)
        while self.__flag_run:
            print self.__thread_name
            time.sleep(1)
        else:
            self.set_stopflag(True)
            
            
a = thread_task_a("thread1")
#a.set_runflag(True)
a.start()