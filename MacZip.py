#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    zip_ui.run(datas)


if __name__ == "__main__":
    len = len(sys.argv)
    fileNames = sys.argv.__getslice__(1, len)
    main(fileNames)

