import random
from 기본 import basic
#length의 갯수만큼 mix이상 max이하가 들어가는 리스트를 만들어주는 함수 basic
def find_zero(array):
    for i in range(len(array)):
        if array[i] == 0:
            return True

if __name__ == "__main__":

    mix,max,length = map(int, input('세 숫자를 입력하세요 ').split())
    print(mix,max,length)
    #print(mix)
    array = basic(length)
    print(array)
    


    '''
     #length의 갯수만큼 0이 들어가는 리스트를 만들어주는 함수
    while True:
        

        if find_zero(array) == True:
            break
    '''
    
    
