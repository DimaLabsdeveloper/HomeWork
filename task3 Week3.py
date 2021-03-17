import random
list1 =[]
list2 = []
n = random.randint(0,10)
for x in range(0,n):
    list1.append(random.randint(0,10))
m = random.randint(0,10)
for x in range(0,m):
    list2.append(random.randint(0,10))
print(list1)
print(list2)
for x in range(0,n):
    list2.count(list1[x])
    if list2.count(list1[x]) > 0:
        print("елемент",list1[x],"присутній в другому списку")
    else:
        print("елемент",list1[x],"не присутній в другому списку")
