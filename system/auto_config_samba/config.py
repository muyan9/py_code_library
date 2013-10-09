#!/usr/bin/python
# coding=utf8

'''
功能：操作ini格式文件的模块

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

import os

import ConfigParser
from ConfigParser import NoSectionError
from ConfigParser import NoOptionError

filename_global_config = '/etc/samba/smb.conf'
#filename_global_config = os.path.join(os.path.dirname('__file__'), 'system.conf')

def getConf(str_option, str_section = "global"):
    if str_section == None :
        str_section = 'global'
    if str_section.strip() == '' :
        str_section = 'global'
        
    cf = ConfigParser.ConfigParser()
    cf.read(filename_global_config)

    try:
        if str_section.strip() == "" :
            for i in cf.sections():
                for j in cf.options(i):
                    if j == str_option.strip() :
                        return cf.get(i, j)
        else:
            return cf.get(str_section.strip(), str_option.strip())
    except NoSectionError,err:
#        print err
        pass
    except NoOptionError,err:
#        print err
        pass

    return None

def updateConf(str_option_name, str_option_value, str_sectionname = "global"):
    if str_sectionname == None :
        str_sectionname = 'global'
    if str_sectionname.strip() == '' :
        str_sectionname = 'global'
    
    cf = ConfigParser.ConfigParser()
    cf.read(filename_global_config)
    if not cf.has_section(str_sectionname.strip()):
        cf.add_section(str_sectionname.strip())
    cf.set(str_sectionname, str_option_name, str_option_value)
    
    cf.write(open(filename_global_config, "w"))
    return str_option_value

def deleteConf(str_section_name, str_option_name = ''):
    cf = ConfigParser.ConfigParser()
    cf.read(filename_global_config)
    if str_option_name.strip() == '':
        if cf.has_section(str_section_name.strip()):
            cf.remove_section(str_section_name)
    else:
        cf.remove_option(str_section_name, str_option_name)
        
    cf.write(open(filename_global_config, "w"))

#print getConf('dbhost')
