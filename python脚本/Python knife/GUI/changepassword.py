# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepassword.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_changepassword(object):
    def setupUi(self, changepassword):
        changepassword.setObjectName("changepassword")
        changepassword.resize(325, 80)
        changepassword.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(255, 0, 0);")
        self.label = QtWidgets.QLabel(changepassword)
        self.label.setGeometry(QtCore.QRect(24, 48, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(changepassword)
        self.label_2.setGeometry(QtCore.QRect(12, 17, 81, 16))
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(changepassword)
        self.layoutWidget.setGeometry(QtCore.QRect(94, 10, 135, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.changeuserEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.changeuserEdit.setStyleSheet("color: rgb(255, 0, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.changeuserEdit.setObjectName("changeuserEdit")
        self.verticalLayout.addWidget(self.changeuserEdit)
        self.changepasswordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.changepasswordEdit.setStyleSheet("color: rgb(255, 0, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.changepasswordEdit.setObjectName("changepasswordEdit")
        self.verticalLayout.addWidget(self.changepasswordEdit)
        self.layoutWidget_2 = QtWidgets.QWidget(changepassword)
        self.layoutWidget_2.setGeometry(QtCore.QRect(234, 14, 77, 54))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.changeuserButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.changeuserButton.setObjectName("changeuserButton")
        self.verticalLayout_3.addWidget(self.changeuserButton)
        self.changepasswordButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.changepasswordButton.setObjectName("changepasswordButton")
        self.verticalLayout_3.addWidget(self.changepasswordButton)

        self.retranslateUi(changepassword)
        self.changepasswordButton.clicked.connect(changepassword.close)
        QtCore.QMetaObject.connectSlotsByName(changepassword)

    def retranslateUi(self, changepassword):
        _translate = QtCore.QCoreApplication.translate
        changepassword.setWindowTitle(_translate("changepassword", "修改密码"))
        self.label.setText(_translate("changepassword", "请输入密码："))
        self.label_2.setText(_translate("changepassword", "请输入用户名："))
        self.changeuserButton.setText(_translate("changepassword", "确定"))
        self.changepasswordButton.setText(_translate("changepassword", "取消"))

