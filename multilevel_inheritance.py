class Grandparent:
    def greet1(self):
        print("Hello from Grandparent!")

class Parent(Grandparent):
    def greet2(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet3(self):
        print("Hello from Child!")

obj = Child()
obj.greet1()
obj.greet2()
obj.greet3()
