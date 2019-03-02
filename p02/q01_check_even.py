
def is_even(i):
    if i%2 == 0:
        return"{} is even".format(i)
    else:
        return"{} is odd".format(i)

print(is_even(int(input("Enter number: "))))
