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

### insert many 작업진행
# 과일 정보를 담은 리스트 생성
list_fruits = [
    {"name": "사과", "color": "빨강", "origin": "대한민국", "season": "가을"},
    {"name": "바나나", "color": "노랑", "origin": "필리핀", "season": "계절 무관"},
    {"name": "포도", "color": "보라", "origin": "대한민국", "season": "가을"},
    {"name": "수박", "color": "초록", "origin": "대한민국", "season": "여름"},
    {"name": "자두", "color": "보라", "origin": "대한민국", "season": "여름"},
    {"name": "키위", "color": "초록", "origin": "뉴질랜드", "season": "겨울"},
    {"name": "딸기", "color": "빨강", "origin": "대한민국", "season": "봄"},
    {"name": "블루베리", "color": "파랑", "origin": "미국", "season": "여름"},
    {"name": "체리", "color": "빨강", "origin": "미국", "season": "여름"},
    {"name": "오렌지", "color": "주황", "origin": "미국", "season": "겨울"},
]
insert_result = collection.insert_many(list_fruits)

list_inserted_ids = insert_result.inserted_ids # 입력된 내용의 ObjectId를 반환받는 명령어를 inserted_ids라는 변수에 담아낸다.
# 입력된 데이터들의 ObjectId가 list형태로 제공받게 되고, index로 접근하는 것이 가능하다.
# insert_result.inserted_ids[0]
# ObjectId('657a788f5a9411e54b68bf3a')

collection.delete_many({"_id":list_inserted_ids[0]})


# delete inserted records by _ids
pass