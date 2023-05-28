a=len("asansol")

b=len(['a','b','3'])

print(a,b)

def func(a,b=5):
    return a+b
print(func(5))        #'b' is default parameter
print(func(5,7))

class a():
    def func(self):
        print("f1")
class b():
    def func(self):
        print("f2")

a1=a()
b1=b()
a1.func()
b1.func()