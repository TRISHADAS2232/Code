class A:
    def code1(self):
        print("a")
class job1(A):
    def code2(self):
        print("code")
class job2:
    def code3(self):
        print("code for job2")
class job3(job1,job2):
    def code4(self):
        print("code for 1 and 2")
o=job3()
o.code1()
o.code2()