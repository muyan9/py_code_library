# -*- coding: UTF-8 -*-
import smtplib, os, urllib, re
from email.mime.text import MIMEText

mailto_list=['muyan9@163.com']
mail_host="smtp.163.com"  #设置服务器
mail_user="muyan9"    #用户名
mail_pass="***"   #口令
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    conn = urllib.urlopen("http://www.ip138.com")
    if conn.getcode() == 200:
        html = conn.read().decode("gbk")
        match = re.search('<iframe src="(.*?)".*</iframe>', html, re.S)
        url = match.group(1)
    
        conn = urllib.urlopen(url)
        if conn.getcode() == 200:
            content = conn.read().decode('gbk')
            if send_mail(mailto_list,"ip",content):
        #         print "发送成功"
                pass
