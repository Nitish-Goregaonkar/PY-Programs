# Book class with user input
class Book: #class
    #creating constructor
    def __init__(self, name, author, price):
        self.name = name #name to the name argument
        self.author = author #author to author argument
        self.price = price #price to price arguments
    
    def display_details(self): #displaying the information
        print(f"Book Name: {self.name}, Author: {self.author}, Price: {self.price}")
#taking inputs from user name of the book, author of the boook and the price of the book
name = input("Enter book name: ") 
author = input("Enter author name: ")
price = float(input("Enter book price: "))
#creating object of book class
book = Book(name, author, price)
book.display_details()


# BankAccount class with user input and conditional balance assignment
class BankAccount:
    #creating the constructor
    def __init__(self, account_number, balance=1000):
        self.account_number = account_number
        self.balance = max(balance, 100)
    #displaying the details 
    def display_account(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
#taking input from user:- 2 account numbers with there balance
account_number1 = input("Enter first account number: ")
balance1 = float(input("Enter first account balance: "))

account_number2 = input("Enter second account number: ")
balance2 = float(input("Enter second account balance: "))
#creating the 2 objects of the bankaccount class
account1 = BankAccount(account_number1, balance1)
account2 = BankAccount(account_number2, balance2)
#calling display method to shown the details
account1.display_account()
account2.display_account()
