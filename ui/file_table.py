#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

__author__ = 'zengxianxi'


class ScrolledList(Frame):
    def __init__(self, master=None, files=[], parent=None):
        Frame.__init__(self, master)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(files)

    def processEvent(selft, event):
        if event.keysym == "Delete":
            #处理删除
            pass


    def makeWidgets(self, files):
        list = Listbox(self, relief=SUNKEN)
        list.bind("<Key>", self.processEvent)

        v_bar = Scrollbar(self)
        v_bar.config(command=list.yview)
        v_bar.pack(side=RIGHT, fill=Y)
        list.config(yscrollcommand=v_bar.set)

        h_bar = Scrollbar(self, orient=HORIZONTAL)
        h_bar.config(command=list.xview)
        h_bar.pack(side=BOTTOM, fill=X)
        list.config(xscrollcommand=h_bar.set)

        list.pack(side=LEFT, expand=YES, fill=BOTH)

        for file in files:
            list.insert(END, file)
        self.listbox = list

    def __getattr__(self, item):
        if item == "filenames":
            len = self.listbox.size()
            return self.listbox.get(0, len)
        else:
            raise AttributeError


if __name__ == '__main__':
    datas = {
        "curdir": "/Users/zengxianxi/Temp",
        "zipName": "abc",
        "filenames": [
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/zip_model.py"
        ]
    }
    app = Tk()
    list = ScrolledList(app, datas["filenames"])
    # len = list.listbox.size()
    # print list.listbox.get(0, len)

    print list.filenames

    app.mainloop()
