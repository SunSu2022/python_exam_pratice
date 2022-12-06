f = open(r"C:\Users\PSENG\Desktop\이승호\3학년 2학기\파이썬 프로그래밍\기말고사_자료\파이썬실습시간_실습코드\11_14\학생정보.csv", "r",
         encoding="utf-8")  # 한국말을 쓸라면 이걸 쓰자
text = f.readlines()

# in 으로 딕셔너리 문 안에서 찾을 수 있다.

student = {}
# print(text) #list type
for line in text:  #리스트에서 0 1 2 4 string 으로 하나씩 읽어온다.
    new_line = line.split(',')
    id = new_line[0]
    name = new_line[1].strip()  #좌우공백 없애 주지만 왼쪽에만 공백이 있어서 왼쪽 공백이 사라짐
    grade = new_line[2].replace('\n','').strip() #\n 줄바꿈 문자를 ''으로 바꾸어 준다.

    info = {}  #정보라는 딕셔너리를 만들어 준다.
    info["이름"] = name
    info["성적"] = grade

    student[id] = info #학번 : info 이중 딕셔너리 만들어줌 예){'2012': {'이름': '손흥민', '성적': 'A'}}
#학번(key) 입력 받아줌
check_stu = (input("정보를 확인하려는 학생의 학번을 입력하세요 : "))

#key check and print 
if check_stu in student.keys():
    print(check_stu, '학번의 이름은', student[check_stu]['이름'],"성적은",student[check_stu]['성적'])
else:
    print(check_stu,'학번은 없습니다.')

