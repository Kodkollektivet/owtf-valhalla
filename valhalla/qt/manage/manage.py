from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from valhalla.qt.wrappers.qtowtfcontainer import QtOwtfContainer


class ManageContainersWidget(QWidget):
    """Manage containers.

    Build/Start/Stop.
    """
    def __init__(self, container: QtOwtfContainer, parent=None):
        if parent is None:
            raise Exception('Please provide parent')
        else:
            super().__init__(parent=parent)

        self.container = container
        self.setMinimumHeight(5)

        self.vbox = QVBoxLayout()
        self.label = QLabel(self.container.image)

        self.is_built = QCheckBox('<- Built')
        self.is_built.setDisabled(True)
        self.is_built.setChecked(self.container.is_container_built)

        self.loading = QMovie('valhalla/qt/resources/loading.gif')
        self.loading.scaledSize()
        self.loadingLabel = QLabel(self)
        self.loadingLabel.setMovie(self.loading)
        self.loadingLabel.setScaledContents(True)
        self.loadingLabel.setGeometry(5,-80,380,250)
        #self.loading.start()

        self.is_running = QCheckBox('<- Running')
        self.is_running.setDisabled(True)
        self.is_running.setChecked(self.container.is_running)

        self.btn_build = QPushButton('Build')
        self.btn_start = QPushButton('Start')
        self.btn_stop = QPushButton('Stop')

        self.btn_build.clicked.connect(self.cmd_build)
        self.btn_start.clicked.connect(self.cmd_start)
        self.btn_stop.clicked.connect(self.cmd_stop)

        self.vbox.addWidget(self.loadingLabel)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.is_built)
        self.vbox.addWidget(self.is_running)
        self.vbox.addWidget(self.btn_build)
        self.vbox.addWidget(self.btn_start)
        self.vbox.addWidget(self.btn_stop)
        self.setLayout(self.vbox)
        self._check_object_state()
        self.show()

    def _check_object_state(self):
        """Check valhalla container to update GUI."""
        start = self.container.is_running
        if start:
            self.btn_start.setDisabled(True)
        else:
            self.btn_start.setDisabled(False)

    def cmd_build(self):
        self.container.build()
        self.is_built.setChecked(self.container.is_container_built)
        self._check_object_state()

    def cmd_start(self):
        self.container.start()
        self.is_running.setChecked(self.container.is_running)
        self._check_object_state()

    def cmd_stop(self):
        self.loading.stop()
        self.loadingLabel.hide()
        self.container.stop()
        self.is_running.setChecked(self.container.is_running)
        self._check_object_state()