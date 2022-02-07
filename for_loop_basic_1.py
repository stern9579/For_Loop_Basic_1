#Basic
for x in range(151):
    print(x)

#Multiples of Five 
for x in range (5, 1001, 5):
    print(x)

#Counting, the Dojo Way
for x in range (1, 101):
    if ((x % 5 == 0) and (x % 10 == 0)):
        print('Coding Dojo')
    elif(x % 5 == 0):
        print('Coding')
    else:
        print(x)

#Whoa. That Sucker's Huge
sum=0
for x in range(500001):
    if (x % 2 != 0):
        sum += x
print(sum)

#Countdown by Fours
for x in range(2018, -1, -4):
    print(x)

#Flexible Counter
lowNum=1 
highNum=600
mult=7

for x in range (1, 601):
    if (x % 7 == 0):
        print(x)