import random
def print_matrix(n):
    for i in range(n):
        string = str(random.randint(0,1))
        for a in range(n-1):
            string += " "+str(random.randint(0,1))
        print(string)
    
print_matrix(4)
