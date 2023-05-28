def fibo(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibo(n-2)+fibo(n-1)

print(fibo(9))
