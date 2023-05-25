import db


'''
# 프로그램 시작점
Date : 2023-05-25
'''
if __name__ == '__main__' :
    db.init()
    print( db.executeQuery("SELECT * FROM POST")[0][0] )


        
