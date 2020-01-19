# -*- conding: utf-8 -*-
# @Time      :2019/8/13 9:36
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :my_log.py
import logging

class MyLog:
    def my_log(self,msg,level):
        #定义一个日志收集器
        my_logger = logging.getLogger("python11")

        #设定级别
        my_logger.setLevel("DEBUG")
        #设置输出格式
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s")

        #创建自己的输出渠道
        ch=logging.StreamHandler()
        ch.setLevel("INFO")
        ch.setFormatter(formatter)

        #对接输出渠道
        my_logger.addHandler(ch)

        #收集日志
        if level=="DEBUG":
            my_logger.debug(msg)
        elif level=="INFO":
            my_logger.info(msg)
        elif level == 'WARING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)
        #关闭渠道
        my_logger.removeHandler(ch)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')
    def info(self,msg):
        self.my_log(msg,'INFO')
    def error(self,msg):
        self.my_log(msg,'ERROR')



