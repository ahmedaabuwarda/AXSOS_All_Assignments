# print from 1 to 150
for i in range(0, 150):
    print(i)


for i in range(5, 1000):
    if (i % 5 == 0):
        print(i)

for i in range(1, 100):
    if (i % 10 == 0):
        print("Coding Dojo")
    elif (i % 5 == 0):
        print("Coding")

sum = 0
for i in range(0, 500000):
    if(i % 2 != 0):
        sum += 1
    
print(sum)

for i in range(2018, 0, -4):
    print(i)

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if (i % mult == 0):
        print(i)

def n(n=1):
    print(n)

def n(n=1,m=1):
    print(n,m)


n(n=5)
n(n=5, m=10)