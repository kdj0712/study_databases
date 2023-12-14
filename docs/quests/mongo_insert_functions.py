
def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://localhost:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["local"] # 해당 포트에 접속해서 database에 연결
    collection = database['fruits'] # 데이터베이스에서 fruits 라는 collection에 연결
    return collection # collection이 이 모든 과정을 반환할 값으로 선언



def insert(): # 입력을 받는 전체 과정을 통합한 function의 이름으로 insert라는 이름을 지정한다
    input_fruits = {"name" : "", "color":"", "origin" : "", "season": ""} 
# fruits collection의 key값과 빈 밸류값을 미리 부여하고 하단의 입력받을 내용을 연동시키는 역할을 할 딕셔너리의 이름을 input_fruits라고 부여한다.
    input_fruits["name"] = input("과일의 이름을 입력하세요. :" )
# "name" key에 입력받을 값의 위치를 배정하고 입력을 받는다.
    input_fruits["color"] = input("과일의 색깔을 입력하세요. :" )
# "color" key에 입력받을 값의 위치를 배정하고 입력을 받는다.
    input_fruits["origin"] = input("과일의 원산지를 입력하세요. :")
# "origin"(원산지) key에 입력받을 값의 위치를 배정하고 입력을 받는다.
    input_fruits["season"] = input("해당 과일의 제철인 계절을 입력하세요. :")
# "season"(제철) key에 입력받을 값의 위치를 배정하고 입력을 받는다.
    return input_fruits
# 전체적으로 입력받은 딕셔너리의 값을 반환한다.

collection = Connect() 
# MongoDB에 연결하기 위해 function을 호출해서(Connect()) collection객체를 받아올 'collection'리턴값을 매칭해준다.

while True: #아래의 행동을 반복하는 ㄴ구문을 만든다
    insert_fruits = insert() #입력받는 function인 insert()를 실행하여, 그 리턴값인 insert_fruits를 받는다.
    collection.insert_one(insert_fruits) #리턴받은 insert_fruits를 collection에 입력한다.

