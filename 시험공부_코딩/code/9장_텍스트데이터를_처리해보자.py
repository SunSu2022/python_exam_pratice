# 9.2 문자열에서 개별 문자를 뽑아보자.
s = 'Monty Python'
print(s)
print(type(s))
print(s[0])
print(s[-1])
print(s[:-1])
print(s[:11])
s[4:-1]

# print()

# print(s[6:10])
# print(s[-12:-7]) #- 니까 -12 -11- -10 -9 -8 까지 같다.

# t1 = s[-2:]
# t2 = s[:-2]

# t3 = s[:2]
# t4 = s[2:]

# print(s[:-2] + s[-2:] ) #원래 문장이 나온다.

# print(t1)
# print(t2)
# print(t3)
# print(t4)

# s = '   Hello World!   '
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# s = 'Hello, World!'
# print(s.split())
# print(s.split(','))

# p = list('Hello, World')
# print(p)

# s = 'Welcome to, Python, and , bla, bla  '
# list = [x.strip() for x in s.split(',')] #반점을 기준으로 split해주고 strip()사용해서 공백을 없애준다.
# print(list)

# p = ','.join(['apple', 'grape', 'banana']) #하나의 요소만 필요 하다.
# print(p)

# p = '-'.join('010.9794.9101'.split('.')) 
# print(p)

# p = '010.9794.9101'.replace('.','-')
# print(p)

s='#####this is an example##'
print(s.strip('#')) #문자열 앞 뒤에 있는 해시문자를 제거한다.

s='#####this is an example##'
print(s.lstrip('#')) #문자열 left에 있는 해시문자를 제거한다.

s='#####this is an example##'
print(s.rstrip('#')) #문자열 right에 있는 해시문자를 제거한다.

p = s.strip('#').capitalize() #샾문자를 제거하고 문장의 첫 글자를 대문자로 만든다
print(p)

s = 'Hello World'
s = s.lower()
s
s.upper()
s[0].upper()
s = s.capitalize()

s = 'iww.booksr.co.kr'
s.find('ok') #문자열에서 지정된 부분 문자열 찾아서 그 인덱스를 반환한다.
s.find('x') #문자열이 없으면 -1을 반환한다.
print(s.capitalize()) #.제거하면서 첫글자 대문자로 만들어 보기

# pdf 8-2 예제
f=open(r'C:\Users\PSENG\Desktop\삼성전자 자소서.txt' , 'r', encoding='UTF8')
text = f.read()
text = text.replace('삼성전자', '세동전자')
print(text)

f=open(r'C:\Users\PSENG\Desktop\세동전자 자소서.txt' , 'w', encoding='UTF8')
f.write(text)
f.close()

# lab_9-4
import random

n_digits = int(input('몇 자리의 비밀번호를 원하십니까? '))

otp = []
for i in range(n_digits):
    otp += str(random.randrange(0,10))
otp