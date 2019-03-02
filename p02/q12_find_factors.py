a = int(input())
x = 2
lis = []
while a >1:
    if a % x ==0:
        a = a/x
        lis.append(x)
    else:
        x += 1

print(lis)
