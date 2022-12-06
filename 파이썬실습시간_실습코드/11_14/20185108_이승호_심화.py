f=open("학생정보.csv","r",encoding="utf-8") #한국말을 쓸라면 이걸 쓰자
text = f.readlines()

# in 으로 딕셔너리 문 안에서 찾을 수 있다.

student = {}
for line in text:
    new_line = line.split(',')
    # print(new_line)
    id = new_line[0]
    name = new_line[1].strip()
    grade = new_line[2].replace('\n','').strip()
    
    info = {}
    info["이름"] = name
    info["성적"] = grade

    student[id] = info

#학번(key) 입력 받아줌
check_stu = (input("정보를 확인하려는 학생의 학번을 입력하세요 : "))

#key check and print 
if check_stu in student.keys():
    print(check_stu, '학번의 이름은', student[check_stu]['이름'],"성적은",student[check_stu]['성적'])
else:
    print(check_stu,'학번은 없습니다.')

