# -*- coding:utf-8 -*-
"""
author:上海-倾心相遇&安暖相陪-18
time:2019/7/15 0015    15:52
E-mail:2904504961@qq.com
Inspirational motto:To do difficult things is to gain something
"""
import logging
import os
from commons.config import conf
from commons.constant import LOG_DIR

log_level = conf.get('log','log_level').upper()
ls_level = conf.get('log','ls_level').upper()
lf_level = conf.get('log','lf_level').upper()

class MyLog(object):

    def __new__(cls, *args, **kwargs):
        my_log = logging.getLogger('my_log')
        my_log.setLevel(log_level)

        l_s = logging.StreamHandler()
        l_s.setLevel(ls_level)
        l_f = logging.FileHandler(os.path.join(LOG_DIR,'log.log'),encoding='utf-8')
        l_f.setLevel(lf_level)

        my_log.addHandler(l_s)
        my_log.addHandler(l_f)

        ft = '%(asctime)s--[%(filename)s-->line:%(lineno)d]--%(levelname)s--%(message)s'
        ft = logging.Formatter(ft)
        l_s.setFormatter(ft)
        l_f.setFormatter(ft)

        return my_log

myLog = MyLog()