#!/usr/bin/python
# coding=utf8

'''
功能：自动创建和删除linux系统上的samba共享
共享文件夹将在 /opt 下创建
添加共享时会自动检查 共享名 用户名 /opt/share_name 时候存在，若存在则退出
删除共享时只删除 /etc/samba/smb.conf 中相应的设置和 /opt/share_name 文件夹，不删除用户名
参数：
add				添加共享
del				删除共享
share_name		共享名
username		用户名
password		用户密码

版本：0.1
开发人：赵长宇
开发时间：2010-9-1 16:38:00
'''

'''
配置说明：
/etc/samba/smb.conf 文件只保留以下内容
[global]
passdb backend = tdbsam
server string = Samba Server Version %v
'''

'''
修改后版本：
修改人：
修改时间：
解决的主要问题说明：
'''

import os
import sys
import shutil

import config

path_smb_root = '/opt'

def write_smb_conf(share_name, path, username, comment = 'default'):
    '''
    将配置参数写入smb配置文件
    '''
    share_name = share_name.strip()
    if comment.strip() == 'default':
        config.updateConf('comment', 'share folder for %s' % username, share_name)
    else:
        config.updateConf('comment', comment, share_name)
    config.updateConf('path', path, share_name)
    config.updateConf('write list', username, share_name)
    
def create_smb_user(share_name, username, password):
    '''
    创建smb用户，共享文件夹，并重新加载服务使之生效
    '''
    #检查共享目录和用户是否存在
    if config.getConf('path', share_name) != None:
        print 'the share name exist.'
        sys.exit()
    cmd = '/usr/bin/pdbedit -L'
    a = os.popen(cmd).readlines()
    for i in a :
        if i.split(':')[0] == username.strip():
            print 'the username exist.'
            sys.exit()
    if os.path.exists(os.path.join(path_smb_root, share_name)):
        print 'the path %s exist.' % os.path.join(path_smb_root, share_name)
        sys.exit()
    #创建smb帐户
    cmd = '/usr/sbin/useradd -M -s /sbin/nologin %s' % username
    os.system(cmd)
    #设置密码
    cmd = 'echo %s > /tmp/dynamic_smb_password && echo %s >> /tmp/dynamic_smb_password && cat /tmp/dynamic_smb_password | /usr/bin/smbpasswd -a -s %s && rm /tmp/dynamic_smb_password'
    os.system(cmd % (password, password, username))
    #创建文件夹
    os.makedirs(os.path.join(path_smb_root, share_name))
    cmd = 'chmod -R 777 %s' % os.path.join(path_smb_root, share_name)
    os.system(cmd)
    #修改smb配置
    write_smb_conf(share_name, os.path.join(path_smb_root, share_name), username)
    #重启smb服务
    cmd = '/etc/init.d/smb reload'
    os.system(cmd)

def del_smb_share(share_name, flag_delete_dir = True, flag_delete_user = False):
    username = config.getConf('write list', share_name)
    #删除配置
    config.deleteConf(share_name)
    #重启smb服务
    cmd = '/etc/init.d/smb reload'
    os.system(cmd)
    #删除文件夹
    if flag_delete_dir and os.path.exists(os.path.join(path_smb_root, share_name)):
        shutil.rmtree(os.path.join(path_smb_root, share_name))
        
    if flag_delete_user:
        os.system('smbpasswd -x %s' % username)
    
def help(help_sort):
    if help_sort == 1:
        print '[cmd] add|del share_name [username] [password]'
    if help_sort == 2:
        print '[cmd] add share_name username password'
    if help_sort == 3:
        print '[cmd] del share_name'

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'add':
            if len(sys.argv) == 5:
                create_smb_user(sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                help(2)
        if sys.argv[1] == 'del':
            if len(sys.argv) == 3:
                del_smb_share(sys.argv[2])
            else:
                help(3)
    else:
        help(1)
