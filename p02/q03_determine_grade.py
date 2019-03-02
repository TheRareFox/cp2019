def grade(n):
    if 0<=n<=34:
        return "U"
    elif 35<=n<=44:
        return "S"
    elif 45<=n<=49:
        return "E"
    elif 50<=n<=54:
        return "D"
    elif 55<=n<=59:
        return "C"
    elif 60<=n<=69:
        return "B"
    elif 70<=n<=100:
        return"A"
    else:
        return "Invalid! Score must be within 0 - 100"
    
print(grade(int(input("Enter score: "))))
