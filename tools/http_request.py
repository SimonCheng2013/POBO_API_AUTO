# -*- conding: utf-8 -*-
# @Time      :2019/8/9 9:45
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :http_request.py

import requests
from tools.my_log import MyLog
my_logger = MyLog()
class HttpRequest:
    @staticmethod
    def http_request(url,data,header,params,http_method,cookie=None):
    # def http_request(url,data,header,http_method,cookie=None,params=None):
        try:
            if http_method=="get":
                res = requests.get(url,data,cookies=cookie)
            elif http_method=="post":
                res = requests.post(url,data=data,headers=header,params=params,cookies=cookie)
                # res = requests.post(url,data=data,headers=header,params=params,cookies=cookie)

            else:
                my_logger.info("输入请求方法不对")
        except Exception as e:
                my_logger.error("请求报错了：{}".format(e))
                raise e
        return res

