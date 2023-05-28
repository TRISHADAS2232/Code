def fibo(num):

    listx = [0, 1]

    for i in range(2, num):
        listx.append(listx[-2]+listx[-1])
        
    return  listx

print(fibo(5))

