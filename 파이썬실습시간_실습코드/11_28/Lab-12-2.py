import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('weather.csv', encoding='CP949')

monthly = [None for x in range(12)]
monthly_wind = [0 for x in range(12)]

weather['month'] = pd.DatetimeIndex(weather['일시']).month
print(weather)

for i in range(12):
    monthly[i] = weather[ weather['month'] == i+1] # 각 달마다 슬라이스 해서 달별로 모아 준다 
    monthly_wind[i] = monthly[i].mean()['평균 풍속(m/s)'] #1월 부터 12월 모아두운것 mean()써서 평균 데이터 프레임 만들어 준다.

# plt.plot(monthly_wind)
# plt.show()
