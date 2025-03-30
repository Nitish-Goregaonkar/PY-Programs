# Book class with user input
class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
    
    def display_details(self):
        print(f"Book Name: {self.name}, Author: {self.author}, Price: {self.price}")

name = input("Enter book name: ")
author = input("Enter author name: ")
price = float(input("Enter book price: "))

book = Book(name, author, price)
book.display_details()


# BankAccount class with user input and conditional balance assignment
class BankAccount:
    def __init__(self, account_number, balance=1000):
        self.account_number = account_number
        self.balance = max(balance, 100)
    
    def display_account(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

account_number1 = input("Enter first account number: ")
balance1 = float(input("Enter first account balance: "))


