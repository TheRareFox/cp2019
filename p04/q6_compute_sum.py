def sum_digits(n):
    if len(str(n)) == 1:
        return int(n)
    else:
        a = str(n)
        return int(a[0]) + int(sum_digits(a[1:]))

print(sum_digits(2321))
