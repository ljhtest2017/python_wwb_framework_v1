#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

# 框架项目顶级目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
testdatas_dir = os.path.join(base_dir,  "TestDatas")
testcases_dir = os.path.join(base_dir, "TestCases")
htmlreport_dir = os.path.join(base_dir, "HtmlTestReport")
logs_dir = os.path.join(base_dir, "Logs")
screenshot_dir = os.path.join(base_dir, "ScreenShot")

if __name__ == '__main__':
    print(base_dir)
    print(testcases_dir)
    print(testdatas_dir)
    print(htmlreport_dir)
    print(logs_dir)
    print(screenshot_dir)
