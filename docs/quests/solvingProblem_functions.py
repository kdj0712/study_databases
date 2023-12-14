def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://localhost:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["local"] # 해당 포트에 접속해서 database에 연결
    collection = database['solvingproblem'] # 데이터베이스에서 solvingproblem 이라는 collection에 연결
    return collection # collection이 이 모든 과정을 반환할 값으로 선언

def insert_quiz_list(): # 출제한 문제의 리스트를 펑션으로 만든다
    quiz_list = [{
            "question": "Python의 생성자 함수 이름은 무엇인가요?",
            "choices": ["__init__", "__main__", "__str__", "__del__"],
            "answer": "__init__",
            "answer_number": 1,
            "score": 20},
            {
            "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
            "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
            "answer": "print('Hello, World!')",
            "answer_number": 1,
            "score": 20},
            {
            "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
            "choices": ["//", "/* */", "#", "--"],
            "answer": "#",
            "answer_number": 3,
            "score": 20},
            {
            "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
            "choices": ["size()", "length()", "len()", "sizeof()"],
            "answer": "len()",
            "answer_number": 3,
            "score": 20},
            {
            "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
            "choices": ["str()", "int()", "char()", "float()"],
            "answer": "int()",
            "answer_number": 2,
            "score": 20}]
    return quiz_list

#모든 딕셔너리를 quiz_list라는 이름으로 반환한다.

solvingproblem = [] #solvingproblem이라는 컬렉션을 리스트로 정의한다.
collection = Connect() #위의 MongoDB와의 연결을 호출한 뒤 이것을 collection이라는 변수로 지정한다.
quiz_list = insert_quiz_list() #딕셔너리의 리스트의 function화 한 기능을 호출하고 quiz_list라는 변수로 선언한다.

for x in quiz_list:  # 위의 리스트를 x라는 변수에 넣는 것을 반복한다.
    collection.insert_one(x) #MongoDB에 연결하여 리스트에 있는 내용을 한 라인씩 입력한다.
    pass 


