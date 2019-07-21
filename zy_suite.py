
# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/06 0:35
file:zy_suite.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

import unittest
import os
from testcases import test_register_case                       # 导入模块
from testcases.test_register_case import RegisterTestCase      # 导入类
from commons.config import conf
from commons.constant import TEST_CASE_DIR,REPORT_DIR
from libraries.HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.TestSuite()

loader = unittest.TestLoader()

report_description = conf.get('report','description')
report_title = conf.get('report','title')
report_tester = conf.get('report','tester')

# 按模块添加测试用例
# suite.addTest(loader.loadTestsFromModule(test_register_case))

# 按类添加测试用例
# suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))

# 按目录添加测试用例
suite.addTest(loader.discover(TEST_CASE_DIR))

with open(os.path.join(REPORT_DIR,'report.html'),'wb') as f:
    runner = HTMLTestRunner(
                            stream=f,
                            verbosity=2,
                            description=report_description,
                            title=report_title,
                            tester=report_tester
                            )
    runner.run(suite)