import random
fib1 = 1
fib2 = 1
n = random.randint(0,10)
 
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    print(fib1)