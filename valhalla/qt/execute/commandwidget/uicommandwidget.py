# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commandwidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetCommand(object):
    def setupUi(self, WidgetCommand):
        WidgetCommand.setObjectName("WidgetCommand")
        WidgetCommand.resize(576, 178)
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetCommand)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(WidgetCommand)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblCommand = QtWidgets.QLabel(self.widget)
        self.lblCommand.setObjectName("lblCommand")
        self.horizontalLayout.addWidget(self.lblCommand)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.chkSelect = QtWidgets.QCheckBox(self.widget)
        self.chkSelect.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkSelect.setObjectName("chkSelect")
        self.horizontalLayout.addWidget(self.chkSelect)
        self.verticalLayout.addWidget(self.widget)
        self.lblNoise = QtWidgets.QLabel(WidgetCommand)
        self.lblNoise.setObjectName("lblNoise")
        self.verticalLayout.addWidget(self.lblNoise)
        self.lblDescription = QtWidgets.QLabel(WidgetCommand)
        self.lblDescription.setObjectName("lblDescription")
        self.verticalLayout.addWidget(self.lblDescription)
        self.lblContainer = QtWidgets.QLabel(WidgetCommand)
        self.lblContainer.setObjectName("lblContainer")
        self.verticalLayout.addWidget(self.lblContainer)

        self.retranslateUi(WidgetCommand)
        QtCore.QMetaObject.connectSlotsByName(WidgetCommand)

    def retranslateUi(self, WidgetCommand):
        _translate = QtCore.QCoreApplication.translate
        WidgetCommand.setWindowTitle(_translate("WidgetCommand", "Form"))
        self.lblCommand.setText(_translate("WidgetCommand", "Tool"))
        self.chkSelect.setText(_translate("WidgetCommand", "Select"))
        self.lblNoise.setText(_translate("WidgetCommand", "Noise"))
        self.lblDescription.setText(_translate("WidgetCommand", "Description"))
        self.lblContainer.setText(_translate("WidgetCommand", "Container"))

