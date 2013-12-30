#coding: utf8

import hashlib, os
import binascii


def md5(str):
    return hashlib.md5(str).hexdigest().upper()

def md5_file(filename):
    if os.path.exists(filename) and os.path.isfile(filename):
        f = open(filename, 'rb')
        
    else:
        raise Exception("not exist this file : %s." % filename)

def crc32(str):
    return '%08X' % (binascii.crc32(str) & 0xffffffff)

path = u"D:\\迅雷下载\\CentOS-6.5-x86_64-bin-DVD1.iso"

print len(open(path, 'rb').read())

print md5(open(path, 'rb').read())
print crc32(open(path, 'rb').read())