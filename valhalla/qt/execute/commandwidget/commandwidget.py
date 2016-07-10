from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pprint import pprint as pp

from .uicommandwidget import Ui_WidgetCommand
from valhalla.qt.communicate import COMMUNICATE


class CommandWidget(QWidget, Ui_WidgetCommand):
    def __init__(self, command, parent=None):
        if parent is None:
            raise Exception('Please provide parent')
        else:
            super().__init__(parent=parent)

        self.setupUi(self)
        self._parent = self.parent()
        self.com = COMMUNICATE
        self.command = command

        self.lblCommand.setText(self.command['command'].replace('@@@HOST@@@', 'host'))
        self.lblDescription.setText(self.command['description'] if not '?' else 'No description')
        self.lblNoise.setText(self.command['noise'] if not '?' else 'Unknown')
        self.lblContainer.setText(self.command['image'])

        self.chkSelect.stateChanged.connect(self.select_unselect_command)

    def select_unselect_command(self):
        """When command is selected/unselected.
        append/remove it from selected_commands list.
        """
        if self in self._parent.selected_commands:
            self._parent.selected_commands.remove(self)
        else:
            self._parent.selected_commands.append(self)
        #print(len(self._parent.selected_commands))
        self.com.statusbar_message.emit('Commands: {}'.format(str(len(self._parent.selected_commands))))

