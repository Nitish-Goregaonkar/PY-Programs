#Example of Method Overloading Using Default Arguments and *args
# class MathOperations: 
#     # Method to add numbers 
#     def add(self, a, b=0, c=0): 
#         return a + b + c 
 
# # Testing method overloading 
# math_op = MathOperations() 
# print("Addition of two numbers:", math_op.add(5, 10))   
# print("Addition of three numbers:", math_op.add(5, 10, 15))   

#Example of Method Overloading Using *args
class MathOperations: 
    def add(self, *args): 
        return sum(args) 
 
# Testing method overloading with varying arguments 
math_op = MathOperations() 
print("Addition of two numbers:", math_op.add(5, 10))   
print("Addition of three numbers:", math_op.add(5, 10, 15))  
print("Addition of four numbers:", math_op.add(5, 10, 15, 20)) 


#example of method overriding
class Animal: 
    def sound(self): 
        return "Animal makes sound" 