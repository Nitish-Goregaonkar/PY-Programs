class ParameterizedConstructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object with arguments
obj = ParameterizedConstructor("Alice", 25)