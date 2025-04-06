#Example of Method Overloading Using Default Arguments and *args
class MathOperations: 
    # Method to add numbers 
    def add(self, a, b=0, c=0): 
        return a + b + c 
 
# Testing method overloading 
math_op = MathOperations() 
print("Addition of two numbers:", math_op.add(5, 10))   
print("Addition of three numbers:", math_op.add(5, 10, 15))   