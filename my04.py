# Author:Joker
# -*- codeing = utf-8 -*-
# @Time :2022/1/13 14:39
# @Author:zsj
# @Site :彭博数据库
# @File :my04.py
# @Software:PyCharm

from tkinter import *
from ctypes import *

# 窗口和标题

def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)
    pixel = gdi32.GetPixel(hdc, x, y)

    r = pixel & 0x0000ff
    g = pixel & 0x00ff00
    b = pixel & 0xff0000
    return([r, int(g / 256), int(b / 256 / 256)])

class MouseKeyEventDemo:
    def __init__(self):
        self.window = Tk()
        canvas = Canvas(self.window, width=50, height=50, bg="white")
        canvas.focus_set()  # 让画布获得焦点,对于键盘
        canvas.pack()
        self.msg = Label(self.window, text="what")
        self.msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        self.msg.pack()
        # 绑定鼠标左键事件，交由processMouseEvent函数去处理，事件对象会作为参数传递给该函数
        canvas.bind(sequence="<B1-Motion>", func=self.processMouseEvent)
        # 消息循环
        self.window.mainloop()

    # 处理鼠标事件，me为控件传递过来的鼠标事件对象
    def processMouseEvent(self, me):
        # print("me=", type(me))  # me= <class>
        r,g,b = get_color(me.x_root, me.y_root)
        self.msg['text'] = ("坐标", me.x_root, me.y_root, "RGB", r, g, b)

MouseKeyEventDemo()