'''
Created on 2010-1-19

@author: zcy
'''
import traceback
import time
try:
    pass1
except:
    print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) 
    print traceback.print_exc()