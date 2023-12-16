import solvingProblem_functions copy # SolvingProblem_functions copy라는 파이썬 파일(모듈)을 호출한다.

collection = solvingProblem_functions copy.Connect() #호출한 파읠의 Connect라는 function을 호출하여 collection이라는 변수로 지정한다.

def run(): # 출제된 문제를 출력하고 실행할 function을 생성한다.
    quiz_list = list(collection.find()) # collection에 있는 모든 문서를 가져와 list로 만들고, 그것을 quiz_list라고 지정한다.
    user_name = input("이름을 입력해 주세요: ") # 새로운 키 값으로 지정하기 좋은 문제를 푸는 사람을 user_name이라고 이름지어주고, 이름을 입력받는다.
    final_score = 0 # 정답이 맞은 점수를 합산하기 위한 변수'final_score'선언하고 초기값으로 0을 지정한다.
    for i in range(len(quiz_list)): # 퀴즈 리스트에 있는 값의 개수만큼 반복하도록 for 구문을 작성한다.
        quiz = quiz_list[i] #quiz_list의 인덱스 값을 quiz라는 변수로 지정한다.
        print(str(i+1) + ". " + quiz["question"], end=" ")
        # 리스트에 저장된 값은 0부터 이므로 +1을 더해준 뒤 해당 문제를 출력해 주고. 다음에 배점을 연결해서 출력할 수 있게 end를 이어서 선언한다.
        print(str(quiz["score"])+"점") # 해당 배점을 출력한다.
        # print(str(quiz[score][i])+"점") # 해당 위치의 배점을 옆에 출력해준다.
        # 배점이 다를 경우를 고려하여 인덱스화 한 뒤 출력을 시도해 봤지만, 계속 에러가 발생,
        # 해당 에러 구문 내용은 "quiz 딕셔너리의 "score" 키에 대응하는 값이 리스트가 아니라 단일 정수라면 오류를 발생시킵니다."라고 함
        for j in range(len(quiz["choices"])):#문제 보기를 출제하기 위하여 반복문을 사용
            choice = quiz["choices"][j] #퀴즈 리스트에 있는 보기의 리스트를 인덱스화 하여 choice라는 변수로 선언
            print(str(j+1)+". "+choice)  # 0번값부터 저장되어 있을 문제의 번호값을 +1을 한 뒤, 해당 보기들을 옆에 같이 출력한다.
        user_answer =int(input("답을 입력해 주세요(번호로 입력): ")) 
        # 사용자가 해당 문제의 답을 입력하면 그것을 숫자형 정수로 저장하고 그것을 user_answer라는 변수로 선언한다.
        if user_answer == quiz["answer_number"]: #사용자가 입력한 답이 "answer_number"에 저장되어 있는 값과 같은지 확인한다.
            final_score += quiz["score"] # 정답과 일치할 경우 최초에 0으로 지정된 점수로부터 배점된 점수를 가산 시킨다.
        collection.update_one({'_id': quiz['_id']}, {"$set": {user_name: user_answer}}) 
        # collection에 동일한 이름의 키값이 있는지 확인한 다음 없을 경우 사용자의 이름을 키값으로 입력하고, 받은 정답을 value에 입력한다.
    print(user_name + "님의 점수는 " + str(final_score) + "점 입니다.")
    # 사용자의 이름과 계산한 점수를 이용하여 결과를 출력한다.
    return # 이 과정을 반환한다.

run() 
# 위 과정을 실행하는 function을 호출하여 동작시킨다.