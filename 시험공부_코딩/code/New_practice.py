# phone_book = {}
# phone_book['홍길동'] = '010-1234-0001'
#
# phone_book1 = {'동길홍': '010-1029-3847'}
#
# phone_book['강감찬'] = '010-1234-0002'
# phone_book['이순신'] = '010-1234-0003'
# print(phone_book)

# phone_book1 = {'이승호': '010-1029-3847'}  # 아예 초기화가 되버리네
# print(phone_book1)

# print(phone_book.keys())
# print(phone_book.values())
# print(phone_book.items())
# print()  # 1칸 띄움
#
# print(phone_book1.keys())
# print(phone_book1.values())
# print(phone_book1.items())
# for문에서 phone_book.item()와 같은 함수를 호출하면 (키, 값) 튜플이 반환된다.

# for name, number in phone_book.items():
#      print(name, ':', number)

# 딕셔너리의 모든 항목을 하나씩 출력하려면 리스트처럼 for 루프를 사용하자.
# keys()메소드는 딕셔너리에 있는 키 항목을 시퀀스로 반환하므로, 이 값을 받아서 phone_book[key]로 접근해보자.
# 딕셔너리 안에서 항목들은 자동으로 정렬되지 않는다.
# 그래서 우리는 sorted() 함수를 사용하여서 딕셔너리의 키를 기준으로 정렬을 수행할 수 있다.
# for key in phone_book.keys():
#      print(key, ':', phone_book[key])

# print(sorted(phone_book))
# lambda 매개변수 : 표현식
# sorted_phone_book1 = sorted(phone_book.items(), key=(lambda x: x[0])) #키를 기준으로 sorted
# sorted_phone_book2 = sorted(phone_book.items(), key=lambda x: x[1]) #항목을 기준으로 sorted
# print(phone_book.items())
# print(sorted_phone_book1) #list type
# print(sorted_phone_book2) #list type
#
# print(phone_book)
#
# print(phone_book.get('강감찬'))
# print(phone_book.pop('이순신')) #키에 대한 항목 반환 후 삭제
# print(phone_book.popitem()) #요소를 넣으면 takes no arguments 라네
# print((phone_book))

# del phone_book["홍길동"] #삭제 하는 방법
# print(phone_book)

# del phone_book['이순신']
# print(phone_book)

# phone_book.clear()
# print(phone_book)

# def add(x, y):  # x,y 람다 함수 인자
#     return x + y

# add_num = add(12389648127, 10294798236472635478)
# add_num = (lambda x, y: x + y)(100, 200)  # 100, 200 람다 함수 인자
# x+y가 함수 몸체 / x, y 매개변수

# 특정한 튜플에서 첫 항목만을 추출하는 람다 함수를 정의하려면 다음과 같이 할 수 있다.
# t = (100, 200, 300)
#
# print((lambda x: x[0])(t))  # t를 인자로 받아서 그 첫 항목 t[0]을 반환한다.
# print((lambda x: x[1])(t))  # t를 인자로 받아서 그 두번쨰 항목 t[1]을 반환한다.
#
# for a in range(len(t)):
#     print((lambda x: x[a])(t))

# 도전문제 8.1
# contact = {}
# contact['성'] = '이'
# contact['이름'] = '승호'
# contact['직장'] = '순천향대학교'
# print(contact)
#
# for key, value in contact.items():
#     print(key, value)

#람다 함수
# t2 = lambda x : x*2
# key = t2 (x=5)
# print(key)

# lab_8-1
# items = {'커피음료': 7, '펜': 3, '종이컵': 2, '우유': 1, '콜라': 4, '책': 5}
# aa = input('물건의 이름을 입력하시오: ')
# print('재고 :', items[aa])
# for key in items:
#     print(key, items[key])

