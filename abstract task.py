from abc import ABC

class Number(ABC):

    def add(self):
        pass

class No1(Number):

    def add(self):
        print("add the 2 values")

class No2(Number):

    def add(self):
        print("add the 3 numbers")

obj1 = No1()
obj1.add()

obj2 = No2()
obj2.add()
    

    
