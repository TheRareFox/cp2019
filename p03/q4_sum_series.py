def m_series(i):
    num = 0
    print("i         m(i)")
    for n in range(1,i+1):
        num += n/(n+1)
        print("{0}{1:>15.4f}".format(n,num))
    
m_series(int(input("Enter number: ")))
        
        
    
