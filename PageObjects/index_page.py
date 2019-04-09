#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
from PageLocators.index_locator import IndexLocator


class IndexPage(IndexLocator):
    def __init__(self, driver):
        self.driver = driver

    def get_nickName(self):
        # return self.driver.find_element_by_xpath('').text
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.user_nick_name)))
        return self.driver.find_element(self.user_nick_name)

    def click_first_invest_button(self):
        self.driver.find_element(self.first_invest).click()
        pass
