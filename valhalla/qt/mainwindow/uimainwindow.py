# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 784)
        self.mainWindowCentralwidget = QtWidgets.QWidget(MainWindow)
        self.mainWindowCentralwidget.setObjectName("mainWindowCentralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWindowCentralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.mainWindowCentralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabExecute = QtWidgets.QWidget()
        self.tabExecute.setObjectName("tabExecute")
        self.tabExecuteCerticalLayout = QtWidgets.QVBoxLayout(self.tabExecute)
        self.tabExecuteCerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabExecuteCerticalLayout.setObjectName("tabExecuteCerticalLayout")
        self.tabWidget.addTab(self.tabExecute, "")
        self.tabManageContainers = QtWidgets.QWidget()
        self.tabManageContainers.setObjectName("tabManageContainers")
        self.tabManageVerticalLayout = QtWidgets.QVBoxLayout(self.tabManageContainers)
        self.tabManageVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabManageVerticalLayout.setObjectName("tabManageVerticalLayout")
        self.tabWidget.addTab(self.tabManageContainers, "")
        self.tabResults = QtWidgets.QWidget()
        self.tabResults.setObjectName("tabResults")
        self.tabResultsVerticalLayout = QtWidgets.QVBoxLayout(self.tabResults)
        self.tabResultsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabResultsVerticalLayout.setObjectName("tabResultsVerticalLayout")
        self.tabWidget.addTab(self.tabResults, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.mainWindowCentralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OWTF Valhalla"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExecute), _translate("MainWindow", "Execute"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabManageContainers), _translate("MainWindow", "Manage Containers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResults), _translate("MainWindow", "Results"))

