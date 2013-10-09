#!/usr/bin/env python
# -*- coding: cp936 -*-

#return link time of sample
#from NT_HEADERS.FILE_HEADER
from pe_info import pefile
import glob

def LinkTime(str_filename):
    pe =  pefile.PE(str_filename)
    s = pe.NT_HEADERS.FILE_HEADER
    t = str(s).splitlines()
    t_time = t[3][t[3].index('[')+1:t[3].index(']')]
    return t_time
        
#s = LinkTime('binaries/2b489199cb69a1b3eefcd276e8265334')
#print s