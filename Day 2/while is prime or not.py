n = int(input())
i = 2
while(i!= n):
    if n % i == 0:
        print("not prime")
        exit(0)
    n += 1
print("prime")