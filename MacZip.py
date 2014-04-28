#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import sys
from os.path import isdir, join, abspath, dirname

from ui import zip_ui

__author__ = 'zengxianxi'


def main(fileNames):
    datas = {}
    if isdir(fileNames[0]):
        curdir = abspath(join(fileNames[0], os.path.pardir))
    else:
        curdir = dirname(fileNames[0])
    datas["filenames"] = fileNames
    datas["curdir"] = curdir
    datas["zipName"] = "archive"
    logger.debug("传入数据:%s", datas)
    zip_ui.run(datas)


if __name__ == "__main__":
    #配置日志信息
    logFile = os.path.expanduser("~") + '/Library/Logs/MacZip/MacZip.log'

    if not os.path.exists(dirname(logFile)):
        os.makedirs(dirname(logFile))

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=logFile)
    logger = logging.getLogger("MacZip")
    len = len(sys.argv)

    logger.debug("接收到%d个参数:%s", len, sys.argv)
    if len > 1:
        fileNames = sys.argv.__getslice__(1, len)
        logger.debug("接收到的文件为：%s", fileNames)
        main(fileNames)
    else:
        pass