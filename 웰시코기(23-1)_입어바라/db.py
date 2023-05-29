import sqlite3 as db
import os.path as path

tableList = ['post', 'user' ]
tableCreateQuery = {
    'post' : '''CREATE TABLE IF NOT EXISTS Post(
	postID INTEGER PRIMARY KEY AUTOINCREMENT, 
	postName TEXT,
    postSubName TEXT, 
	postDesc TEXT, 
	postDate DATETIME,
	postEndDate DATETIME, 
	postCategory TEXT,
	postViewCount INTEGER,
	postScore INTEGER, 
	postEnabled INTEGER, 
    userID INTEGER)''',
    'user' : '''CREATE TABLE IF NOT EXISTS User(
    userID INTEGER PRIMARY KEY AUTOINCREMENT, 
	userName TEXT,
	userBirth DATETIME, 
	userSex TEXT, 
	userAddress Text)'''}
tableImportQuery = {
    'post' : '''INSERT INTO Post(postID, postName, postSubName, postDesc, postDate, postEndDate, 
	postCategory, postViewCount, postScore, postEnabled, userID) 
	VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    'user' : '''INSERT INTO User(userID, userName, userBirth, userSex, userAddress) 
	VALUES(?, ?, ?, ?, ?)'''}

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


def init():
    global con, cur

    flag = path.isfile('./db/입어바라.db')
    con = db.connect('./db/입어바라.db')
    cur = con.cursor()
    #print(tableCreateQuery['post'])
    # DB 데이터 유무
    if flag == False :
        for _ in tableList :
            cur.execute(tableCreateQuery[str(_)])
            importData(cur, tableImportQuery[str(_)], './db/' + str(_) + '.txt')
            con.commit()
        


def executeQuery(query) :
    return cur.execute(query).fetchall()
    '''
    raw = cur.execute(query).fetchall()
    for _ in raw :
        print(_)
    '''

def executeUpdate(query) :
    cur.execute(query)
    con.commit()
