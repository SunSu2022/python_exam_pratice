import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv(r'C:\Users\PSENG\Desktop\이승호\3학년 2학기\파이썬 프로그래밍\기말고사_자료\파이썬실습시간_실습코드\weather.csv', encoding='CP949')
# print(weather)
print() #한칸 줄 띄우기
monthly = [None for x in range(12)] #0~11리스트 만들어 주고 0넣어준다
print(monthly)
monthly_wind = [0 for x in range(12)] #0~11리스트 만들어 주고 0넣어준다
print(monthly_wind)

weather['month'] = pd.DatetimeIndex(weather['일시']).month
# print(weather)

for i in range(12):
    monthly[i] = weather[ weather['month'] == i+1] # 각 달마다 슬라이스 해서 달별로 모아 준다 
    monthly_wind[i] = monthly[i].mean()['평균 풍속(m/s)'] #1월 부터 12월 모아두운것 mean()써서 평균 데이터 프레임 만들어 준다.

plt.plot(monthly_wind)
plt.show()
