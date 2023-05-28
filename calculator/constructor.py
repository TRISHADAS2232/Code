class cal():
    def __init__(self, a , b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return a*b

    def div(self):
        return self.a/self.b


a = int(input("enter first number:"))

b = int(input("enter second number:"))


obj = cal(a, b)
c = obj.mul()
print(c)
