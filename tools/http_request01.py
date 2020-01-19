# -*- conding: utf-8 -*-
# @Time      :2019/8/9 9:45
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :http_request.py

import requests
from tools.my_log import MyLog
my_logger = MyLog()
url = "http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token"
data = {'rand': '4e24eefa-1298-4601-8dfd-5e63f742a43', 'clientCode': 'pbsso', 'orgCode': '0000', 'userCode': '90000003', 'password': '9418375E1760BFEAA4D016E9F92FFF1F', 'kaptchaCode': '7165'}
header = {"Content-Type": "application/json"}
params = {"authType": "password"}
http_method = "post"
class HttpRequest:
    @staticmethod
    def http_request(url="http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token",
                     data={'rand': '4e24eefa-1298-4601-8dfd-5e63f742a43', 'clientCode': 'pbsso', 'orgCode': '0000', 'userCode': '90000003', 'password': '9418375E1760BFEAA4D016E9F92FFF1F', 'kaptchaCode': '7165'},
                     header={"Content-Type": "application/json"},
                     params={"authType": "password"},
                     http_method="post",
                     cookie=None):
        try:
            if http_method=="get":
                res = requests.get(url,data,cookies=cookie)
            elif http_method=="post":
                # res = requests.post(url,data=data,headers=header,params=params,cookies=cookie)
                res = requests.post(url,data,header,params,cookies=cookie)
            else:
                my_logger.info("输入请求方法不对")
        except Exception as e:
                my_logger.error("请求报错了：{}".format(e))
                raise e
        return res
    def http_request01(self):
        url = "http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token"
        data = {'rand': '4e24eefa-1298-4601-8dfd-5e63f742a43', 'clientCode': 'pbsso', 'orgCode': '0000',
                'userCode': '90000003', 'password': '9418375E1760BFEAA4D016E9F92FFF1F', 'kaptchaCode': '7165'}
        header = {"Content-Type": "application/json"}
        params = {"authType": "password"}
        http_method = "post"
        res = requests.post(url,data,header,params)
        print(res.json())

    def notice(self,info_num=90000003111111):
        import hashlib
        '''获取MD5加密后的秘钥'''
        m = hashlib.md5()
        str_info_password = str(info_num)
        m.update(str_info_password.encode("utf-8"))
        hexdigest = m.hexdigest()
        password = hexdigest.upper()
        '''获取登录接口Token的值'''
        url = "http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token"
        querystring = {"authType": "password"}
        # payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\"," \
        #       "\n\t\"clientCode\":\"pbsso\"," \
        #       "\n\t\"orgCode\":\"0000\"," \
        #       "\n\t\"userCode\":\"90000003\"," \
        #       "\n\t\"password\":\"9418375E1760BFEAA4D016E9F92FFF1F\"," \
        #       "\n\t\"kaptchaCode\":\"7165\"}"
        payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\"," \
                  "\n\t\"clientCode\":\"pbsso\"," \
                  "\n\t\"orgCode\":\"0000\"," \
                  "\n\t\"userCode\":\"90000003\"," \
                  "\n\t\"password\":\"password_value\"," \
                  "\n\t\"kaptchaCode\":\"7165\"}".replace("password_value", str(password))
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=payload, headers=headers, params=querystring)
        print(response.json())
# if __name__ == '__main__':
#     # HttpRequest.http_request()
#     HttpRequest().http_request01()

def notice():

    import hashlib
    '''获取MD5加密后的秘钥'''
    # m = hashlib.md5()
    # str_info_password = str(info_num)
    # m.update(str_info_password.encode("utf-8"))
    # hexdigest = m.hexdigest()
    # password = hexdigest.upper()
    '''获取登录接口Token的值'''
    url = "http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token"
    querystring = {"authType": "password"}
    payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\"," \
          "\n\t\"clientCode\":\"pbsso\"," \
          "\n\t\"orgCode\":\"0000\"," \
          "\n\t\"userCode\":\"90000003\"," \
          "\n\t\"password\":\"9418375E1760BFEAA4D016E9F92FFF1F\"," \
          "\n\t\"kaptchaCode\":\"7165\"}"

    # payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\",\"clientCode\":\"pbsso\",\"orgCode\":\"0000\",\"userCode\":\" \",\"password\":\"9418375E1760BFEAA4D016E9F92FFF1F\",\"kaptchaCode\":\"7165\"}"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=payload, headers=headers, params=querystring,cookies=None)
    # response = requests.post(url, payload, headers, querystring)
    print(type(payload))
    print(response.json())



notice()