
def Connect():
    from pymongo import MongoClient 
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    collection = database['fruits']
    return collection



def insert():
    input_fruits = {"name" : "", "color":"", "origin" : "", "season": ""}
    input_fruits["name"] = input("과일의 이름을 입력하세요. :" )
    input_fruits["color"] = input("과일의 색깔을 입력하세요. :" )
    input_fruits["origin"] = input("과일의 원산지를 입력하세요. :")
    input_fruits["season"] = input("해당 과일의 제철인 계절을 입력하세요. :")
    return input_fruits

collection = Connect()

while True:
    insert_fruits = insert()
    collection.insert_one(insert_fruits)

