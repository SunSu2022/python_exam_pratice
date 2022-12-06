price = int(input('물건 가격: '))

Change = 1000 - price

num500 = (Change / 500) 
Change = Change % 500

num100 = (Change / 100) 
Change = Change % 100

num50 = (Change / 50) 
Change = Change % 50

num10 = (Change / 10) 
Change = Change % 10

sum = int(num500) + int(num100) + int(num10) + int(num50)
print(sum)