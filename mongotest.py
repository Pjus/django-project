from pymongo import MongoClient 
import datetime 

client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.EPL
collection = db.match_results
findall = collection.find()

for i in findall:
    print(i)