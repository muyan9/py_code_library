import time
import threading

class thread_task(threading.Thread):
    __thread_name = ""
    
    __flag_run = False
    
    __flag_stop = True
    
    def __init__(self, thread_name = ""):
#        self._thread_name = thread_name
#        threading.Thread.__init__(self, name = self._thread_name)
        self.set_stopflag(True)
        
    def set_thread_name(self, thread_name):
        self.__thread_name = thread_name
        
    def set_runflag(self, flag):
        self.__flag_run = flag
        
    def get_runflag(self):
        return self._flag_run
        
    def set_stopflag(self, flag):
        self.__flag_stop = flag
        
    def get_stopflag(self):
        return self.__flag_stop
        
    def run(self):
        self.set_stopflag(False)
        while self.__flag_run:
            print self.__thread_name
            time.sleep(1)
        else:
            self.set_stopflag(True)
            
            
#a = thread_task("thread1")
#b = thread_task("thread2")
#
#a.set_runflag(True)
##True: quit with parent process
#a.setDaemon(True)
#a.start()
#a.set_runflag(False)
#b.start()