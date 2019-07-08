#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
from logging.handlers import RotatingFileHandler
import time
from Common import dir_config

fmt = "%(asctime)s %(levelname)s %(filename)s %(funcName)s [line:%(lineno)d]"
datefmt = "%a, %d, %b %Y %H:%M:%S"
handler_1 = logging.StreamHandler()
curTime = time.strftime("%Y-%m-%d %H%M%S", time.localtime())
filename =  dir_config.logs_dir+"/Web_Autotest_{0}.log".format(curTime)
handler_2 = RotatingFileHandler(filename)
# 设置root-logger的输出内容格式，输出渠道
logging.basicConfig(format=fmt,  datefmt=datefmt,level=logging.INFO, handlers=[handler_1,handler_2])

if __name__ == '__main__':

    logging.info("hehe")

