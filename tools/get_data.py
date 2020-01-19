# -*- conding: utf-8 -*-
# @Time      :2019/8/13 17:03
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :get_data.py
from tools import project_path
import pandas as pd

class GetData:
    Cookie=None
    NoRegTel = pd.read_excel(project_path.test_case_path,sheet_name="login").ix[0,0]
if __name__ == '__main__':
    print(pd.read_excel(project_path.test_case_path,sheet_name="login").ix[0,0])