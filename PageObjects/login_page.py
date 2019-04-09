#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PageLocators.login_locator import LoginLocator


class LoginPage(LoginLocator):
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, passwd):
        self.driver.find_element(self.username_input).send_keys(username)
        self.driver.find_element(self.passwd_input).send_keys(passwd)
        self.driver.find_element(self.login_button).click()

    def get_errorMsg_fromLoginArea(self):
        return self.driver.find_element(self.error_msg_prompt).text
