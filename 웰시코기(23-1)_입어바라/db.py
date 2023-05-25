import sqlite3 as db
import os.path as path

tableList = ['post', 'user' ]
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

con = None
cur = None

'''
# txt 테이블 임포트
작성 : 2023-05-22
변경 : 2023-05-22
'''
def importData(cur, query, path):
    data = open(path, 'r', encoding = 'utf-8').readlines()
    for _ in data :
        cur.execute(query, _.split("\t"))


if __name__ == '__db__' :
    print("asdasd")


def init():
    global con, cur

    flag = path.isfile('./db/입어바라4.db')
    con = db.connect('./db/입어바라4.db')
    cur = con.cursor()
    
    # DB 데이터 유무
    if flag == False :
        cur.execute(tableCreateQuery['post'])
        importData(cur, tableImportQuery['post'], './db/post.txt')
        con.commit()
        print("Asdasd")
        


def executeQuery(query):
    return cur.execute(query).fetchall()
    '''
    raw = cur.execute(query).fetchall()
    for _ in raw :
        print(_)
    '''
