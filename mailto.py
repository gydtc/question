#!/usr/bin/python
#coding=utf-8

import os
import time
import zipfile
import smtplib
from email.mime.text import MIMEText  
from email.header import Header  
from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication

date_today = time.strftime("%Y%m%d", time.localtime())

def jfile(fname):
    if os.path.exists(fname) :
        print fname+"      exists"
    else:
        print fname+"      no such file or dir"
        os._exit(1)

#jira back file 
data_jira_export=time.strftime("%Y-%b-%d--2245", time.localtime())
file_export_name=data_jira_export+".zip"
file_export_dir="/var/atlassian/application-data/jira/export/"
jfile(file_export_dir)
file_export_zip=file_export_dir+file_export_name
jfile(file_export_zip)

#mail info
msg_from='250428568@qq.com'
passwd='xxxxxxxxxxxxxx'   qq邮箱设置smtp会给    
msg_to='250428568@qq.com'

subject="jirabackup"+date_today
content="jirabackup success!!!"

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to

#mail text
ctext = MIMEText(content)
msg.attach(ctext)

#mail zip export
zippart_e = MIMEApplication(open(file_export_zip, 'rb').read())
zippart_e.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_export_zip))  
msg.attach(zippart_e)

#mail gz attachment
#zippart_a = MIMEApplication(open(file_jira_attachments_zipname, 'rb').read())
#zippart_a.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_jira_attachments_zipname))
#msg.attach(zippart_a)

#mail gz mysql
#zippart_s = MIMEApplication(open(fire_jira_mysql, 'rb').read())
#zippart_s.add_header('Content-Disposition', 'attachment', filename=os.path.basename(fire_jira_mysql))
#msg.attach(zippart_s)



#mail send
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print "success"
except s.SMTPException,e:
    print "failed"
finally:
    s.quit()
