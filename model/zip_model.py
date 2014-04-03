#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import zipfile
from os.path import *
from chardet import detect


__author__ = 'zengxianxi'

logger = logging.getLogger("zip_model")


def zip_file(cur_dir, src, dst):
    logger.debug("开始压缩：%s到%s", src, dst)
    zip = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
    for src_file in src:
        logger.debug("正在处理:%s", src_file)
        if isdir(src_file):
            logger.debug("正在处理:%s", src_file)
            #遍历文件
            for root, dirs, files in os.walk(src_file):
                logger.debug("遍历dir:%s", root)
                for file in files:
                    absPath = join(root, file)
                    #把文件名转换成相对路径，并对文件名进行编码
                    rel_path = relpath(absPath, cur_dir)

                    if not isinstance(rel_path, unicode):
                        rel_path = unicode(rel_path, "utf-8")

                    rel_path = rel_path.encode("gbk")
                    logger.debug("压入文件：%s", rel_path)
                    zip.write(absPath, rel_path)
        else:
            rel_path = relpath(src_file, dirname(src_file))
            if not isinstance(rel_path, unicode):
                rel_path = unicode(rel_path, "utf-8")

            arc_name = rel_path.encode("gbk")
            logger.debug("压入文件：%s", src_file)
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
    fhZip.close()



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename="dev.log")
    files = ['/Users/zengxianxi/Projects/cbh/documents/current/云营业厅工程实施规划']
    dst = '/Users/zengxianxi/Projects/MacZip/test.zip'
    cur_dir = "/Users/zengxianxi/Projects/cbh/documents/current"
    zip_file(cur_dir, files, dst)
