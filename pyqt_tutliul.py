import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.test = QCheckBox("test", self)
        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle("QCheckBox")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

