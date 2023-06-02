import db
from trade import tradeWindow
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPixmap

class boardWindow(QMainWindow, uic.loadUiType("./ui/board.ui")[0]):
    def __init__(self, query):
        super().__init__()
        self.setupUi(self)

        list_data = db.executeQuery(query)
        self.print_posts(list_data)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setGeometry(10, 50, 480, 460)

        self.homeButton.clicked.connect(self.homeBtn_click)

        self.show()

    def print_posts(self, list_data):
        image_size = 220
        images_per_row = 2

        scroll_content = QWidget(self.scrollArea)
        scroll_layout = QGridLayout(scroll_content)
        scroll_layout.setHorizontalSpacing(10)
        scroll_layout.setVerticalSpacing(5)

        row = 0
        column = 0

        for idx, row_data in enumerate(list_data):
            image_path = './img/' + row_data[1] + '.jpg'
            pixmap = QPixmap(image_path).scaled(image_size, image_size)

            image_label = QLabel(scroll_content)
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)

            text_label = QLabel(row_data[1], scroll_content)
            text_label.setAlignment(Qt.AlignCenter)
            text_label.setStyleSheet("color: white;")

            scroll_layout.addWidget(image_label, row, column)
            scroll_layout.addWidget(text_label, row + 1, column)

            image_label.mousePressEvent = lambda event, image_id=row_data[0]: self.imgBtn_click(image_id)

            column += 1
            if column >= images_per_row:
                row += 2 
                column = 0

        scroll_layout.setRowStretch(row, 1)  

        self.scrollArea.setWidget(scroll_content)

    def imgBtn_click(self, postID):
        self.trade = tradeWindow(postID)
        self.trade.show()

    def homeBtn_click(self):
        self.close()
