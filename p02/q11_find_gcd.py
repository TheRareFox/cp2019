a = int(input())
b = int(input())
x = a-1
list = []
while x>0:
    if a%x == 0 and b %x ==0:
        list.append(x)
    x -= 1
    
list.sort()
print(list[-1])
