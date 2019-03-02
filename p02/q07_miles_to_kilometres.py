print("Miles Kilometers Kilometers Miles")

for i in range(1,11):
    
    if 7<=i<=9:
        print("{0} {1:>10.3f} {2:>6.0f} {3:>14.3f}".format(i, i*1.609, i*5+15 , (5*i+15)*1.609))
    elif i == 10:
        print("{0} {1:>9.3f} {2:>6.0f} {3:>15.3f}".format(i, i*1.609, i*5+15 , (5*i+15)*1.609))
    else:
        print("{0} {1:>9.3f} {2:>7.0f} {3:>14.3f}".format(i, i*1.609, i*5+15 , (5*i+15)*1.609))

