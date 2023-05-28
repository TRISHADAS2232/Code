class a:
    def code1(self):
        print("parent of b and c")
class b(a):
    def code2(self):
        print("child of a")
class c(a):
    def code3(self):
        print("chilf of a")
o1=c()
o2=b()
o1.code1()
o1.code3()
o2.code1()
o2.code2()