import tkinter
win = tkinter.Tk()
win.title("qianxiao")
win.geometry("400x400+800+400")
"""
输入控件
用于显示简单的文本
"""
#show  密文显示   show = "*"
#绑定变量
e = tkinter.Variable()
entry = tkinter.Entry(win,show= "",textvariable = e)
entry.pack()

#e就代表输入框这个对象
#设置值
e.set("qianxiao is good man ")
#打印值
print(e.get())
print(entry.get())

win.mainloop()