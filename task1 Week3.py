import random
list =[]
sum = 0
n = random.randint(0,10)
for x in range(0,n):
    list.append(random.randint(0,10))
for z in range(0,len(list)):

    sum = sum + list[z]
print(list)
print(sum)

for i in range(0,len(list)):
    if list[i] > sum/n:
        print("число",list[i]," більше за середнє арифметичне",sum/n)
    elif list[i]==sum/n:
        print("число",list[i]," дорівнює середньому арифметичному",sum/n)
    else:
        print("число",list[i]," менше за середнє арифметичне",sum/n)
