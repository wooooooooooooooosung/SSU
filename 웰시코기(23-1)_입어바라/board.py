import db

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QUrl
from PyQt5 import *

class boardWindow(QMainWindow, uic.loadUiType("./ui/board.ui")[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
