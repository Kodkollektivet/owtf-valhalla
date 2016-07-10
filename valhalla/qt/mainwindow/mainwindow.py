from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .uimainwindow import Ui_MainWindow

from valhalla.qt.execute import ExecuteWidget
from valhalla.qt.manage import ManageContainersWidget
from valhalla.qt.results.resultswidget import ResultsWidget
from valhalla.qt.communicate import COMMUNICATE
from valhalla.qt.wrappers.qtowtfcontainer import get_owtf_c


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Communicate
        self.com = COMMUNICATE
        self.com.statusbar_message[str].connect(self.update_statusbar)

        # Execute
        self.executewidget = ExecuteWidget(self)
        self.tabExecuteCerticalLayout.addWidget(self.executewidget)

        # Manage containers
        status, containers = get_owtf_c()
        if status:
            for container in containers:
                m = ManageContainersWidget(container, parent=self)
                self.tabManageVerticalLayout.addWidget(m)

        self.resultswidget = ResultsWidget(parent=self)
        self.tabResultsVerticalLayout.addWidget(self.resultswidget)

    def update_statusbar(self, message):
        self.statusBar().showMessage(message, msecs=999999)

