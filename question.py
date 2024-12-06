class rectangle:

  def set_dimensions(self,length,breadth):
    self.length = length
    self.breadth = breadth
  
  def area(self):
    return self.length * self.breadth

  def peramiter(self):
    return 2*(self.length + self.breadth)


length= int(input("Enter the legth of rectangle:"))
breadth= int(input("Enter the breadth of rectangle:"))
area= rectangle()
area.set_dimensions(length,breadth)
peramiter= rectangle()
peramiter.set_dimensions(length,breadth)
print("Area of rectangle is:",area.area())
print("Peramiter of rectangle is:",area.peramiter())