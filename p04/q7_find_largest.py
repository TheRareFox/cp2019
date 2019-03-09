def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return max(int(alist[0]),find_largest(alist[1:]))
        
a = 1,2,3,4,5,9
print(find_largest(a))
