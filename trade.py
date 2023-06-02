import db
from desc import descWindow

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QUrl
from PyQt5 import *

class tradeWindow(QMainWindow, uic.loadUiType("./ui/trade.ui")[0]):
    def __init__(self, postID):
        super().__init__()
        self.setupUi(self)
        
        list = db.executeQuery("SELECT * FROM POST LEFT JOIN USER on POST.userID = USER.userID WHERE postID = '" + str(postID) + "'")[0]
        print(list)
        self.title.setText(list[1])
        self.name.setText(list[12])
        self.score.setText(str(list[8]))
        self.viewCount.setText(str(list[7]))
        self.subTitle.setText(list[1])
        self.regdate.setDate(QDate.fromString(list[4],"yyyy-MM-dd"))
        self.enddate.setDate(QDate.fromString(list[5],"yyyy-MM-dd"))
        if list[6] == '상의' : self.op1.toggle()
        elif list[6] == '하의' : self.op2.toggle()
        elif list[6] == '모자' : self.op3.toggle()
        elif list[6] == '신발' : self.op4.toggle()
        elif list[6] == '기타' : self.op5.toggle()
        self.img.setPixmap(QtGui.QPixmap("./img/" + list[1] + ".jpg").scaledToWidth(471))
        if list[9] == 0 : 
            self.enabled.setText('X')
            self.trade.setStyleSheet("background-color: rgb(255, 0, 110); border-radius: 5px; color: white;")
        else : 
            self.enabled.setText('O')
            self.trade.setStyleSheet("background-color: rgb(35, 35, 35); border-radius: 5px; color: white;")
        self.desc.clicked.connect(lambda : self.descBtn_click(list[1], list[2], list[3], list[15]))
        self.homeButton.clicked.connect(self.homeBtn_click)
        self.trade.clicked.connect(lambda : self.tradeBtn_click(list[9], postID))

    def descBtn_click(self, title, subTitle, desc, address) :
        self.desc = descWindow(title, subTitle, desc, address)
        self.desc.show()

    def homeBtn_click(self):
        self.close()

    def tradeBtn_click(self, enabled, postID) :
        if enabled == 1 :
            QMessageBox.critical(self, '오류', '이미 만료된 게시물입니다.')
            return
        else :
            db.executeUpdate("UPDATE POST SET postEnabled = 1 WHERE postID = '" + str(postID) + "'")
            QMessageBox.information(self, '성공', '대여 신청이 성공했습니다.')
            self.close()
