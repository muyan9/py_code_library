#!/usr/bin/python
# coding=utf8

'''
功能：ssh命令远程，scp远程文件

版本：0.1
开发人：赵长宇
开发时间：2010-3-1 16:38:00

依赖paramiko包
'''

'''
修改后版本：
修改人：
修改时间：
解决的主要问题说明：
'''

import paramiko

class ssh(object):
    _client = object
    def __init__(self, host='', user='', psw='', port=22):
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(hostname=host, port=port, username=user, password=psw)
        
    def exec_command(self, cmd):
        try:
            i, o, e = self._client.exec_command(cmd)
            return o.read()
        except:
            print e.read()
    
    def transmit_file(self, method, filepath1, filepath2):
        scp = self._client.open_sftp()
        print 'scp'
        if method.strip()=='get':
            scp.get(filepath1, filepath2)
        elif method.strip()=='put':
            scp.put(filepath1, filepath2)
        else:
            pass
        scp.close()
        
        
    def __del__(self):
        self._client.close()

import os

#a = ssh('122.159.248.170', 'root', '%%0W_*nYJr8')
a = ssh('192.168.0.199', 'zcy', 'bushiwobu')
#s = a.exec_command('/honeypot/bakdata.sh')
#s = a.exec_command('ls /mmc/data_bak')
#print s
#s = a.exec_command('ls /')
#print s
#print '/home/zcy/%s' % os.path.basename(s)
#a.transmit_file('get', '/mmc/data_bak/captured#A20100120-0001#2010-03-19-07-54-19.zip', '/home/zcy/a.zip')
a.transmit_file('get', '/home/zcy/recover_gluster.txt', '/home/zcy/a.zip')
#a.transmit_file('put', '/home/zcy/tttttt.ttt', '/home/zcy/aaaaaa.aaa')
