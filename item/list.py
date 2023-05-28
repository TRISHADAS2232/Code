class item():
    def __init__(self,listx):

        self.listx=[]

    def add_item(self,product):
        self.listx.append(product)
        print(self.listx[0:])

    def remove_item(self,product):
        self.listx.remove(product)
        print(self.list[0:])


list1=[]
obj=item(list1)

obj.add_item('biscuit')

