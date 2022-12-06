import random
#length의 갯수만큼 mix이상 max이하가 들어가는 리스트를 만들어주는 함수
def basic(length):
    array=[0 for i in range(length)]
    for i in range(length):
        array[i] = random.randint(mix, max)
    return array

if __name__ == "__main__":
    mix,max,length = map(int, input('세 숫자를 입력하세요 ').split())
    array = basic(length)
    print(array)