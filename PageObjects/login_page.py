#!/usr/bin/python
# -*- coding: UTF-8 -*-

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, passwd):
        self.driver.find_element_by_xpath('').send_keys(username)
        self.driver.find_element_by_xpath('').send_keys(passwd)
        self.driver.find_element_by_xpath('').click()

    def get_errorMsg_fromLoginArea(self):
        return self.driver.find_element_by_xpath('').get_text
