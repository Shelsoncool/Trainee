import math
class Circle:
    p1=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
r=int(input("Enter the radius:"))
obj=Circle(r)
print(obj.area())
