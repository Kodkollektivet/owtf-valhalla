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
        self.is_built.setChecked(self.container.is_built)

        self.loading = QMovie('valhalla/qt/resources/loading.gif')
        self.loading.scaledSize()
        self.loadingLabel = QLabel(self)
        self.loadingLabel.setMovie(self.loading)
        self.loadingLabel.setScaledContents(True)
        self.loadingLabel.setGeometry(5,-80,380,250)
        #self.loading.start()
        #self.loading.stop()
        #self.loadingLabel.hide()
        #self.loadingLabel.show()

        self.is_running = QCheckBox('<- Running')
        self.is_running.setDisabled(True)
        self.is_running.setChecked(self.container.is_running)

        self.btn_build = QPushButton('Build')
        self.btn_start = QPushButton('Start')
        self.btn_stop = QPushButton('Stop')
        self.btn_remove = QPushButton('Remove')

        self.timer = QTimer()
        self.timer.timeout.connect(self._check_object_state)
        self.timer.start(1000)

        self.btn_build.clicked.connect(self.cmd_build)
        self.btn_start.clicked.connect(self.cmd_start)
        self.btn_stop.clicked.connect(self.cmd_stop)
        self.btn_remove.clicked.connect(self.cmd_remove)

        self.vbox.addWidget(self.loadingLabel)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.is_built)
        self.vbox.addWidget(self.is_running)
        self.vbox.addWidget(self.btn_build)
        self.vbox.addWidget(self.btn_start)
        self.vbox.addWidget(self.btn_stop)
        self.vbox.addWidget(self.btn_remove)
        self.setLayout(self.vbox)
        self._check_object_state()
        self.show()

    def _check_object_state(self):
        """Check valhalla container to update GUI."""
        self.is_built.setChecked(self.container.is_built)
        self.is_running.setChecked(self.container.is_running)

        if self.container.is_running:
            self.btn_start.setDisabled(True)
            self.btn_stop.setDisabled(False)
        else:
            self.btn_start.setDisabled(False)
            self.btn_stop.setDisabled(True)

        if self.container.is_built:
            self.btn_build.setDisabled(True)
            self.btn_remove.setDisabled(False)
        else:
            self.btn_build.setDisabled(False)
            self.btn_remove.setDisabled(True)
            self.btn_start.setDisabled(True)

    def cmd_build(self):
        """Build container."""
        self.container.build()
        self.is_built.setChecked(self.container.is_built)

    def cmd_start(self):
        """Start container."""
        self.container.start()
        self.is_running.setChecked(self.container.is_running)

    def cmd_stop(self):
        """Stop container."""
        self.container.stop()
        self.is_running.setChecked(self.container.is_running)

    def cmd_remove(self):
        """Remove container."""
        self.container.remove()
        self._check_object_state()

