one = int(input("Enter side 1: "))
two = int(input("Enter side 2: "))
three = int(input("Enter side 3: "))
if one + two > three:
    print("Perimeter = {}".format(one+two+three))
else:
    print("Invalid triangle!")