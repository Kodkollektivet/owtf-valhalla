
from PyQt5.QtCore import QObject, pyqtSignal


class Communicate(QObject):
    """This object provides signals."""
    statusbar_message = pyqtSignal(str)

    def __init__(self):
        super(Communicate, self).__init__()


COMMUNICATE = Communicate()