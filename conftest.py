#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pytest
from selenium import webdriver

from PageObjects.login_page import LoginPage
from TestDatas.common_data import web_url
# 登录用例的前置和后置
# setup和teardown
@pytest.fixture
def init_loginEnv():
    # 前置
    # 打开浏览器访问网址
    driver = webdriver.Chrome()
    driver.get(web_url)
    loginp = LoginPage(driver)
    yield [driver,loginp]
    # 后置
    driver.quit()

# setupClass 和 teardownClass
@pytest.fixture(scope='class')
def class_demo():
    print("我是class前置")
    yield
    print("我是class后置")