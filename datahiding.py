class Student:
    def __init__(self, name, grade):
        self.__name = name  # Private variable
        self.__grade = grade  # Private variable

    # Public method to access private variable
    def show_details(self):
        print(f"Student Name: {self.__name}")
        print(f"Grade: {self.__grade}")

# Create an object of the Student class
student1 = Student("Alice", "A")

# Access details using the public method
student1.show_details()
