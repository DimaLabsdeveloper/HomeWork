import random
n = random.randint(0,10)
list = []
for x in range(0,n):
    list.append(random.randint(0,10))
if n == 0:
        print("число n дорівнює 0 ")
else:
    for x in range(0,n):
        if x == 0:
            if list[0] > list[1]:
                print("число",list[0]," більше за",list[1])
            elif list[0] == list[1]:
                print("число",list[0]," дорівнює ",list[1])
            elif list[0] < list[1]:
                print("число",list[0]," менше за ",list[1])

        elif x == n-1:
            if list[n-1] > list[n-2]:
                print("число",list[n-1]," більше за",list[n-2])
            elif list[n-1] == list[n-2]:
                print("число",list[n-1]," дорівнює ",list[n-2])
            elif list[n-1] < list[n-2]:
                print("число",list[n-1]," менше за ",list[n-2])
        
        if list[n] > list[n-1]:
            print("число",list[n]," більше за",list[n-1])
        elif list[n] == list[n]:
            print("число",list[n]," дорівнює ",list[n-1])
        elif list[n] < list[n-1]:
            print("число",list[n]," менше за ",list[n-1])
        elif list[n] > list[n+1]:
            print("число",list[n]," більше за",list[n+1])
        elif list[n] == list[n+1]:
            print("число",list[n+1]," дорівнює ",list[n+1])
        elif list[n] < list[n+1]:
            print("число",list[n]," менше за ",list[n+1])

    