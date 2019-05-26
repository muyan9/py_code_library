#coding: utf8

import hashlib, os
import binascii
import base64
base64._b85alphabet = b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
def base85encode(str, coding = 'utf8'):
    if type(str)==type('ss'):
        a = str.encode(coding)
    return base64.b85encode(a).decode(coding)

def base85decode(str, coding = 'utf8'):
    if type(str)==type('ss'):
        a = str.encode(coding)
    return base64.b85decode(a).decode(coding)

def md5(str):
    return hashlib.md5(str).hexdigest().upper()

def md5_file(filename):
    if os.path.exists(filename) and os.path.isfile(filename):
        hash_new = hashlib.md5() #或hashlib.md5()
        with open(filename,'rb') as fp: #打开文件，一定要以二进制打开
            while True:
                data = fp.read(4096*256) #读取文件块
                if not data: #直到读完文件
                    break
                hash_new.update(data)
        hash_value = hash_new.hexdigest() #生成40位(sha1)或32位(md5)的十六进制字符串
        return hash_value
        
    else:
        raise Exception("not exist this file : %s." % filename)

def crc32(str):
    return '%08X' % (binascii.crc32(str) & 0xffffffff)


def sha1(str):
    hash_new = hashlib.sha1() #或hashlib.md5()
    hash_new.update(str)
    hash_value = hash_new.hexdigest() #生成40位(sha1)或32位(md5)的十六进制字符串
    return hash_value

def sha1_file(filename):
    hash_new = hashlib.sha1() #或hashlib.md5()
    #FIXME: 整理并封装成安装包
    with open(filename,'rb') as fp: #打开文件，一定要以二进制打开
        while True:
            data = fp.read(4096*256) #读取文件块
            if not data: #直到读完文件
                break
            hash_new.update(data)
    hash_value = hash_new.hexdigest() #生成40位(sha1)或32位(md5)的十六进制字符串
    return hash_value

def sha256(str):
    hash_new = hashlib.sha256() #或hashlib.md5()
    hash_new.update(str)
    hash_value = hash_new.hexdigest() #生成40位(sha1)或32位(md5)的十六进制字符串
    return hash_value

def sha256_file(filename):
    hash_new = hashlib.sha256() #或hashlib.md5()
    with open(filename,'rb') as fp: #打开文件，一定要以二进制打开
        while True:
            data = fp.read(4096*256) #读取文件块
            if not data: #直到读完文件
                break
            hash_new.update(data)
    hash_value = hash_new.hexdigest() #生成40位(sha1)或32位(md5)的十六进制字符串
    return hash_value

if __name__ == "__main__":
    path = u"D:\\迅雷下载\\CentOS-7.0-1406-x86_64-livecd.iso"
    
#     print len(open(path, 'rb').read())
#     print md5(open(path, 'rb').read())
#     print(md5_file(path))
#     print crc32(open(path, 'rb').read())
#     print sha1(open(path, 'rb').read())
#     print sha1_file(path)

    a = base85encode('abcdefghijklmnopqrstuvwxyz')
    #                 abcdefghijkkmnopqrstuvwxyz
    print(a)
    b = base85decode(a)
    print(b)
