#
# Python Ver:   3.12.6
#
# Author:       Prince M. Macaldo
#
# Purpose:      Abstraction Submission Assignment from the Tech Academy 
#  



from abc import ABC, abstractmethod  

 
class Shape(ABC):  
    
    @abstractmethod  
    def area(self):  
        pass   


class Rectangle(Shape):  
    
    def __init__(self, width, height):  
        self.width = width  
        self.height = height  
    
    # Implementing the abstract method  
    def area(self):  
        return self.width * self.height  


rectangle = Rectangle(5, 10)  
print("Area of the rectangle:", rectangle.area())
