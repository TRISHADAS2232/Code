class a:
    def f1(self):
        print("i am f1")
class b(a):
    def f2(self):
        print("i am f2")
class c(b):
    def f3(self):
        print("i am f3")
c1=c()
c1.f1()
c1.f2()
c1.f3()