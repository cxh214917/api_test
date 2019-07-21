# -*- coding:utf-8 -*-
"""
author:上海-倾心相遇&安暖相陪-18
time:2019/7/19 0019    11:12
E-mail:2904504961@qq.com
Inspirational motto:To do difficult things is to gain something
"""
"""
封装各种路径
"""
import os

# BASE_DIR:项目存放目录路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)

# CONF_DIR:配置文件存放目录路径
CONF_DIR = os.path.join(BASE_DIR,'confs')
# print(CONF_DIR)

# DATA_DIR:测试数据存放目录路径
DATA_DIR = os.path.join(BASE_DIR,'datas')
# print(DATA_DIR)

# LOG_DIR:日志存放目录路径
LOG_DIR = os.path.join(BASE_DIR,'logs')
# print(LOG_DIR)

# REPORT_DIR:测试报告存放目录路径
REPORT_DIR = os.path.join(BASE_DIR,'reports')
# print(REPORT_DIR)

# TEST_CASE_DIR:测试用例存放目录路径
TEST_CASE_DIR = os.path.join(BASE_DIR,'testcases')
# print(TEST_CASE_DIR)