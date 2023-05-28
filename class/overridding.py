class a:
    def so(self):
        print("f1")
class b(a):
    def so(self):
        print("f2")
class c(a):
    def so(self):
        print("f3")
class d(b,c):
    def so(self):
        print("f4")
a1=a()
b1=b()
c1=c()
d1=d()
d1.so()