startindex = int(input())
endindex = int(input())
count = 0
for i in range(startindex, endindex+1):
    flag = True
    for b in range(2, i):
        if i % b == 0:
            flag = False
            break
    if flag == True:
        count += 1
        if count <= 3:
            print(i)
        else:
            exit(0)
