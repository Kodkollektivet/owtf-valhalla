# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'executewidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExecuteWidget(object):
    def setupUi(self, ExecuteWidget):
        ExecuteWidget.setObjectName("ExecuteWidget")
        ExecuteWidget.resize(1104, 712)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ExecuteWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.objectivesScrollArea = QtWidgets.QScrollArea(ExecuteWidget)
        self.objectivesScrollArea.setWidgetResizable(True)
        self.objectivesScrollArea.setObjectName("objectivesScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 538, 692))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.objectivesScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.objectivesScrollArea)
        self.menuWidget = QtWidgets.QWidget(ExecuteWidget)
        self.menuWidget.setObjectName("menuWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menuWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.menuWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.widget = QtWidgets.QWidget(self.menuWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Host")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.btnAdd = QtWidgets.QPushButton(self.widget)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_2.addWidget(self.btnAdd)
        self.verticalLayout_2.addWidget(self.widget)
        self.btnExecute = QtWidgets.QPushButton(self.menuWidget)
        self.btnExecute.setObjectName("btnExecute")
        self.verticalLayout_2.addWidget(self.btnExecute)
        self.horizontalLayout.addWidget(self.menuWidget)

        self.retranslateUi(ExecuteWidget)
        QtCore.QMetaObject.connectSlotsByName(ExecuteWidget)

    def retranslateUi(self, ExecuteWidget):
        _translate = QtCore.QCoreApplication.translate
        ExecuteWidget.setWindowTitle(_translate("ExecuteWidget", "Form"))
        self.btnAdd.setText(_translate("ExecuteWidget", "Add"))
        self.btnExecute.setText(_translate("ExecuteWidget", "Execute"))

