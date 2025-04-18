class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child1(Parent):
    def greet1(self):
        print("Hello from Child1!")

class Child2(Parent):
    def greet2(self):
        print("Hello from Child2!")

obj1 = Child1()
obj2 = Child2()

obj1.greet()
obj1.greet1()
obj2.greet()
obj2.greet2()
