list =[]
while True:
    num = int(input("введіть цифру "))
    if num == 134:
        print(list)
    elif num == 123321456:
        print("програма зупинилася")
        break
    elif list.count(num) >= 1:
        print("ви вже вводили це число")
    else:
        print("ви ще не вводили це число")
        list.append(num)
