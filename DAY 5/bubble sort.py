listx = [3, 2, 7, 8, 4]

for i in range(0, len(listx)-1):
    for j in range(i+1, len(listx)):
        if listx[i] > listx[j]:
            temp = listx[i]
            listx[i] = listx[j]
            listx[j] = temp


print(listx)

listx.reverse()

print(listx)