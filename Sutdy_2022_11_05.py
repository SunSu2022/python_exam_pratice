# #터틀 그래픽
# import turtle
# t= turtle.Turtle()
# t.speed(1000000^5)
# for count in range(600):
    # t.circle(100)
    # t.left(360/1800)

# ######################################
# #N-각형 그리기
# ######################################
# import turtle
# t= turtle.Turtle()
# t.shape('circle')
# t.speed(10)
# def tturle():
#     s = turtle.textinput("", "몇각형을 원하시나요?:")
#     n = int(s)

#     for count in range(n):
#         t.forward(100)
        # t.left(360/n)

# if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
#     for i in range(10):
#         tturle()


# #####################################
# 랜덤하게 그리기
# #####################################
# import turtle
# t= turtle.Turtle()
# t.shape('circle')
# t.speed(6)

# s = turtle.textinput("", "몇각형을 원하시나요?:")
# n = int(s)

# for count in range(n):
#     t.forward(100)
#     t.left(360/n)

# ######################################
# # 랜덤하게그림 count의 수가 가 떨어지면 반복문종료 하고 프로그램 종료
# ######################################
# import turtle
# import random
# t = turtle.Turtle()
# t.shape('turtle')
# count=0

# while True:
#     length = random.randint(1,100)
#     t.forward(length)
#     angle = random.randint(-180 , 180)
#     t.right(angle)
#     count += 1
#     if count == 10:
#         break
# turtle.exitonclick()


# ######################################
# n=int(input("정수를 입력하시오: "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(n,"!은",fact, "이다. " )

# under_ = True
# while under_:
#     reponse = input("공사가 완료 되었습니까?")
#     if reponse == '예':
#         under_ = False
# print('루프를 탈출했습니다.')
# dan = int(input("원하는 단은: "))
# i=1

# while i <= 9:
#     print('%s*%s=%s' %(dan, i, dan*i))
#     i=i+1
# import turtle
# t=turtle.Turtle()
# t.shape('turtle')
# t.speed()
# i=0
# while i<5:
#     t.forward(150)
#     t.right(144)
#     i += 1
# import turtle

# t=turtle.Turtle()

# t.speed(0)
# t.width(3)

# length = 3
# while length<500:
#     t.forward(length)
#     t.right(89)
#     length += 5
# import random

# tries=0
# guess=0

# answer=random.randint(1,100)
# print('1부터 100 사이의 숫자를 맞추시오')
# # print(answer)
# while guess != answer:
#     guess = int(input('숫자를 입력하시오: '))
#     tries += 1
#     if guess < answer:
#         print('낮음')
#     elif guess > answer:
#         print('높음!')

# print('축하합니다. 총 시도횟수 =' ,tries)

# breads = ["호밀빵", "위트", "화이트" ]
# meats = ["미트볼", "소시지", "닭가슴살"]
# vegis = ["양상추", "토마토", "오이"]
# sauces = ["마요네즈", "허니 머스타드", "칠리"]

# print('달수네 샌드위치 가게의 가능한 조합')
# for b in breads:
#     for m in meats:
#         for v in vegis:
#             for s in sauces:
#                 print(b+" + "+m+" + "+v+" + "+s)

# import random
# while True:
#     x = random.randint(1,10)
#     y = random.randint(1,10)
#     print(x,'-',y,'=',end = '')
#     answer = int(input('정답은?:'))
#     corret = x-y
#     if answer == corret:
#         print('Good job!')
#     elif answer == corret-1 or answer == corret+1:
#         print('almost right!')
#     elif answer == 123456789:
#         break
# print('종료합니다.')
# def calc(n1, n2):
#     return n1 + n2, n1 - n2, n1 * n2, n1 / n2  # 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 반환

# n1, n2 = 200, 100
# t1, t2, t3, t4 = calc(n1, n2)  # 네 개의 값을 반환받기 위해 4개의 변수를 사용함
# print(n1, '+', n2, '=', t1)
# print(n1, '-', n2, '=', t2)
# print(n1, '*', n2, '=', t3)
# print(n1, '/', n2, '=', t4)

def get_sum(start, end):
    s=0
    for i in range(start, end+1):
        s += i
    return s
print(get_sum(1,1123540))

import turtle
t = turtle.Turtle()
t.shape('turtle')
t.speed(100)

def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360//n) #정수 나눗셈은 //으로 한다.

for i in range(10):
    t.left(20)
    n_polygon(8, 30)