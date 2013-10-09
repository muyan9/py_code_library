'''
Created on 2009-11-19

@author: zcy
'''

import time
import os

class cpu(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print 'top  -n 1 |grep Cpu'
        
    def get_cpu_usage(self): 
        return os.system('top  -n 1 |grep Cpu')
    
    def get_mem_usage(self):
        return os.system('free -m')
    
    def get_disk_usage(self):
        return os.system('df -h | grep sample')
    
a = cpu()
print a.get_cpu_usage()