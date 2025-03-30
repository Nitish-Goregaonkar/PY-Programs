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


