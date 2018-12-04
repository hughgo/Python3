import tkinter
win = tkinter.Tk()
win.title("qianxiao")
win.geometry("400x400+800+400")

def showInfo():
    print(entry.get())

entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win,text= "按钮",command = showInfo)

button.pack()
win.mainloop()