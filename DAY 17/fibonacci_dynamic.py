def fibo(n):

    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return(fibo(n-2)+fibo(n-1))

for i in range(0, 8):
    print(fibo(i))