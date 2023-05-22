import sqlite3 as db
import os.path as path

table = ['post', 'user' ]
tableCreateQuery = {
    'post' : '''CREATE TABLE IF NOT EXISTS post(
	postID INTEGER PRIMARY KEY AUTOINCREMENT, 
	postName TEXT,
	postDesc TEXT, 
	postDate DATETIME,
	postCategory TEXT,
	postStyle TEXT,
	rentalDate DATETIME,
	rentalPlace TEXT, 
	postViewCount INTEGER,
	postScore REAL, 
	userID INTEGER)''' }
tableImportQuery = {
    'post' : '''INSERT INTO post(postID, postName, postDesc, postDate, postCategory, 
	postStyle, rentalDate, rentalPlace, postViewCount, postScore, userID) 
	VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''}

'''
# 테이블 임포트
작성 : 2023-05-22
변경 : 2023-05-22
'''
def importData(cur, query, path):
    data = open(path, 'r', encoding = 'utf-8').readlines()
    for _ in data :
        cur.execute(query, _.split("\t"))
        


'''
# 프로그램 시작점
작성 : 2023-05-22
변경 : 2023-05-22
'''
if __name__ == '__main__' :
    # importData('post', './database/post.txt')
    
    # 해당 디렉토리에 db 파일이 없으면 생성
    # if path.isfile('./database/입어바라3.db') == False:
    if False == False:
        con = db.connect('./db/입어바라.db')

        cur = con.cursor()
        cur.execute(tableCreateQuery['post'])    
        print("[SUCCESS] CREATE TABLE")

        importData(cur, tableImportQuery['post'], './db/post.txt')
        con.commit()
        print("[SUCCESS] IMPORT DATA")
        
        cur.execute("SELECT * FROM post")
        raw = cur.fetchall()
        for _ in raw :
            print(_)






        
