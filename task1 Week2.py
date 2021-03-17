print("Ця програма рахує Факторіал")
n = int(input("n = "))
factorial = n
if n == 1 :
    print("n! = 1")
else:
    
    while n > 1:
       
        factorial = factorial * (n-1)
        
        n = n-1        
    print("n! = ", factorial)