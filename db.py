import sqlite3 as db
import os.path as path

'''
테이블 리스트
type list
'''
tableList = [ 'post', 'user' ]

'''
테이블 생성 쿼리
type dictionary
'''
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

'''
테이블 데이터 임포트 쿼리
type dictionary
'''
tableImportQuery = {
    'post' : '''INSERT INTO Post(postID, postName, postSubName, postDesc, postDate, postEndDate, 
	postCategory, postViewCount, postScore, postEnabled, userID) 
	VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    'user' : '''INSERT INTO User(userID, userName, userBirth, userSex, userAddress) 
	VALUES(?, ?, ?, ?, ?)'''}

con = None
cur = None



'''
# 테이블 임포트
내용 : csv 포맷의 데이터를 읽어서 해당 테이블에 넣음
작성 : 2023-05-22
변경 : 2023-05-22
'''
def importData(cur, query, path):
    data = open(path, 'r', encoding = 'utf-8').readlines()
    for _ in data :
        cur.execute(query, _.split("\t"))

	
	
'''
# db 초기 설정
내용 : sqlite 파일 연동(db 파일 없을 경우 생성)
작성 : 2023-05-22
변경 : 2023-05-22
'''
def init():
    global con, cur

    flag = path.isfile('./db/입어바라.db')
    con = db.connect('./db/입어바라.db')
    cur = con.cursor()
    
    # DB 존재 유무
    if flag == False :
        for _ in tableList :
            cur.execute(tableCreateQuery[str(_)])
            importData(cur, tableImportQuery[str(_)], './db/' + str(_) + '.txt')
            con.commit()
        
	
	
'''
# 쿼리문 실행
파라미터 : query sqlite3 query
내용 : return 값이 있는 쿼리
작성 : 2023-05-22
변경 : 2023-05-22
'''
def executeQuery(query) :
    return cur.execute(query).fetchall()
	
	
	
'''
# 쿼리문 실행
파라미터 : query sqlite3 query
내용 : return 값이 없는 쿼리
작성 : 2023-05-22
변경 : 2023-05-22
'''
def executeUpdate(query) :
    cur.execute(query)
    con.commit()
