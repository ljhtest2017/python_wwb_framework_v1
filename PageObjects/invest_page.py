#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
from PageLocators.big_locator import BigLocator


class BigPage(BigLocator):
    def __init__(self, driver):
        self.driver = driver

    def get_user_left_money(self):
        pass

    def invest(self, money):
        pass

    def click_active_button_from_invest_success_puput(self):
        pass


