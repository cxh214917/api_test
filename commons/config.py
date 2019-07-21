# -*- coding:utf-8 -*-
"""
author:上海-倾心相遇&安暖相陪-18
time:2019/7/15 0015    17:55
E-mail:2904504961@qq.com
Inspirational motto:To do difficult things is to gain something
"""
import configparser
import os
from commons.constant import CONF_DIR
class Config(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        self.read(os.path.join(CONF_DIR,'my_ini.ini'),encoding='utf-8')

conf = Config()
