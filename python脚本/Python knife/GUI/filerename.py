# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filerename.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_renameForm(object):
    def setupUi(self, renameForm):
        renameForm.setObjectName("renameForm")
        renameForm.resize(349, 82)
        renameForm.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(255, 0, 0);")
        self.renameedit = QtWidgets.QLineEdit(renameForm)
        self.renameedit.setGeometry(QtCore.QRect(95, 15, 241, 20))
        self.renameedit.setStyleSheet("color: rgb(255, 0, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.renameedit.setObjectName("renameedit")
        self.renamelabel = QtWidgets.QLabel(renameForm)
        self.renamelabel.setGeometry(QtCore.QRect(14, 17, 81, 16))
        self.renamelabel.setObjectName("renamelabel")
        self.layoutWidget = QtWidgets.QWidget(renameForm)
        self.layoutWidget.setGeometry(QtCore.QRect(178, 47, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.renameButton = QtWidgets.QPushButton(self.layoutWidget)
        self.renameButton.setStyleSheet("")
        self.renameButton.setObjectName("renameButton")
        self.horizontalLayout.addWidget(self.renameButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(renameForm)
        self.pushButton_2.clicked.connect(renameForm.close)
        QtCore.QMetaObject.connectSlotsByName(renameForm)

    def retranslateUi(self, renameForm):
        _translate = QtCore.QCoreApplication.translate
        renameForm.setWindowTitle(_translate("renameForm", "重命名"))
        self.renamelabel.setText(_translate("renameForm", "请输入文件名："))
        self.renameButton.setText(_translate("renameForm", "确定"))
        self.pushButton_2.setText(_translate("renameForm", "取消"))

