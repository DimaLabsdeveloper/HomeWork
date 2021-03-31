import random
steps =int(input("кроків:"))
def circlelist(lst, steps):
    
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
nums =[]
for x in range(3,10):
    nums.append(random.randint(0,10))

print(nums)
 
circlelist(nums, -steps)
print(nums)
 
