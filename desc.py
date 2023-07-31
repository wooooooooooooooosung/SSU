from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import *
from map import *


class descWindow(QMainWindow, uic.loadUiType("./ui/desc.ui")[0]):
    def __init__(self, title, subTitle, desc, address) :
        super().__init__()
        self.setupUi(self)
        self.title.setText(title)
        self.subTitle.setText(subTitle)
        self.desc.setText(desc)
        self.homeButton.clicked.connect(self.homeBtn_click)

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

    def homeBtn_click(self):
        self.close()
