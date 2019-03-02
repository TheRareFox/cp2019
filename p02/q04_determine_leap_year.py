def leap_year(n):
    if (n%4 == 0 and n%100 != 0) or n%400 == 0:
        return "Leap"
    else:
        return "Non-Leap"

print(leap_year(int(input("Enter year: "))))