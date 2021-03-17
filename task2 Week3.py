import random
n = random.randint(0,10)
list = []

for x in range(0,n):
    list.append(random.randint(0,10))
print(list)
if n == 0 :
        print("число n дорівнює 0 ")
elif n == 1:
    print("Найбільший елемент",list[n-1])
else:
    
    for x in range(0,n):
        if x == 0:
            if list[x] > list[x+1]:
                print("число",list[x]," більше за",list[x+1])
            elif list[x] == list[x+1]:
                print("число",list[x]," дорівнює ",list[x+1])
            elif list[x] < list[x+1]:
                print("число",list[x]," менше за ",list[x+1])

        elif x == n-1:
            if list[n-1] > list[n-2]:
                print("число",list[n-1]," більше за",list[n-2])
            elif list[n-1] == list[n-2]:
                print("число",list[n-1]," дорівнює ",list[n-2])
            elif list[n-1] < list[n-2]:
                print("число",list[n-1]," менше за ",list[n-2])
        else:
            maxValeu = list[x] 
            if list[x] < list[x-1]:
                maxValeu = list[x-1]
            elif maxValeu < list[x+1] :
                maxValeu = list[x+1]
            print ("Найбільший елемент",maxValeu)

    