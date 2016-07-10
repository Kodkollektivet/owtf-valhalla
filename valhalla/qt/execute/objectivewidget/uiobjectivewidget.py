# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectivewidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ObjectiveWidget(object):
    def setupUi(self, ObjectiveWidget):
        ObjectiveWidget.setObjectName("ObjectiveWidget")
        ObjectiveWidget.resize(793, 78)
        self.verticalLayout = QtWidgets.QVBoxLayout(ObjectiveWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(ObjectiveWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblObjectiveCode = QtWidgets.QLabel(self.widget)
        self.lblObjectiveCode.setObjectName("lblObjectiveCode")
        self.horizontalLayout.addWidget(self.lblObjectiveCode)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnShowHideObjectiveTools = QtWidgets.QPushButton(self.widget)
        self.btnShowHideObjectiveTools.setObjectName("btnShowHideObjectiveTools")
        self.horizontalLayout.addWidget(self.btnShowHideObjectiveTools)
        self.chkObjectiveCommands = QtWidgets.QCheckBox(self.widget)
        self.chkObjectiveCommands.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkObjectiveCommands.setTristate(False)
        self.chkObjectiveCommands.setObjectName("chkObjectiveCommands")
        self.horizontalLayout.addWidget(self.chkObjectiveCommands)
        self.verticalLayout.addWidget(self.widget)
        self.widgetObjectiveTools = QtWidgets.QWidget(ObjectiveWidget)
        self.widgetObjectiveTools.setObjectName("widgetObjectiveTools")
        self.widgetObjectiveToolsVerticalLayout = QtWidgets.QVBoxLayout(self.widgetObjectiveTools)
        self.widgetObjectiveToolsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetObjectiveToolsVerticalLayout.setObjectName("widgetObjectiveToolsVerticalLayout")
        self.verticalLayout.addWidget(self.widgetObjectiveTools)

        self.retranslateUi(ObjectiveWidget)
        QtCore.QMetaObject.connectSlotsByName(ObjectiveWidget)

    def retranslateUi(self, ObjectiveWidget):
        _translate = QtCore.QCoreApplication.translate
        ObjectiveWidget.setWindowTitle(_translate("ObjectiveWidget", "Form"))
        self.lblObjectiveCode.setText(_translate("ObjectiveWidget", "Objective code"))
        self.btnShowHideObjectiveTools.setText(_translate("ObjectiveWidget", "Show"))
        self.chkObjectiveCommands.setText(_translate("ObjectiveWidget", "All"))

