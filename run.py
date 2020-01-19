# -*- conding: utf-8 -*-
# @Time      :2019/7/26 8:58
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :run.py
'''
请求后读入数据
'''
#执行代码入口
# from tools.http_request import HttpRequest
# from tools.do_excel import DoExcel
# from tools.get_cookie import GetCookie

'''获得cookie第一种方法 global COOKIE'''
# COOKIE=None
# def run(test_data):
#     #register
#     for item in test_data:
#         print("正在测试的用例是:{}".format(item["title"]))
#         res = HttpRequest().http_request(item["url"],eval(item["data"]),item["http_method"])
#         print("请求的结果是：{}".format(res.json()))
#         DoExcel().write_back("test_data/test_data.xlsx","register",item["case_id"]+1,str(res.json()))

    #login
    # for i in range(len(test_data)):
    #     print("正在测试的用例是:{}".format(test_data[i]["title"]))
    #     res = HttpRequest().http_request(test_data[i]["url"],eval(test_data[i]["data"]),test_data[i]["http_method"])
    #     print("请求的结果是：{}".format(res.json()))
    #     DoExcel().write_back("test_data/test_data.xlsx","login",i+2,str(res.json()))

# def run_recharge(test_data,sheet_name):#列表嵌套字典格式进来
#     global COOKIE
#     # recharge
#     for item in test_data:
#         print("正在测试的用例是:{}".format(item["title"]))
#         '''获得cookie第一种方法 global COOKIE'''
#         # res = HttpRequest().http_request(item["url"], eval(item["data"]), item["http_method"],COOKIE)
#         '''获得cookie第二种方法 反射'''
#         res = HttpRequest().http_request(item["url"], eval(item["data"]), item["http_method"], getattr(GetCookie,'Cookie'))
#         if res.cookies:
#
#             '''获得cookie第一种方法 global COOKIE'''
#             # COOKIE=res.cookies
#             '''获得cookie第二种方法 反射'''
#             setattr(GetCookie,'Cookie',res.cookies)
#
#         print("请求的结果是：{}".format(res.json()))
#         DoExcel().write_back("test_data/test_data.xlsx", sheet_name, item["case_id"] + 1, str(res.json()))


# test_data=DoExcel().get_data("test_data/test_data.xlsx","login")
# run(test_data)

# test_data=DoExcel().get_data("test_data/test_data.xlsx","register")
# run(test_data)

# test_data=DoExcel().get_data("test_data/test_data.xlsx","recharge")
# run_recharge(test_data,"recharge")


import unittest
import HTMLTestRunner
from tools.project_path import *
from tools.test_http_request_login import TestHttpRequest_Login
from tools.test_http_request_login_mysql import TestHttpRequest_Login
from tools.test_http_request_notice import TestHttpRequest_Notice
from tools.test_http_request_notice_mysql import TestHttpRequest_Notice
from tools.test_http_request_review import TestHttpRequest_Review
from tools.test_http_request_review_mysql import TestHttpRequest_Review
from tools.my_log import MyLog
from tools.send_email import sendEmail

my_logger = MyLog()
suite= unittest.TestSuite()
# suite.addTest(TestHttpRequest("test_api"))#测试类实例
loader = unittest.TestLoader()

#并行多个用例方法一
# suite.addTest(loader.loadTestsFromModule(test_login))
# suite.addTest(loader.loadTestsFromModule(test_recharge))

testcase=[loader.loadTestsFromTestCase(TestHttpRequest_Login),loader.loadTestsFromTestCase(TestHttpRequest_Notice),loader.loadTestsFromTestCase(TestHttpRequest_Review)]

# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest_Notice))
# suite.addTests([loader.loadTestsFromTestCase(TestHttpRequest_Login),loader.loadTestsFromTestCase(TestHttpRequest_Notice),loader.loadTestsFromTestCase(TestHttpRequest_Review)])
suite.addTests(testcase)
# suite.addTests([loader.loadTestsFromTestCase(TestHttpRequest_Notice)])

with open(test_report_path,'wb') as file:
    #执行用例
    my_logger.info("开始执行用例")
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title="这是个单元测试报告1115",
                                           description="这是个单元测试报告1116")
    runner.run(suite)
    my_logger.info("完成执行用例")
    # sendEmail().send_email("amazing2013@163.com",r"D:\PycharmProjects\POBO_API_AUTO\test_result\html_report\test_api.html")
    '''
    E:\tools\jenkins.war
    执行Jenkins命令
    java -jar jenkins.war
    '''