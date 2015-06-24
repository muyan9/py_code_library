#!/usr/bin/python
# coding=utf8

'''
功能：时间与字符串之间的转换，可指定格式字符串

版本：0.1
开发人：赵长宇
开发时间：2010-9-1 16:38:00
'''

'''
修改后版本：
修改人：
修改时间：
解决的主要问题说明：
'''

import datetime
import time

#TODO: 多种时间对象判断
def datetime2str(datetime_obj = None, str_format = '%Y-%m-%d %H:%M:%S'):
    '''
    按指定格式获取日期时间
    参数：
    datetime_obj    datetime类型的对象
    str_format    格式描述字符串，若不指定格式，默认为%Y-%m-%d %H:%M:%S
    返回值：string    时间字符串
    '''
    if datetime_obj != None:
        print 'dd',datetime_obj
        return datetime_obj.strftime(str_format)
    else:
        return datetime.datetime.now().strftime(str_format)
    
def str2datetime(str_time, str_format):
    t = time.mktime(time.strptime( str_time, str_format))
    return datetime.datetime.fromtimestamp(t)
    
    
if __name__ == '__main__' :
    print datetime2str()
    d = datetime.datetime(2000, 5, 2, 12, 34 , 23)
    print 'd 类型           ' , type(d)
    print '将 d 转换成字符串  ' , datetime2str(d)
    
    d1 = '2009-08-03 11:13:15'
    d2 = '2011-08-03 12:13:16'
    print 'd1 字符串内容     ' , d1
    print 'd2 字符串内容     ' , d2
    
    t1 = str2datetime(d1, "%Y-%m-%d %H:%M:%S")
    t2 = str2datetime(d2, "%Y-%m-%d %H:%M:%S")
    t = datetime.timedelta()
    t = t2-t1
    print 'd1 与 d2 间隔秒数 ' , t.seconds
    print '将 d1 转换为日期型 ' , type(str2datetime(d1, "%Y-%m-%d %H:%M:%S"))