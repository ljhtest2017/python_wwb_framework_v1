#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import logging
from Common import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common.dir_config import screenshot_dir


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    #等待操作
    def wait_element_to_visiblity(self, locator, wait_times=20, poll_frequency=0.5, model=None):
        # 开始时间
        try:
            start_time = time.time()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束时间
            end_time = time.time()
            logging.info('xxxx')
        except:
            # 获取异常
            logging.exception("xxxxx")
            # 截图
            self._screenshot(model)
            # 抛出异常
            raise
    #元素定位操作
    def get_element(self,locator, model=None):
        try:
            return self.driver.find_element(locator[0],locator[1])
        except:
            # 获取异常
            logging.exception("xxxxx")
            # 截图
            self._screenshot(model)
            # 抛出异常
            raise
    #文本输入操作
    def input_text(self,locator, text, model=None):
        ele = self.get_element(locator)
        try:
            ele.send_keys(text)
        except:
            # 获取异常
            logging.exception("xxxxx")
            # 截图
            self._screenshot(model)
            # 抛出异常
            raise
    #元素点击操作
    def click_element(self,locator, model=None):
        ele = self.get_element(locator)
        try:
            ele.click()
        except:
            # 获取异常
            logging.exception("xxxxx")
            # 截图
            self._screenshot(model)
            # 抛出异常
            raise
    #获取元素文本操作
    def get_text(self, locator, model=None):
        ele = self.get_element(locator)
        try:
            return ele.text
        except:
            pass
            # 获取异常
            # 截图
            # 抛出异常
    #弹出框操作
    #js脚本执行
    #上传操作
    # 截屏
    def _screenshot(self, model_name):
        # 时间
        filePath = screenshot_dir + '/{0}_{1}.png'.format(model_name, time.strftime("%Y%m%d_%H%M%S"))
        self.driver.save_screenshot()

