import sys
import inspect

def fun():
    print __file__
    print sys._getframe().f_code.co_name
    print inspect.getframeinfo( inspect.currentframe() )

fun()