import random
def print_matrix(n):
    for i in range(n):
        string = ""
        for a in range(n):
            string += " "+str(random.randint(0,1))
        print(string.strip())
    
print_matrix(4)
