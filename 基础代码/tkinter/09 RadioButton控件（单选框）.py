import tkinter
win = tkinter.Tk()
win.title("qianxiao")
win.geometry("400x400+800+400")
def updata():
    print(r.get())
#一组单选框要绑定同一个变量
r = tkinter.IntVar()
radio1 =tkinter.Radiobutton(win , text= "one",value = 1,variable = r,command = updata)
radio1.pack()
radio2 =tkinter.Radiobutton(win , text= "two",value = 2,variable = r,command = updata)
radio2.pack()

win.mainloop()