#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 成功登录
login_succ = {"username": "18566722082", "passwd": "python", "check": "我的账户[小小蜂96027]"}

# 登录失败，无用户名，无密码，用户名格式不正确
login_fail = [
    {"username": "", "passwd": "python", "check": "请输入手机号"},
    {"username": "18566722082", "passwd": "", "check": "请输入密码"},
    {"username": "185667220823", "passwd": "python", "check": "请输入正确的手机号"}
]