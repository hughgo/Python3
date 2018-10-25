import tkinter

win = tkinter.Tk()
win.title("qianxiao")
win.geometry("400x400+800+400")

'''
标签空间：可以显示文本

'''
#win ： 父窗体
#text:显示文本内容
#bg:背景色
#fg:字体颜色
#wraplength : 指定text文本中多宽进行换行
#justify：换行后的对齐方式
#anchor:位置  n 靠上   e靠右     s靠下    w靠左  enter居中  ne   se   sw  nw
label = tkinter.Label(win,
                      text="qianxiao is very good man",
                      bg = "blue",
                      fg = "red",
                      font=("黑体",20),
                      width=100,
                      height = 10,
                      wraplength=120,
                      justify = "left",
                      anchor = "center")


#显示到视图
label.pack()


win.mainloop()