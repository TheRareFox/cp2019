def display_pattern(n):
    pattern=[]
    a="1"
    pattern.append(a)
    for i in range(2, n+1):
        a=str(i)+" "+a
        pattern.append(a)

    for i in pattern:
        num = (n*2-len(i))
        spaces = ""
        for space in range(num):
            spaces += " "
        print(spaces + i)
display_pattern(int(input()))
