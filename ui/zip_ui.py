#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
import os
from Tkinter import *
import tkFileDialog
from ttk import *
import file_table
from model.zip_model import zip_file

__author__ = 'zengxianxi'

win_options = {"width": 430, "height": 320, "top": 120}


class Application(Frame):
    """
    压缩文件的主显示窗口
    """

    def __init__(self, master=None, **datas):
        Frame.__init__(self, master)
        self.file_opt = {"defaultextension": ".zip",
                         "initialfile": datas["zipName"],
                         "initialdir": datas["curdir"],
                         "title": "压缩为：",
                         "parent": self}
        self.dst_zip = StringVar()
        self.dst_zip.set(datas["curdir"] + os.sep + datas["zipName"] + ".zip")

        self.createWidgets(datas)
        self.pack()

    def createWidgets(self, datas):
        """
        创建页面元素
        """
        tabs = Notebook(self, width=win_options["width"], height=win_options["height"] - 90)
        tab1 = Frame(tabs)
        tab2 = Frame(tabs)
        tab3 = Frame(tabs)
        tab4 = Frame(tabs)
        tabs.add(tab1, text="常规")
        tabs.add(tab2, text="文件列表")
        tabs.add(tab3, text="密码")
        tabs.add(tab4, text="注释")
        tabs.pack()

        self.createTab1(tab1)
        self.createTab2(tab2, datas["filenames"])

        #定义确定、取消按钮
        frame = Frame(self, padding=2)
        Button(frame, text="取消", command=self.quit).pack(side=LEFT)
        Button(frame, text="确定", command=self.exc_zip).pack()
        frame.pack(side=RIGHT)


    #event -------------
    def asksaveasfilename(slef):
        # get filename
        filename = tkFileDialog.asksaveasfilename(**slef.file_opt)
        if filename:
            slef.dst_zip.set(filename)

    def createTab1(self, tab1):
        grid_column_options = {"pady": 5, "padx": "2"}
        Label(tab1, text="压缩文件名").grid(row=0, column=0, sticky=W, **grid_column_options)
        Button(tab1, text="浏览", command=self.asksaveasfilename).grid(row=0, column=1, sticky=E,
                                                                      **grid_column_options)
        Entry(tab1, textvariable=self.dst_zip, width=45).grid(row=1, column=0, columnspan=2, sticky=W,
                                                              **grid_column_options)

    def createTab2(self, tab2, filenames):
        self.fileList = file_table.ScrolledList(tab2, filenames)

    def exc_zip(self):
        try:
            files = self.fileList.filenames
            dst = self.dst_zip.get()
            zip_file(self.file_opt["initialdir"], files, dst)
            self.quit()
        except Exception:
            pass


def run(datas):
    """
    datas = {
        "curdir": "/Users/zengxianxi/Temp",
        "zipName": "abc",
        "filenames": [
            "/Users/zengxianxi/fiel1.py",
            "/Users/zengxianxi/fiel2.py"
        ]
    }
    """
    root = Tk()
    root.title("MacZip")
    root.resizable(width=False, height=False)  #宽不可变, 高可变,默认为True
    app = Application(master=root, **datas)

    w = win_options["width"]
    h = win_options["height"]
    x = root.winfo_screenwidth() / 2 - (w / 2)
    y = win_options["top"]

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.mainloop()
    # root.destroy()


if __name__ == "__main__":
    datas = {
        "curdir": "/Users/zengxianxi/Temp",
        "zipName": "abc",
        "filenames": [
            "/Users/zengxianxi/Projects/maczip/model/__init__.py",
            "/Users/zengxianxi/Projects/maczip/model/zip_model.py"
        ]
    }
    run(datas)