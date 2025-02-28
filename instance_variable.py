class rectangle:
    def set_values(self,l,b):
        self.length=l
        self.breadth=b
    
    def get_values(self):
        print("Length of rectangle: ",self.length," id: ",id(self.length))
        print("breadth of rectangle: ",self.breadth," id: ",id(self.breadth))

    def area(self):
        self.area = self.length * self.breadth
        print("Area of rectangle is ",self.area)

r = rectangle()
length =float(input("Enter the length:  "))
breadth =float(input("Enter the breadth:  "))
#setting instance variable
r.set_values(length,breadth)
#accessing instance variable
r.get_values()
r.area()
