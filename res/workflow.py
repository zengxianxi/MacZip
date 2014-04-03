# -*- coding: utf-8 -*-
import os
import sys

__author__ = 'zengxianxi'

args = ""
for p in sys.argv[1:]:
    args = args + p + " "

app = "open /Applications/maczip.app --args " + args
os.system(app)