# -*- conding: utf-8 -*-
# @Time      :2019/8/13 16:14
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :project_path.py
import os
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]#文件根路径
#测试报告路径
test_case_path = os.path.join(project_path,"test_data","pobo_test_data.xlsx")

#测试报告的路径
test_report_path=os.path.join(project_path,"test_result","html_report","test_api.html")

#配置文件路径
case_config_path=os.path.join(project_path,'conf','case.config')