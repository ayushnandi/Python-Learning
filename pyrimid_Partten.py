def full_pyrmid(n):
    for i in range (1, n+1):
        for j in range (n-i):
            print(" ",end="")
        for k in range (1 , 2*i):
            print("*", end="")
        print()
full_pyrmid(5)