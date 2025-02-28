def main():
    a=A()
    B=A()
    print()
    print ("accessing via object: ")
    print('public Variable :',a.public_var)
    print()
    # print('private variable',a.__private_var) if we uncomment this print then error will occur

class A:
    # public variable
    public_var=0

    #private Variable
    __private_var=1

    def _init_(self,str='welcome!'):
        print('constructor is started')
        print ()
        print("constructor(): ",str)
        print()
        print("public variable: ", self.public_var)
        print()
        print("private variable:",self.__private_var)

#driver code
main()