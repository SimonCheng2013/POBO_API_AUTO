# -*- conding: utf-8 -*-
# @Time      :2019/8/6 9:57
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :send_email.py
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
_user="532873515@qq.com"
_pwd="ropnoxczhavtcbeb"

now = time.strftime("%Y-%m-%d_%H_%M_%S")#获得时间数据

class sendEmail:
    def send_email(self,email_to,filepath):
        #名字是Multipart就是多个部分
        msg = MIMEMultipart()
        msg["Subject"]=now+"华华的测试报告"
        msg["From"]=_user
        msg["To"]=email_to

        #文字部分
        part=MIMEText("这次是自动化测试结果")
        msg.attach(part)
        '''附件部分'''
        part=MIMEApplication(open(filepath,'rb').read())
        part.add_header("Content-Disposition","attachment",filename=filepath)
        msg.attach(part)
        s = smtplib.SMTP_SSL("smtp.qq.com",timeout=30)
        s.login(_user,_pwd)
        s.sendmail(_user,email_to,msg.as_string())
        s.close()
if __name__ == '__main__':
    sendEmail().send_email("amazing2013@163.com",r"D:\PycharmProjects\POBO_API_AUTO\test_result\html_report\test_api.html")
