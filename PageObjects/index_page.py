#!/usr/bin/python
# -*- coding: UTF-8 -*-

class IndexPage:
    def __init__(self, driver):
        self.driver = driver

    def get_nickName(self):
        return self.driver.find_element_by_xpath('').text

