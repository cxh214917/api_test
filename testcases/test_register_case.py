# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/06/28 22:38
file:test_register_case.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
import unittest
import os
from commons.constant import DATA_DIR
from libraries.ddt import ddt,data
from commons.my_log import myLog
from commons.read_write_excel import ReadExcel
from register import register
from commons.config import conf

sheet_name = conf.get('excel','sheet_name')
read_columns = conf.get('excel','read_columns')

wb = ReadExcel(os.path.join(DATA_DIR,'register_cases.xlsx'),sheet_name)
cases = wb.read_excel_obj(read_columns)

@ddt
class RegisterTestCase(unittest.TestCase):

    @data(*cases)
    def test_register(self,case):
        row = case.case_id + 1
        res = register(*eval(case.data))
        try:
            self.assertEqual(eval(case.excepted),res)
        except AssertionError as e:
            res = 'FAIL'
            myLog.exception(e)
            raise e
        else:
            res = 'PASS'
            myLog.info('该条用例执行的结果是:{}'.format(res))
        finally:
            wb.read_write_data(row=row,column=4,msg=res)

