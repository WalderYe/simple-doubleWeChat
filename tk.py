from tkinter import *
from tkinter.filedialog import askdirectory
import os
import subprocess
def selectPath():
    path_ = askdirectory()
    path.set(path_)
def startWC():
    f = path.get()
    f = f.replace("/", os.sep)
    subprocess.Popen("start WeChat.exe && WeChat.exe", shell = True, cwd = f)
root = Tk()
path = StringVar()
root.title("双开微信")
Label(root, text = "微信安装目录：").grid(row=0, column=0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "选择目录", command = selectPath).grid(row = 0, column = 2)
Button(root, text = "启动", command = startWC).grid(row = 1, column = 1)
root.mainloop()
