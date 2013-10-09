#!/usr/bin/python
#-*-coding: utf8 -*-

import os
import sys
import getopt
import yaml
import time
import platform
import hashlib
import binascii
import glob
from xml.etree import ElementTree as ET

from TSMDispatcher.TSMDispatcher import Connection,Result

version = '0.4'

host = '10.255.33.121'
port = 31200
role = 'testtest'
tasktypes = 'AVPSCAN'
#tasktypes = ''
#tasktypes = 'MCASCAN'
priority = 9
path_src = '/home/zcy/test/tt/1'
path_result = os.path.abspath('./result')
para_str = ''
count_retry = 3
connection = None

taskid_filename = {}

role_filename = {}

filenames = []

md5_filenames = {}

def help():
    help_str = u'''Usage: python put_task.py [OPTION]... [FILE]...

--host:        主机ip                默认值：10.255.33.121
--port:        端口                  默认值：31200
--role:        角色名
--tasktype:    队列名
--priority:    优先级                默认值：9
--para:        各子系统自定义参数
--path_src:    样本路径（支持递归）
--path_result: 任务结果存放路径        默认值：./result
--retry:       样本投放失败的重试次数   默认值：3
--help:        帮助

%s示例：python put_task.py --host=10.255.33.121 --port=31200 --role=ChangYu --tasktype=AUTOTEST --priority=9 --para='{MISSION: {"MAX_TIME": 30, PACK_JUDGE: "yes", "MODE": "single", "FILE_TYPE":"file_unkown","TIME_TYPE":"minute", "SAMPLE_TYPE":"aaa"}}' --path_src=~/test --path_result=/opt/tmp%s
'''
    if platform.system()=="Linux":
        print help_str % ("\33[1;31m", "\33[0m")
    else:
        print help_str %("", "")

#遍历目录
def blobdir(path):
    #TODO 判断是单文件还是路径
    if os.path.isdir(path):
        for root,dirs,files in os.walk(path):
            for f in files:
                flag_ok = False
                #若任务投放失败，重试 --retry 指定的次数
                i_retry = 0
                while i_retry<count_retry:
                    ret = push_task(para_str, os.path.join(root,f))
                    print ret
                    filenames.append(f)
                    flag_ok = ret[0]
                    i_retry = i_retry+1
                    if flag_ok == True:
                        break
                    print u'%s  重试 %s 次 ' % (f, i_retry)
                    time.sleep(1)
    else:
        flag_ok = False
        #若任务投放失败，重试 --retry 指定的次数
        i_retry = 0
        while i_retry<count_retry:
            ret = push_task(para_str, path)
            print ret
            filenames.append(os.path.basename(path))
            flag_ok = ret[0]
            i_retry = i_retry+1
            if flag_ok == True:
                break
            print u'%s  重试 %s 次 ' % (path, i_retry)

#投放任务
def push_task(para_str, filename):
    f = open(filename, 'rb')
    file_context = f.read()
    f.close()
    md5 = hashlib.md5(file_context).hexdigest().upper()
    md5_filenames[md5] = os.path.basename(filename)
    crc32 = '%08X' % (binascii.crc32(file_context) & 0xffffffff)
    res = connection.push_task(file_name="%s.%s" %(md5, crc32), file_content = file_context, task_args = para_str, tsm_task_type = tasktypes, priority=priority)
    if res[0]==True:
        t = yaml.load(res[1], yaml.loader.Loader)
        #记录投放任务的taskid，用于判断此次投放的任务是否全部完成
        for tasktype in tasktypes.split(","):
            taskid_filename[t[tasktype]] = [tasktype, role, os.path.basename(filename)]
        return (True, t)#taskid
    else:
        return (False, res[1])#错误提示

#取得任务
def pop():
    dis = Connection(host, port, role)
    result = dis.pop_result()
    if result[0]:
        r = Result()
        r = result[1]
        taskid = r.get_taskid()
#        try:
            #保存avml内容taskid_filename
        dict_avml = r.fetch_avmlfile()
        if dict_avml[0] == True:
            content_avml = dict_avml[1]['content']
            path_store = path_result
            if not os.path.exists(path_store):#判断路径是否存在
                os.makedirs(path_store)
            if taskid in taskid_filename.keys():
                filename = "%s_%s_%s.avml" % tuple(taskid_filename[taskid])
            else:
                filename = dict_avml[1]['filename']
            if not filename == '':
                f = open(path_store+os.sep+filename, "wb")
                f.write(content_avml)
                f.close()
            #保存衍生文件
            #对照扫描没有衍生文件，可以不做文件名处理，其他系统都是一次性返回文件，不会因文件名相同而覆盖
            path_derive = path_store+os.sep+filename+"_derive"
            if not os.path.exists(path_derive):
                os.makedirs(path_derive)
            for filename_derive in r.get_filenames():
                f = open(path_derive+os.sep+filename_derive, "wb")
                c = r.fetch_filecontent(filename_derive)
                f.write(c[1])
                f.close()

            if taskid in taskid_filename.keys():
                aa = taskid_filename[taskid]
                aa.append(filename)
                role_filename[(aa[0], aa[2])] = aa
        else:
            pass
            #TODO: print "no avml in tasktype : ", tasktype
