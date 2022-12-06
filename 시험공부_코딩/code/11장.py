# 11.1 데이터 시작화
# 사람들은 시각적으로 보이는 데이터를 직관적으로 이해할 수 있기 때문이다.

# 11.3 matplotlib 무작정 사용해 보기
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt  # 별칭
import numpy as np

# 우리나라의 연간 1인당 국민 소득
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

# 선 그래프  선의 색, 마크의 표시방법, 선의 두께 등을 키워드 인자로 줄 수 있다.
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# title
plt.title("GDP per capita")
plt.ylabel('dollars')
# plt.savefig('gdp_per_capita', dpi=600) # png 이미지로 저장 가능 dpi는 dot per inch로 1인치(약 2.54cm)당 점의 수를 의미함
plt.show() #plt.show()함수를 사용해야 차트가 화면에 출력된다.

# lab 11-1 수학함수 그리기

x = [x for x in range(-10, 10)]  # 목록에 넣는다.
y = [2*t for t in x]
plt.plot(x, y, marker='o')  # 선그래프에 동그라미 표식

plt.axis([-20, 20,-20, 20 ])
plt.show()

x = [x for x in range(20)]

'''
x = list(range(-10,10))
x = np.array(x)

y = [x*2]

x = list[x]
y = list[y]

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
'''
# 11.5 차트 장식 도와주는 다양한 기법
x = [x for x in range(-10, 10)]  # 목록에 넣는다.
b = list(range(-10, 10))
# x 랑 b랑 같은 의미
y1 = [2*t for t in x]
y2 = [t**2+5 for t in x]
y3 = [-t**2-5 for t in x]
plt.plot(x, y1, 'r--', x, y2, 'g^-', x, y3, 'b*:')
plt.axis([-30, 30, -30, 30])
# plt.show()

# • ‘r--’나 ‘g^-’, ‘b*:’와 같은 포맷 지정명령을 통해 선의 색깔, 표식의 종류, 선
# 의 형태를 지정할 수도 있다.
# • r은 빨강, g는 녹색, b는 파랑을 의미
# 한다.
# • --는 점선, -는 실선, :는 짧은 점선을
# 의미한다.
# • 표식 기호 ^는 세모, *는 별표 표식을
# 각각 의미

# 11.6 하나의 차트에 여러 개의 데이터를 그려보자
x = [x for x in range(20)]
y = [x**2 for x in range(20)]
z = [x**3 for x in range(20)]

plt.plot(x, x, label='linear')  # 각 선에 대한 레이블 
plt.plot(1,5, label = 'sdf')
plt.plot(x, y, label='quadratic')
plt.plot(x, z, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("My Plot")

plt.legend()  # 차트를 설명하는 범례
plt.show()

# lab 11-2 삼각함수의 기본인 사인 그래프 그리기
x = []
y = []
z = []
# math.radians(x)
# 각도 x를 도(degree)에서 라디안으로 변환합니다.

for angle in range(360):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))
    z.append(math.cos(math.radians(angle)))
plt.plot(x, y, label='sin')
plt.plot(x, z, 'r--')
plt.title("SINE WAVE")
plt.legend()
plt.show()

# • ‘r--’나 ‘g^-’, ‘b*:’와 같은 포맷 지정명령을 통해 선의 색깔, 표식의 종류, 선
# 의 형태를 지정할 수도 있다.
# • r은 빨강, g는 녹색, b는 파랑을 의미
# 한다.
# • --는 점선, -는 실선, :는 짧은 점선을
# 의미한다.
# • 표식 기호 ^는 세모, *는 별표 표식을
# 각각 의미

# 11.7 막대형 차트도 손쉽게 그려보장

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

plt.bar(range(len(years)), gdp)  # 막대형 차트의 가로축 범위

plt.title("GDP per capita")
plt.ylabel("dollars")

plt.xticks(range(len(years)), years)  # 가로축 범위의 눈금마다 부여할 눈금값을 지정

# 11.8 다중막대형차트
years = [1965, 1975, 1985, 1995, 2005, 2015]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [890, 5120, 11500, 42130, 40560, 38780]
ch = [100, 200, 290, 540, 1760, 7940]

# x_range = range(len(years))
x_range = np.arange(len(years))
plt.bar(x_range-0.3, ko, width=0.25)
plt.bar(x_range+0.0, jp, width=0.25)
plt.bar(x_range+0.3, ch, width=0.25)  # width는 막대의 두께

plt.xticks(range(len(years)), years)  # 가로축 범위의 눈금마다 부여할 눈금값을 지정
plt.title('GDP per capita')
plt.show()

# 11.9 데이터를 점으로 표현하는 산포도 그래프 그리기
# 산포도 플롯 개별 데이터 포인트를 그리는 차트.
# 산포도를 그릴 때는 각 데이터 포인터가 연결되지 않는다. scatter() 함수를 사용한다.

import matlotlib.pyplot as plt
import numpy as np

xData = np.arange(20, 50)
yData = xData + 5 * np.random.randn(30)
# 2*np.random.randn(30)
plt.scatter(xData, yData)
plt.title('Real Age vs Physical Age')
plt.xlabel('Real Age')
plt.ylabel('Physical Age')

plt.savefig("age.png", dpi=300)
plt.show()

