# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/06/26 23:41
file:register.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""


# 注册函数
users = [{'user': 'python', 'password': '123456'}]


def register(username, password1, password2):
    # 注册功能
    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['user']:
            # 账号存在
            return {"code": 0, "msg": "该账户已存在"}
    else:
        if password1 != password2:
            # 两次密码不一致
            return {"code": 0, "msg": "两次密码不一致"}
        else:
            # 账号不存在,密码不重复，判断账号密码长度是否在 6-18位之间
            if 6 <= len(username) <= 18 and 6 <= len(password1) <= 18:
                # 注册账号
                users.append({'user': username, 'password': password1})
                return {'code':1,'msg':'注册成功'}
            else:
                # 账号密码长度不对，注册失败
                return {"code": 0, "msg": "账号和密码必须在6-18位之间"}