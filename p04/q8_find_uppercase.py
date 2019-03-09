def find_num_uppercase(str):
    if len(str) == 1:
        if str.isupper():
            return 1
        else:
            return 0
    else:
        if str[0].isupper():
            return 1 + find_num_uppercase(str[1:])
        else:
            return find_num_uppercase(str[1:])

print(find_num_uppercase("Hello WorLd"))
