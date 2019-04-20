#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common.BasePage import BasePage
from PageLocators.login_locator import LoginLocator
import pytest

@pytest.mark.smoke
class LoginPage(LoginLocator, BasePage):
    @pytest.mark.login
    def login(self, username, passwd):
        # self.driver.find_element(self.username_input).send_keys(username)
        # self.driver.find_element(self.passwd_input).send_keys(passwd)
        # self.driver.find_element(self.login_button).click()
        # 日志内容：登录页面的登录功能
        name = "登录页面_登录功能"
        self.wait_element_to_visiblity(self.username_input, model=name)
        self.input_text(self.username_input, username, model=name)
        self.input_text(self.passwd_input, passwd, model=name)
        self.click_element(self.login_button, model=name)
    def get_errorMsg_fromLoginArea(self):
        name = "登录页面_错误提示信息"
        return self.get_text(self.error_msg_prompt, model=name)
