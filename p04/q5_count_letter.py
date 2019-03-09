def count_letter(str, ch):
    if len(str) == 1:
        if str == ch:
            return 1
    else:
        if str[0] == ch:
            return 1 + count_letter(str[1:],ch)
        else:
            return count_letter(str[1:],ch)

print(count_letter("welcome","e"))
