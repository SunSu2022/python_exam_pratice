# import pandas as pd
# print(pd.__version__)

# new_series = pd.Series(['김수안','김수정','박동윤','강이안','강지안'])
# age_series = pd.Series([19, 23, 22, 19, 16])
# sex_series = pd.Series(['여','여','남','여','남'])
# grade_series = pd.Series([4.35, 4.23, 4.25, 4.37, 4.25])
# # print(new_series, age_series, sex_series, grade_series)
# df = pd.DataFrame({'이름': new_series, '나이':age_series,
#                 '성별': sex_series, '평점':grade_series})
# # print(df)

# import pandas as pd 

# df = pd.read_csv(r'C:\Users\user\Desktop\20185108 이승호\countries.csv', index_col = 0)
# df_my_index = pd.read_csv(r'C:\Users\user\Desktop\20185108 이승호\countries.csv', index_col = 0)
# df_no_index = pd.read_csv(r'C:\Users\user\Desktop\20185108 이승호\countries.csv')

# print(df_no_index)
# print(df_my_index)
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv(r'C:\Users\PSENG\Desktop\이승호\3학년 2학기\파이썬 프로그래밍\기말고사_자료\파이썬실습시간_실습코드\weather.csv', index_col = 0, encoding='CP949')
weather['최대 풍속(m/s)'].plot(kind='hist', bins=33)
plt.show()

print(weather)

# print(weather.describe())
# print()

# print(weather.mean())
# print()

# print(weather.std())
# print()

# print(weather.count())
# print()

# print(weather['최대 풍속(m/s)'].count())
# print()

# print(weather['최대 풍속(m/s)'].count())


