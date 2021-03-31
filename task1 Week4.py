a = int(input(("Ведіть a")))
b = int(input(("Ведіть b")))
 
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
 
print(a + b)