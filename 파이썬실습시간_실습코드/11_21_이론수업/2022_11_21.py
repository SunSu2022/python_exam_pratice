import matplotlib.pyplot as plt

f = open(file='export.csv', mode='r', encoding="UTF-8")
lines = f.readlines()

lines = lines[1:]

years=[]
japan=[]
korea=[]

for line in lines :
    line = line.split(',')
    years.append(int(line[0]))
    japan.append(float(line[1]))
    korea.append(float(line[2]))

plt.plot(years, korea, color='blue', linestyle='solid')
plt.plot(years, japan, color='red',linestyle='solid')

plt.title('GDP')

plt.xlabel("years")
plt.ylabel("dollars")

plt.savefig("gdp.png",dpi=600)
plt.show()