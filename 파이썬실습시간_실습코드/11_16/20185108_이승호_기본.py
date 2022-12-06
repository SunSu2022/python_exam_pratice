import numpy as np
f=open("제주도_건강통계-3.csv","r" ) #한국말을 쓸라면 이걸 쓰자
text = f.readlines()

text = text[1:]

obs = []

for line in text:
    new_line = line.split(',')
    obs.append(float(new_line[2]))
    # print(obs) #비만율만 뽑는다,

np_obs = np.array(obs)
print(np_obs)
print(type(np_obs))

# print(np.shape(obs))


# in 으로 딕셔너리 문 안에서 찾을 수 있다.
