import tkinter

def func():
    print("qianxiao is good man")


win = tkinter.Tk()
win.title("qianxiao")
win.geometry("400x400+800+400")
#创建按钮
button1 = tkinter.Button(win,text= "按钮",
                        command =func,
                        width = 30,
                        height = 3)

button2 = tkinter.Button(win,text= "按钮",
                        command =lambda:print("hello"))#匿名函数


button3 = tkinter.Button(win,text= "按钮",
                        command =win.quit)#退出

button1.pack()
button2.pack()
button3.pack()
win.mainloop()
