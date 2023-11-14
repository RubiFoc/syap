import os
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic.properties import QtWidgets

import MainWindow


if __name__ == '__main__':
     app = QApplication(sys.argv)
     window = QMainWindow()
     ui = MainWindow.Ui_MainWindow()
     ui.setupUi(window)
     window.show()
     sys.exit(app.exec())