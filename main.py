#!d:\PythonProjects\AbsorptionGUI\absenv\Scripts\python.exe

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Classes.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()