from pprint import pprint as pp
import copy

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from valhalla.dockerutils import commands as objectives
from valhalla.qt.wrappers.qtowtfcontainer import get_owtf_c
from .uiresultswidget import Ui_Form
from valhalla.qt.execute.objectivewidget.objectivewidget import ObjectiveWidget
from valhalla.qt.execute.commandwidget.commandwidget import CommandWidget


class ResultsWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        if parent is None:
            raise Exception('Please provide parent')
        else:
            super().__init__(parent=parent)
            self._parent = self.parent()

        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_results)
        self.timer.start(2000)
        self.counter = 0

    def update_results(self):
        #print('Updateing results.')
        self.plainTextEdit.clear()
        status, ocs = get_owtf_c()
        #counter_buffer = len([res.get_results() for res in [c for c in ocs]])
        #print(counter_buffer)
        if status:
            for oc in ocs:
                #pp(oc)
                for res in oc.get_results():
                    for key, value in res.items():
                        self.plainTextEdit.appendPlainText(str(key) + ':' + str(value))

                    self.plainTextEdit.appendPlainText('\n')