#도전문제 8.2
# while True:
#     num = int(input('메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료'))
#     if num == 1:
#         name = input('[재고조회] 물건의 이름을 입력하시오: ')
#         print('재고 :', items[name])
#     elif num == 2:
#         name, quantity = map(str, input('[입고] 물건의 이름과 수량을 입력하시오').split())
#         items[name] = items[name] + int(quantity)
#         print('콜라의 재고 :', items[name])
#     elif num == 3:
#         name, quantity = map(str, input('[출고] 물건의 이름과 수량을 입력하시오').split())
#         items[name] = items[name] - int(quantity)
#         print('콜라의 재고 :', items[name])
#     elif num == 4:
#         raise Exception('이부분은 아직 구현이 되지 않았습니다.')
#     else:
#         print('프로그램을 종료합니다.')
#         for key in items:
#             print(key , items[key])
#         break

# lab_8-2
# 입력을 단어 형태로 받고 s[0] 을 검사해서
# 	if q입력 받으면 종료
# 	elif >이거면 그냥 그 딕셔너리에 있는것 출력 해주고
# 		if 없으면 없다고 출력
# 	else < 면 입력을 넣어 주고
#  		입력단어 :  < one:하나 #들어오면
# 		공백을 기준으로 분리해서 입력리스트 = '<' "one:하나" (0,1)로 리스트 분리 해줌
# 		입력리스트[0] 검사해서
# 			if <면
# 				이제 입력리스트 에서 :기준으로 스플릿 해서 뉴리스트 one : 하나 넣어주고
# 				딕셔너리[뉴리스트[0]] = 뉴리스트[1]
#
# diction = {}
# print('사전 프로그램 시작... 종료는 q를 입력')
# while True:
#     list = input('$ ').split()  # 단어 형태로 입력을 받고 split함수로 리스트와 시켜줌
#     if list[0] == 'q': # 종료
#         break
#     elif list[0] == '>': # 출력
#         if list[1] in diction:
#             print(diction[list[1]])
#         else:
#             print(list[1]+'가 사전에 없습니다.')
#     elif list[0] == '<': # 입력
#         newlist = list[1].split(':')
#         diction[newlist[0]] = newlist[1]
# print('사전을 종료합니다.')

#책에 있는 코드 lab 8-2
# print('사전 프로그램 시작... 종료는 q를 입력')
# dictionary = {}
# while True:
#     st = input('$ ')
#     # print(st) #입력 받은 것
#     command = st[0] #첫 입력 문자를 추출한다.
#     # print(st[0]) #기호
#     # print(st[1]) #공백
#     if command == '<':
#         st = st[1:] #st[1]만 들어ㅏ있는 리스트를 만들어 준다.
#         # print(st) #공백포함입력 받은 것
#         inputStr = st.split(':')
#         # print(inputStr)
#         if len(inputStr) < 2 : #2개 이상일 수는 없지
#             print('입력 오류가 발생했습니다.')
#         else:
#             # print(inputStr[1].strip()) #values 값
#             dictionary[inputStr[0].strip()] = inputStr[1].strip()
#     elif command == '>':
#         st = st[1:]
#         # print(type(st))
#         inputStr = st.strip() #공백없음one:하나
#         # print(inputStr)
#         # print(type(inputStr))
#         if inputStr in dictionary:
#             print(dictionary[inputStr])
#         else:
#             print('{}가 사전에 없습니다.'.format(inputStr))
#     elif command == 'q':
#         break
#     else:
#         print('입력 오류가 발생했습니다.')
# print('사전 프로그램을 종료합니다!@!')

# 8.9 퍼일로부터 자료를 읽고 저장해보자
# f = open('hello.txt', 'w')  #파일을 만들고 내용 쓰고 저장
# f.write('안녕하세요 만나서 반갑습니다. \n줄바꿈 문장 입니다.')
# f.close()
#
# f = open('hello.txt' , 'r')  #파일을 읽어 온다.
# print(f.read())
# f.close()

asd = {'이름':'이승호', '학번':'20185108', '학년':'4', '이름':'홍길동'}
print(asd) #key는 중복되면 정보를 넣지 않는다.

# 파이썬 8장 ppt 8.9부터 하면 됨
