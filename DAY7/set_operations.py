
print("start")
n = int(input())
s = set(map(int, input().split()))
for i in range(0, int(input())):
    operation = list(input().split(" "))
    if len(operation) == 2:
        if operation[0] == "remove":
            s.remove(int(operation[1]))
        elif operation[0] == "discard":
            s.discard(int(operation[1]))
    elif len(operation) == 1:
        if operation[0] == "pop":
            s.pop()
print(sum(s))

"""
9
1 2 3 4 5 6 7 8 9
12
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
discard 5
discard 6
discard 8
remove 4
"""