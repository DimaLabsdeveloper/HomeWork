def NOD(a,b):
    
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    
    print("НОД:",a + b)
while True:
    
        x = int(input('a = '))
        y = int(input('b = '))
        NOD(x, y)
   
        break
