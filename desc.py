import requests

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import *


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

def getLatLng(address):
    result = ""

    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = '758707f6a274ebc390627c283aa67caa'
    header = {'Authorization': 'KakaoAK ' + rest_api_key}

    r = requests.get(url, headers=header)

    if r.status_code == 200:
        result_address = r.json()["documents"][0]["address"]
        
        result = result_address["y"], result_address["x"]
    else:
        result = "ERROR[" + str(r.status_code) + "]"
    return result
def getKakaoMapHtml(address_latlng):
    javascript_key = "24c90bc08df574c851cbff398327ac87"

    result = ""
    result = result + "<div id='map' style='width:475px;height:245px;display:inline-block;'></div>" + "\n"
    result = result + "<script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=" + javascript_key + "'></script>" + "\n"
    result = result + "<script>" + "\n"
    result = result + "    var container = document.getElementById('map'); " + "\n"
    result = result + "    var options = {" + "\n"
    result = result + "           center: new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ")," + "\n"
    result = result + "           level: 3" + "\n"
    result = result + "    }; " + "\n"
    result = result + "    var map = new kakao.maps.Map(container, options); " + "\n"
    
    # 검색한 좌표의 마커 생성을 위해 추가
    result = result + "    var markerPosition  = new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ");  " + "\n"
    result = result + "    var marker = new kakao.maps.Marker({position: markerPosition}); " + "\n"
    result = result + "    marker.setMap(map); " + "\n"

    result = result + "</script>" + "\n"
    
    return result