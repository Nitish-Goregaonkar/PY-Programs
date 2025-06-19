class Example:
    def __init__(self):
        self.__private_var = 42

    def get_private_var(self):
        return self.__private_var

obj = Example()
print(obj.get_private_var())  # Access via method
# print(obj.__private_var)     # Will throw an AttributeError