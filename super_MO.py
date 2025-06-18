class Parent:
    def show_message(self):
        print("This is the parent class method.")

class Child(Parent):
    def show_message(self):
        # Call the parent class method
        super().show_message()
        print("This is the child class method.")

# Create an instance of the child class
c = Child()

# Call the overridden method
c.show_message()