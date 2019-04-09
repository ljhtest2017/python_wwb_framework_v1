#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 正常场景
# 前置
# 1、用户余额够用：充值一个亿
# 2、查看有多少余额，然后不够200块，我就去充值，如果有就不充值
# 3、不走web页面，走接口来实现。
# 有可投资的标
# 步骤
#标页面-获取用户可用余额
# 首页直接选第一个标，标页面输入金额，进行投资，投资金额200，点击投资成功弹出框中的，查看并激活按钮。
#验证
# 个人页面：获取用户可用余额
# 比对： 余额=投资前-投资后
# 个人页面还剩多少钱，有没有少。利息是多少
import unittest
from TestDatas.common_data import *
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.invest_page import BigPage
from PageObjects.user_page import UserPage

class TestInvest(unittest.TestCase):

    def setUp(self):
        # 打开浏览器，登录前程贷
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        LoginPage(self.driver).login(user, passwd)

    def tearDown(self):
        self.driver.quit()

    def test_invest_success(self):
        # 首页直接选第一个标，
        IndexPage(self.driver).click_first_invest_button()
        # 标页面-获取用户可用余额
        big_page = BigPage(self.driver)
        user_money_before_invest = big_page.get_user_left_money()
        # 标页面输入金额，进行投资，投资金额200，
        big_page.invest(200)
        # 点击投资成功弹出框中的，查看并激活按钮。
        big_page.click_active_button_from_invest_success_puput()
        # 验证
        # 个人页面：获取用户可用余额
        user_money_after_invest = UserPage(self.driver).get_user_left_money()
        # 比对： 余额=投资前-投资后
        self.assertEqual(200,int(float(user_money_before_invest)-float(user_money_after_invest)))

    def test_invest_fail_no100(self):
        pass

    def test_invest_fail_no10(self):
        pass

# 异常场景 - 用户余额不足 - 手工用例
# 异常场景 - 投资》 标的可投余额 - 手工用例



