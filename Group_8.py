# Task: Display Python reserved keywords
import keyword

def display_keywords():
    print("Python reserved keywords are:")
    for kw in keyword.kwlist:
        print(kw)

display_keywords()
  
# Task: Convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius = float(input("Enter temperature in Celsius: "))
print(f"{celsius}°C is equivalent to {celsius_to_fahrenheit(celsius)}°F")

# Task: Count the number of vowels in a given string using a loop
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage:
text = input("Enter a string: ")
print(f"The number of vowels in '{text}' is: {count_vowels(text)}")


# string_utils.py
def reverse_string(input_string):
    return input_string[::-1]

# Task: Use the reverse string function from a module


text = input("Enter a string to reverse: ")
print(f"The reversed string is: {reverse_string(text)}")

# Task: Implement a Library class with methods to add, remove, and display books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' added to the library.")

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"'{book_name}' removed from the library.")
        else:
            print(f"'{book_name}' not found in the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

# Example usage:
library = Library()
library.add_book("1984")
library.add_book("To Kill a Mockingbird")
library.display_books()
library.remove_book("1984")
library.display_books()


# Task: Write a list of dictionaries into a JSON file and read it back
import json

def write_to_json(file_name, data):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)

def read_from_json(file_name):
    with open(file_name, 'r') as json_file:
        return json.load(json_file)

# Example usage:
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

file_name = "data.json"
write_to_json(file_name, data)

loaded_data = read_from_json(file_name)
print("Loaded data from JSON file:", loaded_data)


# Task: Update the status of an order in a database based on the order ID
import sqlite3

def update_order_status(order_id, new_status):
    connection = sqlite3.connect('orders.db')  # Adjust the database as needed
    cursor = connection.cursor()

    cursor.execute("UPDATE orders SET status = ? WHERE id = ?", (new_status, order_id))
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Order {order_id} status updated to '{new_status}'.")
    else:
        print(f"No order found with ID {order_id}.")

    connection.close()

# Example usage:
order_id = int(input("Enter the order ID: "))
new_status = input("Enter the new status: ")
update_order_status(order_id, new_status)


# Task: Calculate the z-score of a list of numbers
import statistics

def calculate_z_scores(data):
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    z_scores = [(x - mean) / std_dev for x in data]
    return z_scores

# Example usage:
data = [10, 20, 30, 40, 50]
print("Z-scores:", calculate_z_scores(data))


# Task: Raise a custom exception if withdrawal exceeds balance
class InsufficientFundsException(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException("Withdrawal amount exceeds balance.")
        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}.")

# Example usage:
account = BankAccount(100)
account.deposit(50)

try:
    account.withdraw(200)  # This will raise an exception
except InsufficientFundsException as e:
    print(e)



