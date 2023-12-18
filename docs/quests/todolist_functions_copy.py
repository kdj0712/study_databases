def Connect(): 
    from pymongo import MongoClient 
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    return database 

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
#반복적으로 진행하도록 하되 아래의 조건을 두어 동일한 정보가 있을 경우 Record의 저장을 하지 않도록 한다.
if todos_list.count_documents({}) == 0:# record를 확인하여 동일한 정보가 존재하는 지 확인을 하는 조건을 제시 
#(즉,문구 자체를 전체적으로 직역한다면, 저장된 data를 확인하여 동일한 정보가 없다면 아래의 조건을 실행한다.라고 볼 수 있다.)
    get_lists_id = todos_list.insert_many(data_todo_list)# data_todos_list라는 설문조사 리스트를 todos_list라는 collection에 insert 해준다. 그리고 get_lists_id라는 변수를 선언한다.
    lists_id = get_lists_id.inserted_ids #insert 한 get_lists_id의 '_id'를 가져온 값의 이름을 lists_id라고 선언한다.

lists_id = [] # 가져온 lists_id 를 리스트화 한다.
def get_name(): # 참가자의 이름을 입력받는 Function을 get_name()이라고 선언한다.
    input_name = input("설문에 참여하시는 분의 성함을 입력하세요 : ") # 입력받는 이름을 input_name이라는 변수로 선언
    input_name = {"name" : input_name}
# 입력 받은 이름을 삽입하기 위해, 딕셔너리의 조건 중 key값은 name이라고 선언하고 밸류로 입력받은 이름을 지정한 뒤 다시 input_name이라고 변수로 지정한다.
    get_names_id = participants.insert_one(input_name) #이것을 participants라는 collection에 넣어주고 이것을 get_names_id라는 변수로 선언한다.
    inserted_participants = get_names_id.inserted_id
    # get_names_id가 콜렉션인 participants에 저장되면 생성되는 _id를 가져오도록 하고 이것을 inserted_participants라는 변수로 선언한다.
    return inserted_participants #function이 반환되는 값으로 inserted_participants를 선언한다.

# 설문에 대해 진행한 내용을 구간별로 나눠 function화 구성
def survey(todo_list):  # 설문을 입력한 내용인 todo_list를 인용하는 설문 진행 function을 survey라고 선언한다.
    todo_list = list(todos_list.find())  # collection에 입력된 todo_list를 가져와서 리스트화 한 다음 이것을 todo_list라는 변수로 선언한다.
    print("다음의 To Do list 중 에서 하나를 선택하세요") # 설문 안내를 출력한다.
    for i in range(len(todo_list)): # 설문의 항목 별 내용을 출력하기 위한 반복문을 생성한다.
        surveys_title = todo_list[i]["title"] # 리스트화 한 설문 내용의 index 번호 별 내용을 surveys_title이라는 변수로 선언한다.
        print(str(i+1)+". "+ surveys_title)  #각 설문 내용을 앞에 번호를 붙여서 출력한다.
    print(" ") #빈 줄
    user_answer = int(input("번호를 입력하세요 :")) # 설문에 응답할 번호를 입력받는다.
    print(" ") # 빈줄 
    if user_answer in range(len(todo_list)+1): # 설문의 응답한 내용과 그 설명을 출력하기 위한 구문을 생성한다.
        print("{}".format(todo_list[user_answer - 1]['title'])) 
        print("{}".format(todo_list[user_answer - 1]['description']))
    print(" ")
    return todo_list[user_answer - 1]['_id'] # 응답한 내용과 일치하는 ['_id'] 반환한다.

def stutus_input(): #응답한 설문의 상태를 입력받는다.
    while True:
        result = input("업무가 완료되었다면 'D'를, 진행중이라면 'G'를 입력해 주세요")
        if result in ['d','D','g','G']: #입력받은 값이 해당되는 항목과 일치하는 지 확인한다.
            return result.lower() # 대문자로 입력되었을 경우 소문자로 변환하여 해당 내용을 인용할 수 있도록 반환한다.
        else: # 위의 내용과 일치하지 않을 경우 아래의 내용을 출력한다.
            print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            
def update_database(user_answer, status, inserted_participants):
     # 데이터베이스에 입력받은 값과 지정한 값을 입력할 function을 update_database라고 선언한다.
    status_str = "업무 완료" if status == 'd' else "업무 진행중"
    # 위의 입력받은 내용이 'd'라면 "업무 완료", 아닌 경우 "업무 진행중"이 출력되도록 한 다음,
    # 해당 내용들을 재인용 할 수 있도록 변수로 선언한다.
    participants_todos.update_one({ '_id' : user_answer }, # participants_todos컬렉션에 내용들을 업데이트 하기 위해 user_answer의 "_id"와 일치하는 여부를 먼저 확인한다.
                                   {"$set" : {str(inserted_participants): status_str}}, upsert=True)
    # key에는 이름을 입력했을 때 가져온 inserted_participants를 이용하고, 설문에 응답한 사람이 status에 입력한 값을 value로 선언한다.
    # 일치할 경우 해당 내용에 연장하여 쓸 수 있도록,없을 경우 새로운 field에 저장될 수 있도록 upsert라는 복합된 키워드를 적용한다.
    print(status_str) # 컨디션의 내용을 출력한다.

def run(): #종합적으로 실행을 할 function으로 run을 지정한다.
    while True:  
        todo_list = list(todos_list.find()) #위의 내용과 동일하다.
        inserted_participants = get_name()  #get_name()을 호출한 뒤 inserted_participants라고 변수로 지정한다.
        user_answer = survey(todo_list) #설문을 시작하는 survey를 설문의 내용과 같이 호출한 뒤 입력받을 내용을 user_answer라고 변수를 선언한다.
        status = stutus_input() # 사용자의 업무가 진행중 또는 완료 여부를 묻는 status_input function을 호출한 뒤 status라는 변수로 선언한다.
        update_database(user_answer,status,inserted_participants) #update_database function을 호출하면서, 위의 변수들을 같이 불러 값을 반영한다.
        exit = ' ' # exit라는 항목에 대한 빈 값을 우선 선언하여 초기화한다.
        while exit != "x" and exit != "X": # 만약 입력받은 exit에 대한 내용이 x나 X가 아닐 경우 아래의 내용을 진행한다.
            exit = input("설문을 계속 진행하시려면 'C', 설문을 종료하시려면 'Q', 프로그램을 종료하시려면 'X'를 입력해 주세요. :")
            if exit in ['c','C']: #입력받은 값이 c나 C일 경우 아래의 행동을 한다.
                todo_list = list(todos_list.find()) 
                user_answer = survey(todo_list)
                status = stutus_input()
                update_database(user_answer,status,inserted_participants)
            elif exit in ['q','Q']: # 입력받은 값이 q나 Q일 경우 아래의 행동을 한다.
                print("=====" * 15) # 앞전 사용자와의 구분을 위해 ===을 출력해준다.
                inserted_participants = get_name()  # 새로운 사용자의 이름을 입력받는다.
                todo_list = list(todos_list.find()) 
                user_answer = survey(todo_list)
                status = stutus_input()
                update_database(user_answer,status,inserted_participants)
            else: # 그 외의 내용을 입력받았을 경우 아래의 내용을 출력한다.
                print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        if exit in ["x","X"]: # 만약 입력받은 값이 x나 X일 경우 구문을 빠져 나가 프로그램을 종료한다.
            break
    return
