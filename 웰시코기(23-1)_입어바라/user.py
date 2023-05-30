import db

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QUrl
from PyQt5 import *


class userWindow(QMainWindow, uic.loadUiType("./ui/user.ui")[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        list = db.executeQuery("SELECT * FROM USER WHERE userID = 1")[0]
        self.name.setText(list[1])
        self.birth.setDate(QDate.fromString(list[2], "yyyy-MM-dd"))
        self.sex.setText(list[3])
        self.address.setText(list[4])
