import pymysql
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mydb = client.EPL
collection = db.match_results
findall = collection.find()

db = pymysql.connect(host='localhost', port=3306, user='root', \
    passwd='tiger', db='yojulabdb', charset='utf8', autocommit=True)

cursor = db.cursor(pymysql.cursors.DictCursor)
print(cursor.execute("select * from economic"))

