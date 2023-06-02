import db
import sys
import shutil

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from tkinter import filedialog
from datetime import datetime

class postWindow(QMainWindow, uic.loadUiType("./ui/post.ui")[0]):
    
    def __init__(self):
        super(postWindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.regdate.setDate(QDate.currentDate())
        self.enddate.setDate(QDate.currentDate())
        self.uploadFileButton.clicked.connect(self.uploadFileBtn_click)
        self.homeButton.clicked.connect(self.homeBtn_click)
        self.registerButton.clicked.connect(self.registerBtn_click)

    def uploadFileBtn_click(self):
        self.filepath.setText(filedialog.askopenfilename(initialdir='./png', title='파일선택', filetypes=(('jpg files','*.jpg'),('all files','*.*'))))

    def homeBtn_click(self):
        self.close()

    def registerBtn_click(self, message):
        if len(self.title.text()) == 0 :
            QMessageBox.critical(self, '오류', '제목을 입력해주세요.')
            return
        elif len(self.subTitle.text()) == 0 :
            QMessageBox.critical(self, '오류', '부제목을 입력해주세요.')
            return
        elif len(self.filepath.text()) == 0 :
            QMessageBox.critical(self, '오류', '이미지를 첨부해주세요.')
            return
        elif len(self.desc.toPlainText()) == 0 :
            QMessageBox.critical(self, '오류', '설명을 입력해주세요.')
            return
        if self.regdate.date() > self.enddate.date() :
            QMessageBox.critical(self, '오류', '날짜를 수정해주세요.')
            return
        elif self.op_1.isChecked() == False and self.op_2.isChecked() == False and self.op_3.isChecked() == False and self.op_4.isChecked() == False :
            QMessageBox.critical(self, '오류', '카테고리를 입력해주세요.')
            return

        title = self.title.text()
        subTitle = self.subTitle.text()
        desc = self.desc.toPlainText()
        regDate = str(self.regdate.date().toString("yyyy-MM-dd"))
        endDate = str(self.enddate.date().toString("yyyy-MM-dd"))
        count = 0
        category = None
        if self.op_1.isChecked() :
            count = count + 1
            category = '상의'
        if self.op_2.isChecked() :
            count = count + 1
            category = '하의'
        if self.op_3.isChecked() :
            count = count + 1
            category = '모자'
        if self.op_4.isChecked() :
            count = count + 1
            category = '신발'
        if count > 1 :
            category = '기타'

        # db.init()
        db.executeUpdate('INSERT INTO Post(postName, postSubName, postDesc, postDate, postEndDate, postCategory, postViewCount, postScore, postEnabled, userID) VALUES(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', 0, 0, 0, 2)' %(title, subTitle, desc, regDate, endDate, category))
        shutil.copyfile(self.filepath.text(), './img/' + title + '.jpg')
        
        QMessageBox.information(self, '성공', '게시물 등록을 성공했습니다.')
        self.close()
