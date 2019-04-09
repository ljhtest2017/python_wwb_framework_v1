#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
from PageLocators.user_locator import UserLocator


class UserPage(UserLocator):
    def __init__(self, driver):
        self.driver = driver

    def get_user_left_money(self):
        pass
