import random
list = []
list2 = []
for x in range(1,11):
    list.append(random.random())
list.sort()
list2.append(list[9])
list2.append(list[8])
list2.append(list[7])
list2.reverse()
print(list2)