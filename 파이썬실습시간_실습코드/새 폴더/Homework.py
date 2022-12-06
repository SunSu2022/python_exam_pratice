''' 엑셀 데이터 추가하는 구문 ,기준으로
f = open("덮어쓸_학생정보.csv", "a", encoding="utf-8")  # 글 추가할 수 있는 코드 이렇게 추가 해서 하면 될 것 같음
data = "\n2018, 이승호, B"
f.write(data)
f.close()
'''

f = open("123.csv", "r", encoding="utf-8")  # 한국말을 쓸라면 이걸 쓰자
text = f.readlines()  ###이줄이 텍스트 읽는 줄
f.close()

# in 으로 딕셔너리 문 안에서 찾을 수 있다.

student = {}  # 딕셔너리 선언
New_student = {}  # 수정받아서 채울 딕셔너리
for line in text:
    new_line = line.split(',')
    id = new_line[0]
    name = new_line[1].strip()
    grade = new_line[2].replace('\n', '').strip()

    info = {}
    info["이름"] = name
    info["성적"] = grade

    student[id] = info

# 학번(key) 입력 받아줌
# check_stu = (input("정보를 확인하려는 학생의 학번을 입력하세요 : "))

# key check and print
# if check_stu in student.keys():
#     print(check_stu, '학번의 이름은', student[check_stu]['이름'], "성적은", student[check_stu]['성적'])
# else:
#     print(check_stu, '학번은 없습니다.')
######################################  반복문  ################################################
# 학번 수정항목 수정내용
# stu_num change_thing change_form

# dict_keys(['2012', '2013', '2014', '2015'])

print(student)
print(student.items())
print(student.keys()) # 현재 키가 어떤 것이 뭐머가 있는지
print(student.values())

# 2022_11_18 AM 4:58 수정 2누르고 변수에 값 넣는 것 까지 완료

def new_in_dict(newstu_num, new_name, new_score=False):
    f = open("덮어쓸_학생정보.csv", "a", encoding="utf-8")  # 글 추가할 수 있는 코드 이렇게 추가 해서 하면 될 것 같음
    data = '\n' + newstu_num + ', ' + new_name + ', ' + new_score
    f.write(data)
    print(newstu_num, '학번으로', new_name + ',', new_score, '가 저장되었습니다.')
    return data


while (True):
    num = int(input('조회(1) 수정(2) 추가(3) 종료(4) : '))
    if num == 1:  # 조회
        stu_num = (input("학번을 입력하세요:"))
        if stu_num in student.keys():
            print(stu_num, '학번의 이름은', student[stu_num]['이름'], "성적은", student[stu_num]['성적'])
    elif num == 2:  # 수정
        stu_num, change_form, change_thing = map(str, input('학번, 수정항목, 수정내용을 입력하세요:').split())
        print(stu_num, change_form, change_thing)
        # 이름 성적 으로 비교 하는 것 말고 딕셔너리문안에서 비교해서 찾는 거 짜보자
        if change_form == '이름':
            student[stu_num]['이름'] = change_thing
            print(stu_num, '학번의 이름이', student[stu_num]['이름'] + '로 바뀌었습니다.')
            print(stu_num, '학번의 이름은', student[stu_num]['이름'] + ',', "성적은", student[stu_num]['성적'], '입니다.')
        elif change_form == '성적':
            student[stu_num]['성적'] = change_thing
            print(stu_num, '학번의 성적이', student[stu_num]['성적'] + '로 바뀌었습니다.')
            print(stu_num, '학번의 이름은', student[stu_num]['이름'] + ',', "성적은", student[stu_num]['성적'], '입니다.')
        else:
            print('"' + change_form + '"', '항목은 존재하지 않습니다!')
    elif num == 3:  # 추가
        newstu_num, new_name, new_score = map(str, input('추가할 학번, 이름, 성적을 입력하세요: ').split())
        print(newstu_num, new_name, new_score)
        if newstu_num in student.keys():
            print(newstu_num + '학번은 이미 존재합니다.')
        else:
            New_student = new_in_dict(newstu_num, new_name, new_score)
            student[newstu_num] = {}
    elif num == 4:  # 종료
        print('저장됐습니다.')
        break

phonebook = {"홍길동": "010-9794-9101"}
# print(phonebook)
phonebook["2016"] = {"이름": "이준호", "성적": "B"}
a = '2012'
b = '이름'
c = '이승호'
d=  '성적'
e= 'A'

phonebook[a] = {b:c, d:e}
print(phonebook['2012'].keys())
print(phonebook)
print(phonebook.items())
print(phonebook.keys())
print(phonebook.values())



