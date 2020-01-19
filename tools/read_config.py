# -*- conding: utf-8 -*-
# @Time      :2019/8/13 16:34
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :read_config.py
import configparser
class ReadConfig:
    @staticmethod
    def get_config(file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]
if __name__ == '__main__':
    from tools import project_path
    print(ReadConfig.get_config(project_path.case_config_path,'MODE','mode'))