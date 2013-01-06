import MySQLdb

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWD = ""
DB_NAME = "test"
DB_CHARSET = "utf8"
DB_TABLE = "user"

"""
mysql column 'bit' in python is str object : 0 is '\x00', 1 is '\x01'
use ord() turn to 0 or 1
"""

def getConnection():
    try:
        conn = MySQLdb.connect(host = DB_HOST, 
                               user = DB_USER, 
                               passwd = DB_PASSWD, 
                               db = DB_NAME,
                               charset = DB_CHARSET)
        return conn
    except Exception, e:
        print "datebase connection unsuccessful : ", e
        return None
    
def insert():
    connection = getConnection()
    session = connection.cursor()
    sql = "insert into " + DB_TABLE + "(name, age) values('lyc', 22)"
    affectRow = session.execute(sql)
    print affectRow
    
def insertByTransaction():
    connection = getConnection()
    try:
        connection.begin()
        session = connection.cursor()
        sql = "insert into " + DB_TABLE + "(name, age) values('lyc', 22)"
        affectRow = session.execute(sql)
        connection.commit()
        connection.close()
        print affectRow
    except Exception, e:
        connection.rollback()
        print e

def select():
    session = getConnection().cursor()
    sql = "select * from " + DB_TABLE
    session.execute(sql)
    data = session.fetchall()
    for record in data:
        print record

def selectByMap():
    session = getConnection().cursor(cursorclass = MySQLdb.cursors.DictCursor)
    sql = "select * from " + DB_TABLE
    session.execute(sql)
    data = session.fetchall()
    for record in data:
        print record

insertByTransaction()
#select()
#selectByMap()