import numpy as np
np.random.randn()

# 도전문제 11.4 해보기

# 11.10 피자가 생각나는 파이차트
import matplotlib.pyplot as plt
times=[8,14,2] #24시간
timelabels = ['Sleep', 'Study', 'Play']

plt.pie(times, labels = timelabels, autopct = '%.2f')
plt.show()

# 11.11 히스토그램으로 자료의 분포를 보자
import matplotlib.pyplot as plt
books = [1,6,2,3,1,2,0,2]

plt.hist(books, bins = 6) #데이터가 들어가는 통을 bin이라 하자.

plt.xlabel("boooks")
plt.ylabel('frequency')
plt.show()

# 11.12 겹쳐진 히스토그램도 그리자 : 다중 히스토그램
import numpy as np
import matplotlib.pyplot as plt

n_bins=10
x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hist(x, n_bins, histtype='bar', color='red')
plt.hist(y, n_bins, histtype='bar', color='blue', alpha=0.35) #파란색 히스토그램의 투명도는 0.3 alpha 1: 불투명 alpha 0: 투명
plt.show()

# lab11-3 문제 풀어야함 2022 12 04 AM 6:53
import numpy as np
import matplotlib.pyplot as plt

avr = 10
sigma = 2 #평균 + (표준편차(분산) * 난수) 정규분포로 생성된 난수
rand_num1 = avr + sigma*np.random.rand(1000)
rand_num1
avr = -6
sigma = 3 #평균 + (표준편차(분산) * 난수) 정규분포로 생성된 난수
rand_num2 = avr + sigma*np.random.rand(1000)
rand_num2
# x = np.random.randn(1000)
# y = np.random.randn(1000)*-5
# z = np.random.randn(1000)*10

n_bins = list(range(-15, 15))
n_bins
plt.hist(rand_num1,n_bins, histtype='bar', color='blue', alpha=0.35) #파란색 히스토그램의 투명도는 0.3 alpha 1: 불투명 alpha 0: 투명
plt.hist(rand_num2,n_bins, histtype='bar', color='magenta', alpha=0.35) #파란색 히스토그램의 투명도는 0.3 alpha 1: 불투명 alpha 0: 투명
plt.show()

plt.hist(x, n_bins, histtype='bar', color='blue', alpha=0.35) #파란색 히스토그램의 투명도는 0.3 alpha 1: 불투명 alpha 0: 투명
plt.hist(y, n_bins, histtype='bar', color='red', alpha=0.35) #파란색 히스토그램의 투명도는 0.3 alpha 1: 불투명 alpha 0: 투명
# 파란색 히스토그램의 투명도는 0.3 alpha 1: 불투명 alpha 0: 투명
plt.hist(z, n_bins, histtype='bar', color='green', alpha=0.35)
plt.show()

# 모범답안
import numpy as np
import matplotlib.pyplot as plt

mu1, sigma1 = 10,2
mu2, sigma2 = -6,3

standard_Gauuss = np.random.randn(10000) #표준정규분포 난수
Gauss1 = mu1 + sigma1 * np.random.randn(10000)
Gauss2 = mu2 + sigma2 * np.random.randn(10000)

plt.figure(figsize=(10,6))
plt.hist(standard_Gauuss, bins=50, alpha=0.4)
plt.hist(Gauss1, bins=50, alpha=0.4)
plt.hist(Gauss2, bins=50, alpha=0.4)

plt.show()

# 11.13 상자차트 데이터를 효율적을 표현하는
import numpy as np
import matplotlib.pyplot as plt

random_data = np.random.randn(100)
plt.boxplot(random_data)
plt.show()

# 11.14 여러개의 상자 차트
import numpy as np
import matplotlib.pyplot as plt
data1 = [1,2,3,4,5]
data2 = [2,3,4,5,6]
plt.legend()
plt.show()

plt.boxplot([data1, data2]) #리스트 형식
plt.show()
plt.boxplot(np.array([data1, data2])) #넘파이 배열 형식 열 단위 처리가 기본이다.
plt.show()

# 11.15 한 화면에 여러 그래프 그리기
import matplotlib.pyplot as plt

# 갯수가2*2 크기가 5,5인치
# fig, ax =  plt.subplots(2,2, figsize=(5,5)(2),
# plt.show() 2, figsize=(5,5))
# 
# ax[0,0].plot(range(100), 'r') #ax[행, 열]
# ax[1,0].plot(range(10), 'b')
# ax[0,1].plot(range(10), 'g')
# ax[1,1].plot(range(10), 'k')

ax[0,0].fig.add_subplot(2,3,1)
ax[1,0].fig.add_subplot(2,3,2)
ax[0,1].fig.add_subplot(2,3,3)
ax[1,1].fig.add_subplot(2,3,4)

# 2*2 figure()로 각자 다른 스타일로 정규분포 난수 표현 예제
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, ax = plt.subplots(2,2, figsize=(5,5))

ax[0,0].hist(data[0] ,) #히스토그램
ax[1,0].scatter(data[0], data[1]) #산포도 그래프
ax[0,1].plot(data[0],data[1]) #선형 plot
ax[1,1].hist2d(data[0], data[1]) #2차원 히스토그램
plt.show()