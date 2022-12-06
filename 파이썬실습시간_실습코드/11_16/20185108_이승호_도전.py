import numpy as np
import random 
f=open("제주도_건강통계-3.csv","r" ) #한국말을 쓸라면 이걸 쓰자
text = f.readlines()

text = text[1:]

year = []

for line in text:
    new_line = line.split(',')
    year.append(int(new_line[1]))
    # print(year) #년도를 뽑는다

np_year = np.array(year)
# print(np_year)

np_year = np_year.reshape(6,4)
print(np_year)
# print(np_year[1:5, 1:3])




##########################################################

f=open("제주도_건강통계-3.csv","r" ) #한국말을 쓸라면 이걸 쓰자
text = f.readlines()

text = text[1:]

obs = []

for line in text:
    new_line = line.split(',')
    obs.append(float(new_line[2]))
    # print(obs) #비만율만 뽑는다,

np_obs = np.array(obs)
# print(np_obs)
# print(type(np_obs))

np_obs = np_obs.reshape(6,4)
# print(np_obs)
# New_np_obs = np_obs[1:5, 1:3]
# print(New_np_obs)

print(np_obs)

print(np_year > 2015)

mu=10
sigma=2
randoms = mu+sigma*np.random.randn(6,4)
# print(randoms)

print(np_obs + randoms)







