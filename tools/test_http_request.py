# -*- conding: utf-8 -*-
# @Time      :2019/8/9 9:45
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :http_request.py
import hashlib,requests,unittest
from tools.project_path import *
from tools.http_request import HttpRequest
from tools.get_data import GetData
from ddt import ddt,data #列表嵌套列表 或者列表嵌套字典
from tools.do_excel import DoExcel
from tools.my_log import MyLog
test_data =DoExcel.get_data(test_case_path)
# print(test_data)
my_logger = MyLog()

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        my_logger.info("开始测试")
        print(test_data)
        print("setUp")
    def test_tr(self):
        print("test")
        pass
    @data(*test_data)
    def test_api(self,item):
        # print(item)
        res = HttpRequest.http_request(item['url'],eval(item['data']),item['header'],item['http_method'],getattr(GetData,"Cookie"))
        if res.cookies:
            setattr(GetData,"Cookie",res.cookies)
        try:
            self.assertEqual(item['excepted_code'],res.json()["code"])
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult='Failed'
            my_logger.info("执行用例出错：{}".format(e))
            raise e
        finally:
            DoExcel.write_back(test_case_path,"login",item['case_id']+1,str(res.json()),TestResult)
            print('获取到的结果是：{}'.format(res.json()))
        pass
    def tearDown(self):
        my_logger.info('测试结束')
        print("tearDown")


if __name__ == '__main__':
    TestHttpRequest().test_api()