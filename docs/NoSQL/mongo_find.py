# Python to NoSQL DB Flow
# class 선정하여 mongo와 연결 (MongoClient = class = MongoCompass)
from pymongo import MongoClient 
# connect to port in MongoDB (Mongo DB의 포트와 접속)
mongoClient = MongoClient("mongodb://localhost:27017") #MongoClient 는 변수(클래스변수)로 담아내서 DB에서 활동할 수 있는 권한을 얻어야 한다.
# 즉, 자원에 대한 class

# Database 연결
database = mongoClient["local"]

# collection 작성(또는 작성된 collection에 연결)
collection = database['posts']

# insert(내용 입력)
documents = collection.find({},{"_id" : 1," title":1 ,"likes" : 1})
# cast , cursor to list
list_documents = list(documents)
print("list_documents length : {}".format(len(list_documents)))
for document in documents:
    print("document : {}".format(document))
    pass
pass