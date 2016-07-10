from pprint import pprint as pp
import copy

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from valhalla.dockerutils import commands as objectives
from valhalla.qt.wrappers.qtowtfcontainer import get_owtf_c
from .uiexecutewidget import Ui_ExecuteWidget
from valhalla.qt.execute.objectivewidget.objectivewidget import ObjectiveWidget
from valhalla.qt.execute.commandwidget.commandwidget import CommandWidget
from valhalla.qt.communicate.communicate import COMMUNICATE


class ExecuteWidget(QWidget, Ui_ExecuteWidget):
    def __init__(self, parent=None):
        if parent is None:
            raise Exception('Please provide parent')
        else:
            super().__init__(parent=parent)
            self._parent = self.parent()

        self.setupUi(self)
        self.all_commands = []  # All commands
        self.objectives = []  # Code groups
        self.selected_commands = []  # Selected commands
        self.hosts = []
        self.com = COMMUNICATE

        self.btnAdd.clicked.connect(self.add_host)
        self.btnExecute.clicked.connect(self.execute)
        #pp(objectives)
        for objective in sorted(objectives, key=lambda k: k['code']):
            obj = ObjectiveWidget(objective, parent=self)
            for command in objective['commands']:
                command_widget = CommandWidget(command, parent=self)
                obj.objective_commands.append(command_widget)
                self.all_commands.append(command_widget)
                obj.widgetObjectiveToolsVerticalLayout.addWidget(command_widget)
            self.objectives.append(obj)
            self.verticalLayout_3.addWidget(obj)

        self.listWidget.itemClicked.connect(self.remove_host)

    def add_host(self):
        host = self.lineEdit.text()
        if host not in self.hosts:
            self.listWidget.addItem(host)
            self.hosts.append(host)
            self.lineEdit.setText('')
        else:
            QMessageBox.information(self, 'Alert!', 'Target already added.')
            self.lineEdit.setText('')

    def remove_host(self):
        list_items = self.listWidget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            item_text = item.text()
            if item_text in self.hosts:  # Remove from hosts
                self.hosts.remove(item_text)
            self.listWidget.takeItem(self.listWidget.row(item))

    def execute(self):
        if not len(self.hosts) > 0:
            QMessageBox.information(self, 'Alert!', 'Please add at least one target')
        elif not len(self.selected_commands) > 0:
            QMessageBox.information(self, 'Alert!', 'Please selecta at least one command!')
        else:
            for command in self.selected_commands:
                status, oc = get_owtf_c(image=command.command['image'])
                if status:  # If image is found
                    self.com.statusbar_message.emit('Building: {}'.format(oc.image))
                    oc.build()
                    self.com.statusbar_message.emit('Starting: {}'.format(oc.image))
                    oc.start()
                    for host in self.hosts:
                        c = command.command['command']
                        c = c.replace('@@@HOST@@@', host)
                        self.com.statusbar_message.emit('Start executing commands...')
                        oc.add_command({'command': c})
                    oc.execute()

