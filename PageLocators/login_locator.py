#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By


class LoginLocator:
    # 用户名输入框
    username_input = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@name="passwd"')
    # 登录按钮
    login_button = (By.XPATH, '//button[@type="button"]')
    # 无用户名，无密码，用户名格式不正确提示框
    error_msg_prompt = (By.XPATH, '//button[@name')

