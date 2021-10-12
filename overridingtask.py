class Animal:

    def move(self):
        print("Animal is move")

    def eat(self):
        print("Animal is eat")

class Dog(Animal):
   def move(self):
       print("Dog is move")

   def eat(self):
       print("Dog is eat")

obj1 = Animal()
obj2 = Dog()
obj1.move()
obj2.move()
obj1.eat()
obj2.eat()
