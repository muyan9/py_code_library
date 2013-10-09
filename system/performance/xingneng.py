'''
Created on 2009-11-29

@author: zcy
'''
import datetime
import os

def compute_file():
    path_root = "D:/work/compare"

    file_r = open(os.path.join(path_root, "adfs.txt"), "r")
    line = file_r.readline().strip()
    while line:
        line = file_r.readline().strip()
    else:
        file_r.close()


def compute_million():
    
    i = 0
    while i<1000000000:
        i=i+1
    print i
    
    
    
d1 = datetime.datetime.now()
print d1
compute_file()
d2 = datetime.datetime.now()
print d2
print d2-d1