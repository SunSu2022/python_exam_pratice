# 12.1 
# 엑셀은 행과 열로 이루어진 표 데이터 처리 굿 
# 넘파이는 데이터 속성 표시하는 행이나 열의 레이블을 가지고 있지 않음
# 판다스 패키지로 해결
# 판다스의 특징
# 빠르고 효율적이고 다양한 표현력을 갖춘 자료구조
# 다양한 형태의 데이터에 적합
# 넘파이는 자료형 하나인데 판다스는 이종자료형가능
# 핵심구조
#     Series : 1차원 구조를 가진 하나의 열
#     Dataframe : 복수의 열을 가진 2차원 데이터
# 결측데이터 처리 데이터 추가및삭제 데이터 정렬과 다양한 데이터 조작
# 각종 데이터 자료형들을 데이터프레임으로 변환가능
# 데이터 보기 및 검사
# • mean()로 모든 열의 ^평균^을 계산할 수 있다.
# • corr()로 데이터 프레임의 ^열 사이의 상관 관계^를 계산할 수 있다.
# • count()로 각 데이터 프레임 열에서 ^null이 아닌 값의 개수^를 계산할 수 있다.
# • 필터, 정렬 및 그룹화
# • sort_values()로 데이터를 ^정렬^할 수 있다.
# • 조건을 사용하여 열을 필터링할 수 있다.
# • groupby()를 이용하여 ^기준에 따라 ^몇 개의 그룹으로 데이터를 분할^할 수 있다.
# • 데이터 정제
# 12.6 Series and Dataframe
# 판다스의 데이터 구조는 넘파이 배열을 이용해 구현된다

import pandas as pd
import numpy as np
# 하나하나가 판다스 시리즈가 된다.
# 시리즈는 레이블이 붙어있는 1차원 벡터
name = pd.Series(['김레코','이재헌','김현종','심순복','허각',])
age = pd.Series([19,23,22,19,16])
sex = pd.Series(['여','여','남','여','남'])
grade = pd.Series([4.35,4.23,4.25,4.37,4.25])
print(name, age, sex, grade)

# 딕셔너리 형식의 데이터로 데이터 프레임을 생성함
df = pd.DataFrame({'이름':name, '나이':age, '성별':sex, '평점':grade, })
# 시리즈를 만들어 주고 데이터프레임으로 합쳐준다.

# 12.3 csv
# csv는 테이블 형식의 데이터를 저장 이동 사용 구조화된 텍트 파일 형식
# csv는 쉼표로 구분한 변수의 약자
# • CSV 파일은 필드를 나타내는 열과 레코드를 나타내는 행으로 구성
# • 만약 데이터의 중간에 ^구분자^가 포함되어야 한다면 ^따옴표를 사용하여 필드를 묶어야 함
# • 예를 들어서 'Gildong, Hong'이라는 데이터가 있다고 하자. 
# 데이터의 중간에 쉼표(,)가 포함되어 있다. 이러한 경우에는 구분자로 사용되는 쉼표와 구분하기 위하여 
# ^^반드시 데이터를 따옴표로 감싸야 한다. •
#  CSV 파일의 첫 번째 레코드에는 열 제목이 포함되어 있을 수 있다. 
# • CSV 형식 자체의 요구사항이 아니라 단순히 일반적인 관행
# • CSV 파일의 크기를 알 수 없고 잠재적으로 크기가 큰 경우 한 번에 모든 레코드를 읽지
# 않는 것이 좋다. 
# • 이때는 현재 행을 읽고, 현재 행을 처리한 후에 삭제하고 다음 행을 가져오는 방식이 필요할 수도 있
# 다. 아니면 특정한 크기만큼의 데이터를 읽어서 처리한 뒤에, 다음으로 또 그만큼의 크기를 가져오는
# 방식을 사용할 수도 있을 것이다.
# 12.7 판다스로 데이터 파일을 읽기

import pandas as pd
df = pd.read_csv('countries.csv')
df #인덱스 번호는 판다스가 임의로 추가한 열이다.
# newdf = np.array(df)
# newdf[0,0]

# 12.8 인덱스와 컴럼스 객체
# 인덱스는 행들의 레이블이고 컬럼스는 열들의 레이블이 저장된 객체이다.
import pandas as pd #index_col = 0 // 0열이 인덱스로 사용된다.
df = pd.read_csv('countries.csv', index_col = 0)
print(df)

# 12.9 열 기준으로 데이터 선택하기
import pandas as pd

df_my_index =pd.read_csv('countries.csv', index_col=0)
df_no_index =pd.read_csv('countries.csv')
df_my_index[['population']]
df_no_index['population']

