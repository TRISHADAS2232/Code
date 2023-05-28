n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(i,n+1):
        print(k,end=" ")

    print()