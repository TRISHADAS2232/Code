class test:
    def __init__(self, listarr):
        self.listarr = list(('pastry', 'banana'))

    def add(self, item):
        self.listarr.append(item)
        print(self.listarr[0:])


list1 = []
obj = test(list1)
obj.add('cake')