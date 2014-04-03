#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import zipfile
from os.path import *

__author__ = 'zengxianxi'


def zip_file(src, dst):
    zip = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
    for src_file in src:
        if isdir(src_file):
            #遍历文件
            for root, dirs, files in os.walk(src):
                logging.debug(u"遍历dir:", root)
                for file in files:
                    absPath = join(root, file)
                    #把文件名转换成相对路径，并对文件名进行编码
                    rel_path = unicode(relpath(absPath, src), 'utf-8').encode("gbk")
                    logging.debug(u"压入文件：", rel_path)
                    zip.write(absPath, rel_path)
        else:
            arc_name = unicode(relpath(src_file, dirname(src_file))).encode("gbk")
            logging.debug(u"压入文件：", src_file)
            zip.write(src_file, arc_name)
    zip.close()


def unzip_file(src, dst):
    if not exists(dst):
        os.makedirs(dst)
    fhZip = open(src, 'rb')
    z = zipfile.ZipFile(fhZip)
    for name in z.namelist():
        #对文件名进行编码
        fileName = join(dst, unicode(name, "gbk").encode("utf-8"))
        if not exists(dirname(fileName)):
            os.mkdir(dirname(fileName))

        fh = open(fileName, 'wb')
        fh.write(z.read(name))
        fh.close()
        # z.extract(name, dst)
    fhZip.close()
