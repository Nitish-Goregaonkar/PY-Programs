class Sample:
    """
    This is a sample class to demonstrate built-in attributes.
    """
    pass

# Create an instance of the class
obj = Sample()

# Display the built-in attributes of the class
print(f"__dict__      : {Sample.__dict__}")        # Dictionary storing class namespace
print(f"__name__      : {Sample.__name__}")        # Name of the class
print(f"__bases__     : {Sample.__bases__}")       # Base classes in a tuple
print(f"__doc__       : {Sample.__doc__}")         # Docstring of the class
print(f"__module__    : {Sample.__module__}")      # Module where the class is defined
print(f"__qualname__  : {Sample.__qualname__}")    # Qualified name of the class
print(f"__annotations__: {Sample.__annotations__}")# Annotations in the class
print(f"__weakref__   : {getattr(Sample, '__weakref__', None)}") # Weak references to the class
print(f"__sizeof__    : {Sample.__sizeof__()}")    # Size of the class object in memory
print(f"__subclasses__: {Sample.__subclasses__()}")# List of direct subclasses of the class