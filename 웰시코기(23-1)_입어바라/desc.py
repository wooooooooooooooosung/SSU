from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5 import *


class descWindow(QMainWindow, uic.loadUiType("./ui/desc.ui")[0]):
    def __init__(self, title, subTitle, desc) :
        super().__init__()
        self.setupUi(self)
        self.title.setText(title)
        self.subTitle.setText(subTitle)
        self.desc.setText(desc)
        self.homeButton.clicked.connect(self.homeBtn_click)

    def homeBtn_click(self):
        self.close()