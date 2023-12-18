def Connect(): 
    from pymongo import MongoClient 
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    return database 

database = Connect() 
todos_list = database["todos_list"] 
participants = database["participants"]
participants_todos = database["participants_todos"] 


def data_todos_list():  
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
    return todo_list 

data_todo_list = data_todos_list() 
if todos_list.count_documents({}) == 0:             
    get_lists_id = todos_list.insert_many(data_todo_list)
    lists_id = get_lists_id.inserted_ids

lists_id = [] 
def get_name():
    input_name = input("설문에 참여하시는 분의 성함을 입력하세요 : ") 
    input_name = {"name" : input_name}
    get_names_id = participants.insert_one(input_name)
    inserted_participants = get_names_id.inserted_id
    return inserted_participants


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
    return todo_list[user_answer - 1]['_id']

def stutus_input():
    while True:
        result = input("업무가 완료되었다면 'D'를, 진행중이라면 'G'를 입력해 주세요")
        if result in ['d','D','g','G']:
            return result.lower()
        else:
            print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            
def update_database(user_answer, status,inserted_participants):
    status_str = "업무 완료" if status == 'd' else "업무 진행중"
    participants_todos.update_one({ '_id' : user_answer },
                                   {"$set" : {str(inserted_participants): status_str}}, upsert=True)
    print(status_str)

def run():
    while True: 
        todo_list = list(todos_list.find()) 
        inserted_participants = get_name()
        user_answer = survey(todo_list)
        status = stutus_input()
        update_database(user_answer, status,inserted_participants)
        exit = ' '
        while exit != "x" and exit != "X":
            exit = input("설문을 계속 진행하시려면 'C', 설문을 종료하시려면 'Q', 프로그램을 종료하시려면 'X'를 입력해 주세요. :")
            if exit in ['c','C']:
                todo_list = list(todos_list.find()) 
                user_answer = survey(todo_list)
                status = stutus_input()
                update_database(user_answer, status,inserted_participants)
            elif exit in ['q','Q']:
                print("=====" * 15)
                inserted_participants = get_name()
                todo_list = list(todos_list.find()) 
                user_answer = survey(todo_list)
                status = stutus_input()
                update_database(user_answer, status,inserted_participants)
            elif exit in ['x','X']:
                pass
            else:
                print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        if exit in ["x","X"]:
            break
    return
