print("Kilograms Pounds")
for i in range(1,11):
    kilogram = i * 1
    pound = i * 2.2
    if 1<=kilogram<10:
        print("{0:0}         {1:0.1f}".format(kilogram,pound))
    else:
        print("{0:0}        {1:0.1f}".format(kilogram,pound))