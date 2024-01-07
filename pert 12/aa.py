def kontol(n):
    if n == 1 or n==2:
        return 1
    else:
        return n*kontol(n-2)
    
print(kontol(5))