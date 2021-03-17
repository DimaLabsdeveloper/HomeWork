import random

list = []
listUnique=[]

for x in range(1,11): 
    list.append(random.randint(1,10))

print(list)

for c in range(0,10):
    if list[c] not in listUnique:
        listUnique.append(list[c])

print(listUnique)

for i in range(0,len(listUnique)):
    print("Number of occurrences of the number ",listUnique[i], "-",list.count(listUnique[i]))
    
print("Number of occurrences of the number -", len(listUnique))    

    

