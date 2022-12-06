# 넘파이는 Python의 수치해석용 패키지
# 백테와 행렬 선형대수 계산 특화
# 연산속도가 매우 빠름 근데 수치해석은 쉽고 편리 하게 가능
# 왜 넘파이 연산이 빠른 이유 시험문제 나올 수도
# <<첫번째 이유: 자료구조
# 넘파이 배욜은 C언어 배열로 구현되어 있다.
# 파이썬 리스트는 이중포인터로 구현되어있다.
# 이를 통해 어떤 자료형이든 list 추가 할 수있지만
# 포인터의 주소를 통해 간접적으로 값에 접근해야하고 병렬적인 처리가 불가능해 연산이 느리다는 단점이 있다. 
# <<두번째 이유: 벡터화
# 넘파이 배열은 벡터화 연산 지원 현대적cpu가 지원하는 벡터 연산 기능을 활용
# 리스트는 순차적으로 계산 
# 하지만 넘파이배열은 cpu가 지원하는 한모든 연산을 한번에 수행
# 넘파이배열은 100개의 항목이나 10000개의 항목에서 더하기 연산을 하든 거의 시간이 비슷하다
# 차원은 축이라고 한다. 성능이 우수한 ndarray 객체를 제공

np_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
np_array.reshape(4,4)
np_array = np_array.reshape(4,4)
np_array[::2]

np_array[::2][::2]
np_array[::2,::2]
#위에 리스트 스타일 슬라이싱은 먼저 앞에[::2]가 실행되고 나온 어레이문에 다가 [::2]를 또 실행하기 때문에 간격이 1행에 두칸 띄면 없기 때문에 1행만 실행 되는 것이다.

import numpy as np
import matplotlib.pyplot as plt

mid_scores = np.array([10,20,30])
# print(mid_scores)
# print((type(mid_scores)))

mid_scores = np.array([10,20,30])
final_scores = np.array([60, 70, 80])
total_scores = mid_scores+final_scores

# 넘파이의 '+'연산자는 2개의 넘파이 배열에서 대응되는 원소들끼리의 합을 구해 같은 크기의 배열에 담는다

print(total_scores)
print(total_scores/2)

# print(type(final_scores))

a = np.array([1,2,3]) #넘파이 ㅂ열의 속성
a.shape #객체의 형태
a.ndim #몇차원인지
a.dtype #객체 내부 자료형 <<넘파이 배열은 C언어 배열과 동일하기 때문에 자료형을 하나로 정해야합니다.ㄴ>>
a.itemsize #객체 내부 자료향 차지하는 메모리 크기(byte)
a.size #객체의 전체 크기(항목의 수)
a.data #배열의 실제 원소를 포함하고 있는 버퍼
a.strides #배열 각 차원별 다음 요소로 점프하는데 필요한 거리를 바이트로 표시한 값을 모은 튜플

# 10.5
import numpy as np
salary = np.array([220, 250, 230])
salary = salary+100
salary
salary = salary *2.1 #곱셉 정수 및 실수도 가능합니다
salary

# 넘파이를 이용해 BMI계산 해보자
import numpy as np
height = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73]) #대상 자들 키리스트로 넘파이 배열
weight = np.array([86, 74, 59, 95, 80, 68])

Bmi = weight / height**2 
print(Bmi)

# 10.6 인덱싱과 슬라이싱 in Numpy
scores = np.array([88,72,93,94,89,78,99])
for i in range(len(scores)):
    i
    scores[i]
    print()
scores[-4:-1] #마이너스 인덱싱 할때도 그냥 일반적인 정수 인덱싱과 같이 생각 하면 된다 그냥 순서 늘여놓고 그 전까지 가는거 생각 하면 된다.
scores[1:4]
scores[4:-1] #음수 인덱싱도 가능 그냥 딱 늘여놓고 생각하면 된다.
scores[3:] #생략하면 끝까지 나타난다. 

# 10.7 논리적인 인덱싱을 통해 값을 추려내자 어떤 조건 배열 원하는 값 추려내기
ages = np.array([18,19,25,30,28])
y = ages > 20 #부울형 넘파이 배열을 원래 가지고 있는 것들에 넣어서 값 추려낼 수 있다.
print(ages[y])

y=[[1,2,3], [4,5,6,], [7,8,9]]
np_array = np.array(y) #넘파이 2차원 배열
np_array

# 2차원 배열 인덱싱 [행][열] 2차원 넘파이 배열은 !행렬이다! 바로 특정 항목에 접근하게 된다.
# 넘파이 배열은 모든 항목이 동일한 자료형을 가진다는 것을 명심!! 
# 만약 정수형 넘파이 배열인데 실수를 넣으면 소수점 사라지고 삽입됨

np_array[0][2]
np_array[0,2]
np_array

