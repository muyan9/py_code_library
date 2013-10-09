#-*- coding:utf-8 -*-  
import threading
import time

class Base(threading.Thread): 
    
    __flag_stop = True
    
    def __init__(self, thread_name = ""):
#        self._thread_name = thread_name
#        threading.Thread.__init__(self, name = self._thread_name)
        self.set_stopflag(True)
        self.__mark = 'base'
    
    def set_stopflag(self, flag):
        self.__flag_stop = flag

    def tell(self):  
        print "tell:%s" % self._mark  
      
    def display(self):  
        print "display:%s" % self.__mark  
        self.say()  
      
    def say(self):  
        print 'say:%s' % 'Base'
    
    def run(self):
        self.set_stopflag(False)
        while self.__flag_run:
            print self.__thread_name
            time.sleep(1)
        else:
            self.set_stopflag(True)

        
class Teacher(Base):  
    def __init__(self , a=""):  
        Base.__init__(self, a)  
        self.__mark = 'Teacher'  
      
    def tell(self):  
        print 'tell:%s' % self.__mark  
        Base.display(self)  
         
    def say(self):  
        print 'say:%s' % 'Teacher'  
         
         
if __name__ == '__main__':  
    t = Teacher()
    t.start()
    t.tell()