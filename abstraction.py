from abc import ABC 
  
class Polygon(ABC):   
  
   # abstract method   
   def sides(self):   
      pass  
  
class Triangle(Polygon):   
  
     
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):   
  
     
   def sides(self):   
      print("Pentagon has 5 sides")   
  
  
  
# Driver code   
t = Triangle()   
t.sides()   
  
  
p = Pentagon()   
p.sides()   
  
  
