#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from ddt import ddt, data, file_data, unpack
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
# 引入测试数据
from TestDatas.common_data import *
from TestDatas.login_data import *


# @ddt
# class TestLogin(unittest.TestCase):
#     def setUp(self):
#         # 前置
#         # 打开浏览器访问网址
#         self.driver = webdriver.Chrome()
#         self.driver.get(url)
#         self.loginp = LoginPage(self.driver)
#
#     def tearDown(self):
#         # 后置
#         # 关闭浏览器
#         self.driver.quit()
#
#     # 正常场景用例 - 登录成功
@pytest.mark.usefixtures("function_diff_demo")
def test_diffrent_case():
    print("我是特别的用例======要用特别的fixture=====所以我不在测试类当中")



# fixture的函数名称
@pytest.mark.usefixtures("class_demo")
@pytest.mark.usefixtures("init_loginEnv")
class TestLogin:
    # 正常场景用例--登录成功
    # init_loginEnv接收fixture运行的返回值[driver, loginp]
    def test_login_success(self, init_loginEnv):
        # # 输入正确的账户和密码登录
        # self.loginp.login(login_succ['username'], login_succ['passwd'])
        # # 断言
        # self.assertEqual(
        #     IndexPage(
        #         self.driver).get_nickName(),
        #     login_succ['check'])
        init_loginEnv[1].login(login_succ["username"],login_succ["passwd"])
        # 断言
        assert IndexPage(init_loginEnv[0].get_nickName()) == login_succ['check']

    # 异常场景用例 - 登录失败
    # @data(*login_fail)
    # def test_login_fail(self, data):
    #     self.loginp(data['username'], data['passwd'])
    #     self.assertEqual(
    #         self.loginp.get_errorMsg_fromLoginArea(),
    #         data['check'])
    @pytest.mark.parametrize("data",login_noData)
    def test_login_fail_noUser(self, init_loginEnv):
        init_loginEnv[1].login(data['username'],data['passwd'])
        # 断言
        assert  init_loginEnv[1].get_errorMsg_fromLoginArea() == data['check']
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
