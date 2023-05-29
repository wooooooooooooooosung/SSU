import db

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5 import *


class userWindow(QMainWindow, uic.loadUiType("./ui/user.ui")[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.webEngineView = QWebEngineView()
        self.gridLayout.addWidget(self.webEngineView)
        self.webEngineView.load(QUrl("https://naver.me/FOvSy6I3"))

        info = db.executeQuery("SELECT * FROM USER WHERE userID = 1")[0]
        self.name.setText(info[1])
        self.sex.setText(info[2])
        self.address.setText(info[4])