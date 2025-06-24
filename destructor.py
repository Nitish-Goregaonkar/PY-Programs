class DestructorExample:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Destructor called, object is being deleted")

# Creating and deleting object
obj = DestructorExample()
del obj  # Manually calling destructor