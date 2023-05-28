class a:
    def f1(self):
        print("i am in class a")
class b:
    def f2(self):
        print("i am in class b")
class c(a,b):
    def f3(self):
        print("i am in class c")
#a1=a()
#b1=b()
c1=c()
c1.f1()
c1.f2()
c1.f3()