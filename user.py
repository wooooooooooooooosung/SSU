import db

from trade import tradeWindow
from board import boardWindow
from map import *

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QUrl
from PyQt5 import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

img1 = 1
img2 = 1
img3 = 1

class userWindow(QMainWindow, uic.loadUiType("./ui/user.ui")[0]):

    def __init__(self):
        global img1, img2, img3

        super().__init__()
        self.setupUi(self)

        list = db.executeQuery("SELECT * FROM USER WHERE userID = 1")[0]
        
        self.name.setText(list[1])
        self.birth.setDate(QDate.fromString(list[2], "yyyy-MM-dd"))
        self.sex.setText(list[3])
        self.address.setText(list[4])
        address = list[4]
        self.homeButton.clicked.connect(self.homeBtn_click)
        self.reset.clicked.connect(self.resetBtn_click)
        self.myButton.clicked.connect(self.myBtn_click)
        
        self.img1.clicked.connect(lambda : self.imgBtn_click(img1))
        self.img2.clicked.connect(lambda : self.imgBtn_click(img2))
        self.img3.clicked.connect(lambda : self.imgBtn_click(img3))

        

        list = db.executeQuery("SELECT * FROM Post WHERE postCategory = '상의' AND postEnabled = 0 ORDER BY RANDOM() LIMIT 1")[0]
        self.img1.setIcon(QtGui.QIcon('./img/' + list[1] + '.jpg'))
        img1 = list[0]

        list = db.executeQuery("SELECT * FROM Post WHERE postCategory = '하의' AND postEnabled = 0 ORDER BY RANDOM() LIMIT 1")[0]
        self.img2.setIcon(QtGui.QIcon('./img/' + list[1] + '.jpg'))
        img2 = list[0]

        list = db.executeQuery("SELECT * FROM Post WHERE postCategory = '신발' AND postEnabled = 0 ORDER BY RANDOM() LIMIT 1")[0]
        self.img3.setIcon(QtGui.QIcon('./img/' + list[1] + '.jpg'))
        img3 = list[0]

        self.webEngineView = QWebEngineView()
        self.layout.addWidget(self.webEngineView)
        
        # 카카오 REST API로 좌표 구하기
        address_latlng = getLatLng(address)
    
        # 좌표로 지도 첨부 HTML 생성
        if str(address_latlng).find("ERROR") < 0:
            map_html = getKakaoMapHtml(address_latlng)
            
            html_file = open('./map.html', 'w')
            html_file.write(map_html)  
        else:
            print("[ERROR]getLatLng")

        self.webEngineView.load(QUrl("http://localhost:7335/map.html"))
    

    def imgBtn_click(self, postID):
        self.trade = tradeWindow(postID)
        self.trade.show()

    def myBtn_click(self):
        self.user = boardWindow("SELECT postID, postName FROM Post WHERE postEnabled = 1")
        self.user.show()
    
    def resetBtn_click(self):
        global img1, img2, img3
        list = db.executeQuery("SELECT * FROM Post WHERE postCategory = '상의' AND postEnabled = 0 ORDER BY RANDOM() LIMIT 1")[0]
        self.img1.setIcon(QtGui.QIcon('./img/' + list[1] + '.jpg'))
        img1 = list[0]

        list = db.executeQuery("SELECT * FROM Post WHERE postCategory = '하의' AND postEnabled = 0 ORDER BY RANDOM() LIMIT 1")[0]
        self.img2.setIcon(QtGui.QIcon('./img/' + list[1] + '.jpg'))
        img2 = list[0]

        list = db.executeQuery("SELECT * FROM Post WHERE postCategory = '신발' AND postEnabled = 0 ORDER BY RANDOM() LIMIT 1")[0]
        self.img3.setIcon(QtGui.QIcon('./img/' + list[1] + '.jpg'))
        img3 = list[0]

    def homeBtn_click(self):
        self.close()
