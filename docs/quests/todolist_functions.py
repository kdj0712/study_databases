def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #Mongo DB Compass를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://localhost:27017") # Mongo DB Compass의 포트에 연결하는 변수 지정
    database = mongoClient["local"] # 해당 포트에 접속해서 database(local)에 연결후 변수로 database라 선언
    return database # Connect가 호출되면 이 모든 과정을 반환할 값으로 선언

database = Connect() # Connect를 호출하여 MongoDB 내 Database까지 연결을 하고 이를 database라는 변수로 선언한다.
todos_list = database["todos_list"] # Mongo DB 내 'local 데이터베이스'에서 "todos_list" 이라는 collection에 연결
participants = database["participants"]# Mongo DB 내 'local 데이터베이스'에서 "participants" 이라는 collection에 연결
participants_todos = database["participants_todos"] # Mongo DB 내 'local 데이터베이스'에서 "participants_todos"라는 collection에 연결


def data_todos_list():  # 설문조사 기본 Base data List를 Function화 한다.
    todo_list = [
        {
            "title": "주간 보고서 작성", 
            "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."
        },
        {
            "title": "이메일 확인 및 응답", 
            "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."
        },
        {
            "title": "회의 준비", 
            "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."
        },
        {
            "title": "프로젝트 계획서 수정", 
            "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."
        },
        {
            "title": "팀 멤버와의 1:1 면담", 
            "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."
        }
    ]
    return todo_list # 준비된 설문조사 list를 function의 호출시 반환한다.

data_todo_list = data_todos_list() # 위의 list가 담긴 function을 호출하고 그것을 data_todo_list라는 변수로 지정한다.
# for x in data_todo_list: # 원활한 구문 작동을 위해 설문 조사가 진행되는 동안 
#     #반복적으로 진행하도록 하되 아래의 조건을 두어 동일한 정보가 있을 경우 Record의 저장을 하지 않도록 한다.
if todos_list.count_documents({}) == 0: # record를 확인하여 동일한 정보가 존재하는 지 확인을 하는 조건을 제시
             #(즉,문구 자체를 전체적으로 직역한다면, 저장된 data를 확인하여 동일한 정보가 없다면 아래의 조건을 실행한다.라고 볼 수 있다.)
    get_lists_id = todos_list.insert_many(data_todo_list)# data_todos_list라는 설문조사 리스트를 todos_list라는 collection에 insert 해준다. 그리고 get_lists_id라는 변수를 선언한다.
    lists_id = get_lists_id.inserted_ids

lists_id = [] #가져온 설문의 _id를 list화 하여 재사용
def get_name():
    input_name = input("설문에 참여하시는 분의 성함을 입력하세요 : ") # 설문 참가자의 이름을 입력 받고 그것을 input_name이라는 변수로 지정
    input_name = {"name" : input_name}
    get_names_id = participants.insert_one(input_name)
    inserted_participants = get_names_id.inserted_id
    return inserted_participants

inserted_participants = get_name()

def survey(todo_list): 
    todo_list = list(todos_list.find()) 
    print("다음의 To Do list 중 에서 하나를 선택하세요")
    for i in range(len(todo_list)):
        surveys_title = todo_list[i]["title"]
        print(str(i+1)+". "+ surveys_title)  
    print(" ")
    user_answer = int(input("번호를 입력하세요 :"))
    print(" ")
    if user_answer in range(len(todo_list)+1):
        print("{}".format(todo_list[user_answer - 1]['title']))
        print("{}".format(todo_list[user_answer - 1]['description']))
    print(" ")
    return todo_list[user_answer - 1]['key']

# def renew():
#     user_answer = survey()
#     while True:
#         for maped_list in range(len(lists_id)+1):
#             result = input("업무가 완료되었다면 'D'를, 진행중이라면 'G'를 입력해 주세요")
#             user_answer == maped_list
            
#             if result == "D" or result == 'd':
#                 done = "업무 완료"
#                 participants_todos.update_many({ 'id' : user_answer },{"$set" : {str(inserted_participants ): str(done)}},upsert=True)
#                 print(done)
#                 break
#             elif result == "G" or result == 'g':
#                 going = "업무 진행중"      
#                 participants_todos.update_many({ 'id' : user_answer },{"$set" : {str(inserted_participants ): str(going)}},upsert=True)
#                 print(going)
#                 break
#             else:
#                 print("잘못 입력하셨습니다. 다시 입력해 주세요.")
#         if result == "d" or result == "D" or result == "g" or result == "G":
#             break
#         print("")
#     return


def stutus_input():
    while True:
        result = input("업무가 완료되었다면 'D'를, 진행중이라면 'G'를 입력해 주세요")
        if result in ['d','D','g','G']:
            return result.lower()
        else:
            print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            
def update_database(user_answer, status, inserted_participants):
    status_str = "업무 완료" if status == 'd' else "업무 진행중"
    participants_todos.update_many({ 'id' : lists_id[user_answer - 1] },
                                   {"$set" : {str(inserted_participants): status_str}},
                                   upsert=True)
    print(status_str)
# return이 코드는 MongoDB의 `update_one` 메서드를 사용하여 특정 조건을 만족하는
#  문서를 업데이트하는 역할을 합니다. `participants_todos.update_one({str(inserted_participants) 
# : {"$exists": True} },{"$push": {str(inserted_participants ): user_answer}},upsert=True)`
# 이 코드를 분석해 보면, - `{str(inserted_participants) : {"$exists": True}}` : 이 부분은 `inserted_participants`라는 키가 존재하는 문서를 찾는 조건입니다.
#  즉, `inserted_participants`라는 이름의 필드를 가진 문서를 찾습니다.
# - `{"$push": {str(inserted_participants ): user_answer}}` : 
# 이 부분은 찾은 문서에 대해 어떤 작업을 할 것인지를 명시합니다. `$push` 연산자는 배열 필드에 새로운 요소를 추가하는 역할을 합니다.
#  이 코드에서는 `inserted_participants` 필드가 배열이라고 가정하고, 그 배열에 `user_answer` 값을 추가하려고 합니다.
# - `upsert=True` : `upsert` 옵션은 찾는 문서가 없을 경우 새로운 문서를 생성할지 여부를 결정합니다. 
# `True`로 설정하면, 조건에 맞는 문서가 없을 때 새로운 문서를 생성합니다.
# 따라서 이 코드의 전체적인 의미는 "찾은 `inserted_participants` 필드를 가진 문서에 `user_answer` 값을 추가하고,
#  해당 문서가 없다면 새로 생성하라"라는 것입니다.
    
    # upsert=True 옵션은 만약 해당 키가 존재하지 않으면 새로운 키를 만들고 그 키의 값으로 배열을 생성하라는 의미입니다.


def running(): 
    todo_list = list(todos_list.find()) 
    user_answer = survey(todo_list)
    status = stutus_input()
    update_database(user_answer, status, inserted_participants)

def run():
    while True:
        running()
        exit = ' '
        while exit != "x" and exit != "X":
            exit = input("설문을 계속 진행하시려면 'C', 설문을 종료하시려면 'Q', 프로그램을 종료하시려면 'X'를 입력해 주세요. :")
            if exit in ['c','C']:
                running()
            elif exit in ['q','Q']:
                print("=====" * 15)
                get_name()
                running()
            elif exit in ['x','X']:
                pass
            else:
                print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        if exit in ["x","X"]:
            break
    return
