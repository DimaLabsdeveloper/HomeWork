

while 1:   
    x = float(input("число 1: "))
    y = float(input("число 2: "))
    symbol = input("Введіть знак(+,-,/,*): ")
    if symbol in ('+', '-', '*', '/'):
        
        if symbol == '+':
            print(x+y)
        elif symbol == '-':
            print(x-y)
        elif symbol == '*':
            print(x*y)
        elif symbol == '/':
            if y != 0 :
                print(x/y)
            else:
                print("Ділення на ноль!")
    else:
        print("Невірний знак операції!")
        break


