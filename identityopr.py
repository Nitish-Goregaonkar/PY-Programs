#Return True, if variables on either side of the operator point to the same object and False otherwise

a=3
b=3
print("value of a and b are", a,b)
print("the memory location of a is ",id(a))
print("the memory location of b is",id(b))
print (a is b)
#true

print(a is not b)
#false

