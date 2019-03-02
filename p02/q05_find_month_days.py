months = int(input("Enter Month: "))
year = int(input("Enter Year: "))

from calendar import monthrange
month,num_days = monthrange(year, months)
print(num_days)