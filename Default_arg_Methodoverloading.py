class Demo:
    def greet(self, name="Guest"):
        print(f"Hello, {name}!")

# Create an object
obj = Demo()

# Call the method without passing arguments
obj.greet()

# Call the method by passing an argument
obj.greet("Alice")
