#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By


class IndexLocator:
    # 用户昵称
    user_nick_name = (By.XPATH, '//div[@id="nick"]')

