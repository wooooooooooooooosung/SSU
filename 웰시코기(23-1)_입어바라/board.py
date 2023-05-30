import db

from trade import tradeWindow

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QUrl
from PyQt5 import *

class boardWindow(QMainWindow, uic.loadUiType("./ui/board.ui")[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        list = db.executeQuery("SELECT postID, postName FROM Post")
        #print(len(list), list)

        self.print_posts(list)

    def print_posts(self, list):
        for idx, row in enumerate(list):
            #print(idx, row[0], row[1])

            image_path = './img/' + row[1] + '.jpg'
            pixmap = QtGui.QPixmap(image_path).scaled(150,150)
            label = QLabel(self)
            label.setPixmap(pixmap)
            label.setGeometry(150*idx, 150*idx, 150, 150)
            label.mousePressEvent = lambda event, image_id=row[0]: self.imgBtn_click(image_id)
            self.show()

    def imgBtn_click(self, postID) :
        self.trade = tradeWindow(postID)
        self.trade.show()
