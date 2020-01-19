# -*- conding: utf-8 -*-
# @Time      :2019/8/13 9:26
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :http_request_demo.py
import hashlib,requests

def notice(info_num):
    '''获取MD5加密后的秘钥'''
    m = hashlib.md5()
    str_info_password = str(info_num)
    m.update(str_info_password.encode("utf-8"))
    hexdigest = m.hexdigest()
    password = hexdigest.upper()
    '''获取登录接口Token的值'''
    url = "http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token"
    querystring = {"authType": "password"}
    payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\"," \
              "\n\t\"clientCode\":\"pbsso\"," \
              "\n\t\"orgCode\":\"0000\"," \
              "\n\t\"userCode\":\"90000003\"," \
              "\n\t\"password\":\"password_value\"," \
              "\n\t\"kaptchaCode\":\"7165\"}".replace("password_value", str(password))
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=payload, headers=headers, params=querystring)
    print(response.json())
    sid = response.json()["accessToken"]


    # url = "http://192.168.6.119:8080/NoticeService/webservice"
    # payload = "{\"func\":\"2003\",\"uid\":\"474\",\"brokerid\":\"0000\",\"data\":[{\"pagecount\":\"1000\",\"currentindex\":\"1\"}]}"
    # headers = {
    #     'Content-Type': "application/json",
    #     'sid': sid
    # }
    # response = requests.post(url, data=payload, headers=headers)
    # print(response.json())


if __name__ == '__main__':
    info_password = 90000003111111
    notice(info_password)