class Parent1:
    def greet1(self):
        print("Hello from Parent1!")

class Parent2:
    def greet2(self):
        print("Hello from Parent2!")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.greet1()
obj.greet2()