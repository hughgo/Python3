import tkinter
import socket
import threading

win =tkinter.Tk()
win.title("QQ客户端")
win.geometry("400x400+200+20")

ck =None
def getInfo():
    while True:
        data = ck.recv(1024)
        text.insert(tkinter.INSERT,data.decode('utf-8'))


def connecrServer():
    global ck
    ipStr =eip.get()
    portStr =eport.get()
    userStr = euser.get()
    clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clint.connect((ipStr, int(portStr)))
    clint.send(userStr.encode("utf-8"))
    ck =clint
    #等待接收数据
    t=threading.Thread(target=getInfo)
    t.start()
def sendMail():
    frient = efriend.get()
    senfStr = esend.get()
    senfStr =frient+":"+senfStr
    ck.send(senfStr.encode('utf-8'))


labeUser = tkinter.Label(win,text="username").grid(row= 0,column =0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win,textvariable = euser).grid(row= 0,column =1)

labelp = tkinter.Label(win,text="ip").grid(row= 1,column =0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable = eip).grid(row= 1,column =1)

labePort = tkinter.Label(win,text="port").grid(row= 2,column =0)
eport = tkinter.Variable()
entryPort = tkinter.Entry(win,textvariable = eport).grid(row= 2,column =1)

button = tkinter.Button(win,text="连接",command =connecrServer).grid(row= 3,column =1)

laberizhi = tkinter.Label(win,text="收到的内容").grid(row= 4,column =0)
text =tkinter.Text(win,width =20,height=5)
text.grid(row=4,column = 1)


tkinter.Label(win,text="发送内容").grid(row= 5,column =0)
esend = tkinter.Variable()
entrySend = tkinter.Entry(win,textvariable = esend).grid(row= 5,column =1)

tkinter.Label(win,text="发送给谁").grid(row= 6,column =0)
efriend = tkinter.Variable()
entryFriend = tkinter.Entry(win,textvariable = efriend).grid(row= 6,column =1)
button2 = tkinter.Button(win,text="发送",command =sendMail).grid(row= 7,column =1)


win.mainloop()

