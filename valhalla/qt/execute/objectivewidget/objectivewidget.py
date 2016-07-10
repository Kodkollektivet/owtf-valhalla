from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from .uiobjectivewidget import Ui_ObjectiveWidget


class ObjectiveWidget(QWidget, Ui_ObjectiveWidget):
    """Objective Widget.
    Is a relation to OWASP code.
    It holds the commands that is related to the
    OWASP objective code.
    """
    def __init__(self, objective, parent=None):
        if parent is None:
            raise Exception('Please provide parent')
        else:
            super().__init__(parent=parent)
            self._parent = self.parent()

        self.setupUi(self)
        self.objective = objective
        self.objective_commands = []  # Commands related to this objective.
        self.show_commands = False
        self.objective_commands_all_checked = False
        self.lblObjectiveCode.setText(self.objective['code'])

        self.btnShowHideObjectiveTools.clicked.connect(self.show_hide)
        self.chkObjectiveCommands.clicked.connect(self.check_uncked_all_related_commands)

        self.widgetObjectiveTools.hide()

    def show_hide(self):
        """Show or hide all commands related to
        objective.
        """
        if self.show_commands:
            self.widgetObjectiveTools.hide()
            self.show_commands = False
            self.btnShowHideObjectiveTools.setText('Show')
        else:
            self.widgetObjectiveTools.show()
            self.show_commands = True
            self.btnShowHideObjectiveTools.setText('Hide')

    def check_uncked_all_related_commands(self):
        """Check/Uncheck all commands related to
        objective.
        """
        if self.objective_commands_all_checked:
            self.objective_commands_all_checked = False
        else:
            self.objective_commands_all_checked = True
        for command in self.objective_commands:
            command.chkSelect.setChecked(self.objective_commands_all_checked)
