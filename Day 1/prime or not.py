number = int(input())
for i in range(2, number):
    if number % i == 0:
        print("not prime")
        exit(0)
print("prime")