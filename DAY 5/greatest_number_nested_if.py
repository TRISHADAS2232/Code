a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("a is the greatest.", a)
if b > a and b > c:
    print("b is the greatest.", b)
if c > a and c > b:
    print("c is the greatest.", c)


if a > b:
    if b > c:
        print("a is the greatest", a)
    else:
        if a > c:
            print("a is the greatest", a)
        else:
            print("c is the greatest", c)
else:
    if b > c:
        print("b is the greatest", b)
    else:
        print("c is the greatest", c)


