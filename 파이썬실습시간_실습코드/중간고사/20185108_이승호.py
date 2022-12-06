# 이론 1
# input()메소드로 공백을 포함한 세 정수가 들어오면 
# split()메소드가 공백을 기점으로 세개의 문자열을 가지는 리스트를 만들어준다.
# 그러면 세개의 문자열이 들어가있는 리스트가 만들어 지는데 
# map()메소드에서 리스트 안에 있는각각의 요소들을 int형으로 변환해주고 a,b,c에 넣어준다

# 이론 2
# (1) XOR 비트연산자 이다. 같은 값이 나오면 1을 반환해 주고 다른 값이 나오면 0을 반환해준다.
# (2) 값을 나눠주는데 정수형으로 반환해준다. 예를 들어 7 //2 는 3이다.
# (3) AND비트연산자이다. 1과 1의 값일때만 1을 반환해주고 나머지 00 01 10 은 0을 반환해준다.
# (4) 비트의 자릿수를 오른쪽으로 옮겨준다. 8 >> 1 이면  4이다. //2값과 같다.
# (5) 나눠준 값의 나머지를 반환해준다. 8 % 3 이면 2이다.

# 이론 3 
# 9을 2진수로 나타내면 1001이다 여기서 1의 보수를 취해주면 0110 이다 그다음 2의 보수로 만들어 주기 위해서 
# 1을 더해준다 
# 원래수에서 2의 보수를 취해주면 음수를 표현하는 방법이다.
# 0과1만 사용하는 컴퓨터 세상에서 -를 붙혀서 음수를 표현할수 없기 떄문에 2의 보수를 취해서 음수를 표현하는 방법은 정말 획기적이다.

# 이론 4
# (1) global counter   
# (2) counter = 200
# (3) print('counter =', counter)
# (4) print_counter()
# 28줄 counter 전역변수로써 메모리에 저장되어지고 print_counter 함수 안에 있는 counter는 함수안 지역변수로써 주소를 가리키게 되어지는데
# global키워드를 씀으로써 지역변수를 참조하던 함수내 counter가 전역변수의 주소를 가리키게 된다.

# 이론 5
# [-1, -2, 3, 4, 5]
# [-1, -2, 3, 4, 5]
# first_list는 [1,2,3,4,5]리스트가 들어가있는 메모리 주소를 가르키고 있는데 그 주소를 second_list도 같이 가르키기 때문에 리스트내의 변수를 수정하면 
# 같은 리스트를 수정하는 것이기 때문에 이런 결과가 나오는 것이다.

# 실습 1
# import random
# a_list =[0,0,0,0,0]
# for i in range(len(a_list)):
#     a_list[i] = random.randint(-10,10)

# print(a_list)
# b_list = sorted(a_list)
# print(b_list)
# print(min(a_list))
# print(max(a_list))
# a= sum(a_list) / len(a_list)
# print(a)

# 실습 2
# st = input("문자열 입력: ")
# i=0
# while i <len(st):
#     for i in range(len(st)):
#         if st[i] == ['a','e','i','o','u']:
#             print(st[i].upper())
#             st[i] = 'u'
#         print(st[i])
#         i += 1

# 실습 3

# def moving_average(n_list, num):
#     sum1,sum2,sum3 = 0
#     for i in num:
#         sum = n_list[i]
#     for i in num:
#         sum = n_list[i+1]
#     for i in num:
#         sum = n_list[i+2]            
#     sum1 / len(n_list)

# alist =[1,2,3,-1,5]
# print(alist)
# print(moving_average(alist,3))


