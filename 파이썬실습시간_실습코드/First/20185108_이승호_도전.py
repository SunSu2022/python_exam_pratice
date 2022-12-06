num1 = int(input("첫 번째 숫자 입력: "))
num2 = (input("두 번째 숫자 입력: "))
num2_3 = int(num2[0:1]) #5
num1_3 = num1 * num2_3 #출력 (3)

num2_4 = int(num2[1:2])
num1_4 = num1 * num2_4

num2_5 = int(num2[2:3])
num1_5 = num1 * num2_5

print(num1_5)
print(num1_4)
print(num1_3)
print(num1*int(num2))