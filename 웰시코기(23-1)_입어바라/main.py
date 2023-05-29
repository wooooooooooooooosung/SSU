import db
from user import userWindow
from post import postWindow
from trade import tradeWindow

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5 import *

selectHotPost = 4
postID1 = 0
postID2 = 0
postID3 = 0

class WindowClass(QMainWindow, uic.loadUiType("./ui/main.ui")[0]):

    
    def __init__(self):
        super().__init__()
        global postID1, postID2, postID3

        self.setupUi(self)
        self.hotPostImage.setPixmap(QtGui.QPixmap('./img/ex' + str(selectHotPost) + '.jpg').scaledToWidth(500))
        self.leftButton.clicked.connect(lambda : self.arrowBtn_click(0))
        self.rightButton.clicked.connect(lambda : self.arrowBtn_click(1))

        self.writePostButton.clicked.connect(self.writePostBtn_click)
        self.userButton.clicked.connect(self.userBtn_click)

        self.op1.clicked.connect(lambda : self.optionBtn_click('상의'))
        self.op2.clicked.connect(lambda : self.optionBtn_click('하의'))
        self.op3.clicked.connect(lambda : self.optionBtn_click('모자'))
        self.op4.clicked.connect(lambda : self.optionBtn_click('신발'))
        self.op5.clicked.connect(lambda : self.optionBtn_click('기타'))
        
        list = db.executeQuery("SELECT * FROM POST WHERE postCategory = '상의' ORDER BY postViewCount DESC LIMIT 3")
        self.img1.setIcon(QtGui.QIcon('./img/' + list[0][1] + '.jpg'))
        self.img2.setIcon(QtGui.QIcon('./img/' + list[1][1] + '.jpg'))
        self.img3.setIcon(QtGui.QIcon('./img/' + list[2][1] + '.jpg'))
        postID1 = list[0][0]
        postID2 = list[1][0]
        postID3 = list[2][0]

        self.img1.clicked.connect(lambda : self.imgBtn_click(1))
        self.img2.clicked.connect(lambda : self.imgBtn_click(2))
        self.img3.clicked.connect(lambda : self.imgBtn_click(3))

        #self.webEngineView = QWebEngineView()
        #self.gridLayout.addWidget(self.webEngineView)  # row, column, row_span, column_span
        #self.webEngineView.load(QUrl("https://naver.me/FOvSy6I3"))

    def imgBtn_click(self, n) :
        global postID1, postID2, postID3
        postID = None
        if n == 1 : postID = postID1
        elif n == 2 : postID = postID2
        elif n == 3 : postID = postID3
        self.trade = tradeWindow(postID)
        self.trade.show()


    def arrowBtn_click(self, arrow):
        global selectHotPost
        if arrow == 0 :
            if selectHotPost == 1 : selectHotPost = 3
            else : selectHotPost = selectHotPost - 1
        elif arrow == 1 :
            if selectHotPost == 3 : selectHotPost = 1
            else : selectHotPost = selectHotPost + 1
        self.hotPostImage.setPixmap(QtGui.QPixmap('./img/ex' + str(selectHotPost) + '.jpg'))

    def writePostBtn_click(self):
        self.post = postWindow()
        self.post.show()
    
    def userBtn_click(self) :
        self.user = userWindow()
        self.user.show()

    def optionBtn_click(self, option) :
        global postID1, postID2, postID3
        list = db.executeQuery("SELECT * FROM POST WHERE postCategory = \'" + option + "\' ORDER BY postViewCount DESC LIMIT 3")
        self.img1.setIcon(QtGui.QIcon('./img/' + list[0][1] + '.jpg'))
        self.img2.setIcon(QtGui.QIcon('./img/' + list[1][1] + '.jpg'))
        self.img3.setIcon(QtGui.QIcon('./img/' + list[2][1] + '.jpg'))
        postID1 = list[0][0]
        postID2 = list[1][0]
        postID3 = list[2][0]
    

'''
# 프로그램 시작점
작성 : 2023-05-22
변경 : 2023-05-22
'''
if __name__ == '__main__' :

    db.init()

    # print( db.executeQuery("SELECT * FROM POST") )

    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
        
