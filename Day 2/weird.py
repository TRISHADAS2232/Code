n = int(input())
if n % 2 != 0:
    print("weird")
else:
    if n >= 2 and n <= 5:
        print("not weird")
    elif n >= 6 and n <= 20:
        print("weird")
    elif n > 20:
        print("not weird")
