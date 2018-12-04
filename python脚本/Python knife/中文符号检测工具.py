import tkinter
import webbrowser
import re

#本程序是一个中文字符和中文检测工具
#中文字符自己添加，我只添加了一点
#输入字符串，点击检查文本即可判断有没有中文字符
# qianxiao996精心制作
#博客地址：https://blog.csdn.net/qq_36374896


win = tkinter.Tk()
win.title("中文字符检测工具   "+"by qianxiao996"+"    -----博客地址：https://blog.csdn.net/qq_36374896 -----")

#获取全部内容
def showInfo():
    returntext.delete(0.0, tkinter.END)   #清空returntext中的内容
    str=text.get(0.0, tkinter.END)    #得到text中的文本
    list=['，','。','：','￥','；','“','‘']  #中文字符可以自行添加
    endstr=""  #存放文本中的特殊字符
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+') #匹配中文的正则表达式
    for i in str:   #遍历整个文本是否含有中文字符
        if i in list:   #遍历是否含有list中的字符
            endstr+=i
        elif zhPattern.search(i):   #遍历是否是汉字
            endstr += i
    if endstr !='':   #输出中文字符
        returntext.insert(tkinter.INSERT, "中文字符："+endstr)
    else:
        returntext.insert(tkinter.INSERT, "恭喜您，文本中没有中文字符")
#清空
def clearText():
    text.delete(0.0, tkinter.END)
    returntext.delete(0.0, tkinter.END)
def click():
    webbrowser.open("https://blog.csdn.net/qq_36374896")

#创建滚动条
scroll = tkinter.Scrollbar()
#height:显示的行数
str = "请在此输入您的文本(请删除此字符串)："
text = tkinter.Text(win,width =80,height = 50,bg='#F0FFFF',fg="#FF00FF")

text.insert(tkinter.INSERT,str)
#side 放到窗体的哪一侧
scroll.pack(side  =tkinter.RIGHT,fill = tkinter.Y)
text.pack(side  =tkinter.LEFT,fill = tkinter.Y,)
#关联
scroll.config(command =text.yview)
text.config(yscrollcommand =scroll.set)
label = tkinter.Label(win,text= " 欢  迎  您  的  使  用 !",bg='#F0F8FF',fg="green").pack(side="bottom",ipady="8",ipadx="44")
zuozhe=tkinter.Button(win,text= "作者主页",command =click,bg='#F0F8FF',fg="green").pack(side="bottom",ipady="30",ipadx="80")
close = tkinter.Button(win,text= "关闭程序",command =win.quit,bg='#F0F8FF',fg="green").pack(side="bottom",ipady="30",ipadx="80")
clear = tkinter.Button(win,text= "清空文本",command = clearText,bg='#F0F8FF',fg="green").pack(side="bottom",ipady="30",ipadx="80")
button = tkinter.Button(win,text= "检查文本",command = showInfo,bg='#F0F8FF',fg="green").pack(side="bottom",ipady="30",ipadx="80")
returntext = tkinter.Text(win,width = 30,height=30,bg='#F0FFFF',foreground='red')
returntext.pack(side="top",ipadx="3")
win.mainloop()