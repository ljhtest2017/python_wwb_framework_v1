#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from ddt import ddt, data, file_data, unpack
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
# 引入测试数据
from TestDatas.common_data import *
from TestDatas.login_data import *


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        # 前置
        # 打开浏览器访问网址
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.loginp = LoginPage(self.driver)

    def tearDown(self):
        # 后置
        # 关闭浏览器
        self.driver.quit()

    # 正常场景用例 - 登录成功
    def test_login_success(self):
        # 输入正确的账户和密码登录
        self.loginp.login(login_succ['username'], login_succ['passwd'])
        # 断言
        self.assertEqual(IndexPage(self.driver).get_nickName(), login_succ['check'])

    # 异常场景用例 - 登录失败
    @data(*login_fail)
    def test_login_fail(self,data):
        self.loginp(data['username'],data['passwd'])
        self.assertEqual(self.loginp.get_errorMsg_fromLoginArea(), data['check'])
    # def test_login_fail_noUser(self):
    #     self.loginp.login('', 'python')
    #     self.assertEqual(self.loginp.get_errorMsg_fromLoginArea(), '请输入手机号')
    #
    # def test_login_fail_noPasswd(self):
    #     self.loginp.login('18684720553', '')
    #     self.assertEqual(self.loginp.get_errorMsg_fromLoginArea(), '请输入密码')
    #
    # def test_login_fail_wrong_userForamt(self):
    #     pass