#            print role_filename

#        except Exception , value:
#            print "\33[1;31merror\33[0m" ,value
        dis.free_resultsample(taskid)
        dis.free_resultderive(taskid)
        return taskid
    else:
        return 0

if __name__ == '__main__':
#     if len(sys.argv) <=1:
#         help()
#         sys.exit()
    #指定命令行参数列表
#     opts, args = getopt.getopt(sys.argv[1:], None, ["host=", "port=", "role=", "tasktype=", "priority=", "para=", "path_src=", "path_result=", "help"])
    #分析并取得参数值
#     for o,v in opts:
#         if o == '--host':
#             host = v
#         if o == '--port':
#             port = int(v)
#         if o == '--role':
#             role = v
#         if o == '--tasktype':
#             tasktypes = v
#         if o == '--priority':
#             priority = int(v)
#         if o == '--para':
#             para_str = v
#         if o == '--path_src':
#             path_src = v
#             if path_src[0]=='~':
#                 path_src = path_src.replace('~', os.environ['HOME'])
#             path_src = os.path.abspath(path_src)
#         if o == '--path_result':
#             path_result = v
#             if path_result[0]=='~':
#                 path_result = path_result.replace('~', os.environ['HOME'])
#             path_result = os.path.abspath(path_result)
#         if o == '--help':
#             help()
#             sys.exit()
    #创建连接
    connection = Connection(host, port, role)
    #开始遍历目录并投放任务
    blobdir(path_src)
    print '--------------------------------------'
    print u'任务下达完成'
    print '--------------------------------------'
    print u'等待任务处理'
    
    timeout_timestart = time.time()
#    sys.exit()
#    time.sleep(5)
    #本次下发的任务若全部处理完成，结束等待
    while len(taskid_filename.keys())>0:
        keys = taskid_filename.keys()
        ret = pop()
        #若返回不成功，至少大多数可能是队列为空，则等待一段时间
        if ret == 0:
            time.sleep(5)
        else:
            if ret in taskid_filename.keys():
                #print "pre del",taskid_filename.keys() , ret
                del(taskid_filename[ret])#移除已取得结果的taskid
                timeout_timestart = time.time()
                #print "post del", taskid_filename.keys()
        
        #若最后一个接收到的任务距离当前时间超出10分钟,则认为剩余的所有任务超时
        if time.time()-timeout_timestart>60*10:
            break
    
    #TODO: 针对对照扫描的结果输出：各引擎产生的avml应该都不包含原文件名，增加一个字典记录源文件名和md5的关系，用于确定源文件和病毒名的关系
    filenames = set(filenames)
    f_notcomplete = open('notcomplete.lst', 'a')
    for key in taskid_filename:
        f_notcomplete.write(str(taskid_filename[key]))
        f_notcomplete.write('\n')
    f_notcomplete.close()
    
    aaa = open('result.log', 'a')
    for f in filenames:
        #新建xml  将所有字节点加入  保存后删除其他avml
        for f1 in glob.glob("%s/*SCAN_%s_%s.avml" % (path_result, role, f)):
            root = ET.parse(f1).getroot()
            virus_name = root.find('SCAN').find("SCANNER").find("NAME").text
#                if virus_name != "Not Found":
            md5_in_avml = root.find('SCAN').find("HASH").find("MD5").text
            scanner = root.find('SCAN').find("SCANNER").attrib["name"]
            scanner_version = root.find('SCAN').find("SCANNER").find("VERSION").text
            scanner_virusdate = root.find('SCAN').find("SCANNER").find("VIRUSDATE").text
            result_file = """filename: %s   |   scanner: %s   |   virus_name: %s   |   scanner_version: %s   |   virusdate: %s """ % (
                md5_filenames[md5_in_avml], scanner, virus_name, scanner_version, scanner_virusdate)
            print result_file
            aaa.write(result_file)
            aaa.write('\n')
    aaa.close()
    print '--------------------------------------'
    print u"任务全部完成"