np_array[0,0] = 255.153 #
print(np_array)
np_array.dtype

np_array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
np_array[0:2, 2:4]
np_array[0:, 0:]
np_array[:, 1::2]
np_array[1::2, 1::2]
np_array

# 10.11 2차원 배열에서 논리적인 인덱싱을 해 보자
np_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
compa = np_array>5
compa
print(np_array[compa])  

# 넘파이 2차원 배열 비교연산자 2차원 논리 배열이 반환 된다 이것을 이용 특정 값을 뽑아 낼 수 있다.

five  = np_array[:, 2]
five[five>5]
np_array[:, 2][np_array[:, 2]>5]
np_array[:,2]>5

dd = np_array[:] %2 == 0 #짝수만
np_array[:] %2 == 1 #홀수만
dd
np_array[np_array[:] % 2 == 0]  #필터링 작업

# 10.12 arrang()함수 ragne()함수 비교
np.arange(0, 5, 1) #만들때 리스트 형태로 만들지 말고 그냥 괄호 안에 숫자 쓰자 start, stop-1, step
list(range(5))

# range()써서 arange() 같은 넘파이 배열 만들고 싶으면...
np.array(range(5))
np.arange(0,5)

# 10.13 linspace() 와 logspace() 함수

np.linspace(0, 10) #시작값부터 끝값까지 균일한 간격으로 지정 개수 배열 생성 stop도 숫자를 생성 기본값 50개
np.logspace(0, 2, 10).reshape(10, 1) #로그 스케일로 수 생성 stop도 숫자를 생성 기본값 50개 10^n승의 수까지 범위
# 10.14 배열의 형태를 바꾸는 reshape() 함수와 flatten( ) 함수
# reshape(튜플형태) 로 넘겨주는 게 원칙이지만 (x,y) 로 넘겨주면 자동으로 ((x,y)) 으로 인지하게 된다.
y = np.arange(12) 
y.reshape(3,4)
y.reshape(6,-1) #인수로 -1 전달 자동으로 배열형태 결정
y.reshape(-1,6) #인수로 -1 전달 자동으로 배열형태 결정
y.flatten()
y 

# 10.15 난수를 생성해보자
# 의사난수 : 컴퓨터가 규칙을 가지고 생성 한 수 특정한 입력값은 시드(seed)

np.random.seed(100)
np.random.rand(5)
rand = np.random.rand(5,3)
rand.reshape(-1,3)
np.random.randint(1,7, size=10)

# 10.17 정규분포난수생성
# 앞에 난수를 균일 확률 분포 표준편차(분산)이 크면 데이터의 흩어짐이 크다 발생 확류리 평평하게 펴진 상태에 접근

np.random.randn(5)
np.random.randn(5,4)

mu=10 #평균
sigma=2 #표준편차
randoms = mu+sigma*np.random.randn(5,4)
randoms

# 10.18 평균과 중앙값 계산

mu = 175 #평균
sigma = 10 #표준편차
heights = mu+sigma*np.random.randn(10000)
np.mean(heights) #평균 계산
np.median(heights) #중앙값 계산 : 리스트의 중앙에 있는 항목

a = np.array([1,2,3,4,6])
np.mean(a) #평균 실수값이 나오네용
np.median(a) #리스트의 값중 오름차순으로 늘여놓았을때 가운데에 있는 값

# 10.18 데이터 분석 체험하기: 상관관계 분석
# corrcoef() 요소들의 상관관계를 게산
# np.corrcoef()

import numpy as np

f=open('제주도_건강통계-3.csv', 'r')
text = f.readlines()
# print(*text) #*붙히면 보기 편하게 나오네

lines=[]
for t in text[1:]:
    line = t.strip() #\n문자 제거
    line = line.split(',')

    lines.append(line)

print(lines)

for i in lines:
    i

# 이름 연도 비만율 스트레스 호소율 고혈압 진단률을 서로 다른 리스트에 저장 한다.

name=[]
year=[]
obesity=[]
stress=[]
hbp=[]

for l in lines:
    name.append(l[0])
    year.append(int(l[1]))
    obesity.append(float(l[2]))
    stress.append(float(l[3]))
    hbp.append(float(l[4]))
# 넘파이 어레이로 바꾸고 np.mean() 을 통해 평균 비만율 평균 고혈압 진단률 계산 가능하다.!!

obesity = np.array(obesity)
hbp = np.array(hbp)
np.mean(obesity) #비만
np.mean(hbp) #고혈압

result = np.corrcoef(obesity, hbp)
result #비만율과 고혈압 진단률로  0.33정도의 양의 상관관계가 있을음 보인다.


result = np.corrcoef(obesity, stress)
result #비만율과 스트레스 호소율 음의 상관관계

# but 상관관계가 있다고 해서 인과성이 있는건 아니다