df_my_index[ ['area', 'population'] ]
# df_my_index[ 'area', 'population' ] #이건 오류가 난다.두개이상은 리스트
#  안에 넣어서 전달 해야하는듯
# 데이터 프레임으로 읽을 때 컬럼만 넣으면 그냥 데이터만 나오는데 
# 리스트안에 컬럼을 넣어서 인자로 주면 컬럼이 자료위에 표시가 된다.

# 12.10 데이터 가시화 하기
import pandas as pd
import matplotlib.pyplot as plt

# 파이차트
countries_df = pd.read_csv('countries.csv', index_col = 0)
countries_df['population'].plot(kind='pie')
plt.show()

# bar차트
countries_df = pd.read_csv('countries.csv', index_col = 0)
countries_df['area'].plot(kind='bar', color=('b', 'darkorange','g','r','m'))
plt.show()

# 12.11 판다스에서도 슬라이싱으로 행 선택이 된다.
countries_df.head()
countries_df[:3]
countries_df.loc['US'] #행의 레이블이 'KR인 행만을 선택하기
countries_df.loc['KR', 'country'] #loc로 index, column 선택하면 원하는 요소 추출가능
countries_df['population'][:3]
# 밑에 두개 의미가 같다.
countries_df.loc['US', 'capital']
countries_df['capital'].loc['US']

# 12.12 새로운 열을 쉽게 생성해 보자
import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('countries.csv', index_col = 0)
countries_df['density'] = countries_df['population'] / countries_df['area']
countries_df

# 판다스로 csv파일 읽으면 문자열이 아니라 실수데이터로 바로 읽힌다는 것을 알 수 있다. float() 이용해서 굳이 바꿀 필요 ㄴㄴ
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('weather.csv', index_col=0, encoding='CP949')
weather
weather['평균 기온(m/s)'].plot(kind='hist',color='r', bins=33, alpha=1)
weather['최대 풍속(m/s)'].plot(kind='hist',color='g', bins=33, alpha=0.35)
weather['평균 풍속(m/s)'].plot(kind='hist',color='b', bins=33, alpha=0.35)
plt.show()

# 12.13 데이터를 간편 분석 기능
import pandas as pd
weather= pd.read_csv('weather.csv', index_col=0, encoding='CP949')

print(weather)
print(weather.describe()) #간단분석
weather.mean()
weather.std()
weather.min()
weather.max()

# 판다스 표준편차 넘파이 표준편차 차이
# 판다스는 디폴트로 베셀보정이란걸 적용하는데 표본크기 n 대신에 n-1을 적용하는 것으로 모분산 추정에서 편향을 보정하는 역할을 한다.

# 12.14 데이터 집계 분석도 손쉽게
weather = pd.read_csv('weather.csv', index_col = 0, encoding='CP949')
weather.count() #weather가 3개의 열을 가지고 있고, 각각담긴 데이터의 갯수를 알 수 있다.
weather['최대 풍속(m/s)'].count()
weather['최대 풍속(m/s)'].describe()

weather[['최대 풍속(m/s)', '평균 풍속(m/s)']].mean() #평균
weather.mean()[['최대 풍속(m/s)', '평균 풍속(m/s)']] #평균

# lab-12_1 울릉도 바람 와우
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('weather.csv', encoding='CP949')
monthly = [None for x in range(12)] #1~12월별 리스트임
type(monthly)
monthly_wind = [0 for x in range(12)] #각 달의 평균 풍속을 담을 리스트
# 마지막에 해당 행의데이터가 측정된 달을 기록한 열을 추가
weather['month'] =pd.DatetimeIndex(weather['일시']).month

for i in range(12):
    monthly[i] = weather[ weather['month'] == i+1 ]#달별로 분리
    # weather['month'] == i+1 이문장이 논리적 인덱싱이라고 생각하면댐 asd[asd>5] 이거랑 비슷한 거임
    # 몇월달인지 == 을 통해서 물어보고 맞으면 각 달별 데이터프레임에 있는 것에 넣어주는 것! 
    monthly_wind[i] = monthly[i].mean()['평균 풍속(m/s)'] #각 달별 데이터 프레임에 mean() 통해서 바람 평균을 넣어준다.
monthly_wind #list
plt.plot(monthly_wind, 'red')
plt.show()

# 12.15 데이터를 특정한 값에 기반하여 묶는 기능 : 그룹핑
weather = pd.read_csv('weather.csv', encoding='CP949')
weather['month'] =pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()
means
weather.tail() #month가 추가디어있다.

sum_data = weather.groupby('month').sum()
sum_data #해당 레이블에 데이터를 그룹별로 모두 더해 값을 확인ㄴ

# lab_12-3 울릉도 몇월에 바람이 가장 강할까 groupby() 활용
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('weather.csv', encoding='CP949')

weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean() #'month'로 그룹핑 해서 각 달별로 평균을 낸다.
means['평균 풍속(m/s)'].plot(kind='bar', color='green', alpha=0.2)

plt.show()
