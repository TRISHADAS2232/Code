def prime_ornot(integer):
    for i in range(2, integer):
        if integer % 2 == 0:
            print('not prime')
            exit(0)
    print('prime')
prime_ornot(int(input()))