#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        # 前置
        # 打开浏览器访问网址
        self.driver = webdriver.Chrome()
        self.driver.get('http://120.79.176.157:8012/Index/login.html')
        self.loginp = LoginPage(self.driver)

    def tearDown(self):
        # 后置
        # 关闭浏览器
        self.driver.quit()
    def test_login_success(self):
        # 输入正确的账户和密码登录
        self.loginp.login('18684720553', 'python')
        # 断言
        self.assertEqual(IndexPage(self.driver).get_nickName(), '我的账户[小小蜂96027]')

    def test_login_fail_noUser(self):
        self.loginp.login('', 'python')
        self.assertEqual(self.loginp.get_errorMsg_fromLoginArea(), '请输入手机号')

    def test_login_fail_noPasswd(self):
        self.loginp.login('18684720553', '')
        self.assertEqual(self.loginp.get_errorMsg_fromLoginArea(), '请输入密码')

    def test_login_fail_wrong_userForamt(self):
        pass
