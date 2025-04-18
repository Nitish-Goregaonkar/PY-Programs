class Parent:
    def show_message(self):
        print("This is the parent class method.")

class Child(Parent):
    def show_message(self):
        print("This is the child class method.")

# Create instances
p = Parent()
c = Child()

# Call methods
p.show_message()
c.show_message()
