# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
        
# Creating a derived class
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(obj1.c)
# Driver code
obj1 = Base()
obj2 = Derived()

#print(obj1.a)
#print(obj1.c)
print(obj2.c)

