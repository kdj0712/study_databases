# Python to NoSQL DB Flow
# class 선정하여 mongo와 연결 (MongoClient = class = MongoCompass)
from pymongo import MongoClient 
# connect to port in MongoDB (Mongo DB의 포트와 접속)
mongoClient = MongoClient("mongodb://localhost:27017") #MongoClient 는 변수(클래스변수)로 담아내서 DB에서 활동할 수 있는 권한을 얻어야 한다.
# 즉, 자원에 대한 class

# Database 연결
database = mongoClient["local"]

# collection 작성(또는 작성된 collection에 연결)
collection = database['fruits']

# insert(내용 입력)
mixed_fruits =  ({"name": "체리",
                "color": ["빨강","갈색","노랑"],
                "origin": "미국",
                "season": "여름"})
result = collection.insert_one(mixed_fruits)




pass