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
# mixed_fruits =  ({"name": "체리",
#                 "color": ["빨강","갈색","노랑"],
#                 "origin": "미국",
#                 "season": "여름"})
# result = collection.insert_one(mixed_fruits)
# pass


# 분리 입력 (fruit, fruits_colors)
# insert fruits (내용 입력)
dict_fruits =  ({"name": "체리",
                "origin": "미국",
                "season": "여름"})
result = collection.insert_one(dict_fruits)
print("result.inserted_id : {}".format(result.inserted_id))
inserted_id = result.inserted_id #서로 영역이 다르기 때문에 이름이 유사해도 개별적으로 동작한다.



# insert fruits_colors 작업 진행
# insertedId: ObjectId("657bf126e52c79ca7df148a7")
fruits_colors = [{"color" : "빨강"},
                 { "color" : "갈색"},
                 { "color" : "노랑"}]
list_fruits_colors = list()

# documents = collection.find({},{"_id" : 1," title":1 ,"likes" : 1})
# db.fruits_colors.insertMany([{"color" : "빨강"}, {"color" : "갈색"}, {"color" : "노랑"}]);


for dict_color in fruits_colors:
    dict_color["fruits_id"] = inserted_id
    list_fruits_colors.append(dict_color)
    pass


# collection fruits_colors
collection_fruits_colors = database["fruits_colors"]
collection_fruits_colors.insert_many(list_fruits_colors)

# find from fruits_colors
documents = collection_fruits_colors.find({"fruits_id" : { "$eq" : inserted_id} })


pass




# # ToDo 리스트 생성
# todo_list = [
#     {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
#     {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
#     {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
#     {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."},
#     {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."},
# ]






