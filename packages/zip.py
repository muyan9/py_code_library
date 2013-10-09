#!/usr/bin/env python
# -*- coding: cp936 -*-


import zipfile
import os

class zip:
    _filename = ""
    _tmp_path = ""
    _zipfile = None

    def __init__(self,filename,tmp_path):
        self._filename = filename
        self._tmp_path = tmp_path
        self._zipfile = zipfile.ZipFile(filename)
        
    def zipdir(self):
        self._zipfile.printdir()
        
    def namelist(self):
        return self._zipfile.namelist()

    def infolist(self):
        return self._zipfile.infolist()
    
    def getFileInfo(self,filename):
        return self._zipfile.getinfo(filename)

    def unzip(self,filepath = ""):
        if filepath == "" :
            filepath = self._tmp_path
        os.system("unzip -o -q %s -d %s"% (self._filename ,filepath))
    
    def del_dir(self,filepath = ""):
        if filepath == "" :
            filepath = self._tmp_path
        os.system("rm -r -f %s" % self._tmp_path)
    
#zip = zip("../tmp/captrued-[2008-07-15-11-38-21].zip")
#zip.unzip()
#zip.del_dir()


#import re
#str_regex_flowfile = r'\w{32}\.bin'
#re_flowfile = re.compile(str_regex_flowfile)
#result_flowfile = re_flowfile.findall("/var/lib/nepenthes/hexdumps/3ad70fc5fcfa4102539928db9b1cce7a.bin (0x080a9")
#if result_flowfile!= None :
#    for tt in result_flowfile:
#        print tt