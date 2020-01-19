# -*- conding: utf-8 -*-
# @Time      :2019/7/30 15:09
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :test_http_request.py
import unittest
from tools.project_path import *
from tools.http_request import HttpRequest
from tools.get_data import GetData
from ddt import ddt,data #列表嵌套列表 或者列表嵌套字典
from tools.do_excel import DoExcel
from tools.my_log import MyLog
test_data = DoExcel.get_data(test_case_path)#执行所有用例
my_logger = MyLog()

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        my_logger.info("开始测试")
        pass
    @data(*test_data)
    def test_api(self,item):
        print(test_data)
        # print("url是:{0},data是:{1},header是:{2},http_method是:{3}".format(item['url'],eval(item['data']),item["header"],item['http_method']))
        print("url value:{0}".format(type(item['url'])))
        print("data value:{0}:".format(type(item['data'])))
        print("header value:{0}:".format(type(eval(item['header']))))
        # print("params value:{0}:".format(type(eval(item['params']))))
        print("http_method value:{0}:".format(type(item['http_method'])))
        res = HttpRequest.http_request(item['url'],item['data'],eval(item["header"]),item['http_method'],getattr(GetData,"Cookie"))
        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)
        try:
            self.assertEqual(item['excepted_code'],res.json()["code"])
            TestResult='PASS'#成功的
        except AssertionError as e:
            TestResult='Failed'#失败的
            my_logger.info("执行用例出错：{}".format(e))
            raise e
        finally:
            DoExcel.write_back(test_case_path,'login',item['case_id']+1,str(res.json()),TestResult)
            print('获取到的结果是：{}'.format(res.json()))

    def tearDown(self):
        my_logger.info("结束测试")
        pass

if __name__ == '__main__':
    '''从这里开始测试'''
    TestHttpRequest().test_api()
