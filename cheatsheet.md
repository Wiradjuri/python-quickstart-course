# Python QuickStart Cheatsheet 📋

**Quick reference for the most common Python patterns you'll use every day.**

## 🖨️ Output & Input

```python
# Print to screen
print("Hello, World!")
print("Name:", name)
print(f"Hello, {name}!")  # f-string (modern way)

# Get user input (always returns string)
name = input("What's your name? ")
age = int(input("How old are you? "))  # Convert to number
```

## 📦 Variables & Data Types

```python
# Variables
name = "Alice"          # String
age = 25               # Integer
height = 5.6           # Float
is_student = True      # Boolean

# Check type
print(type(name))      # <class 'str'>

# Convert types
age_str = str(25)      # Number to string
age_num = int("25")    # String to number
price = float("19.99") # String to decimal
```

## 🔀 Control Flow

```python
# If statements
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# For loops
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for item in ["a", "b", "c"]:
    print(item)

# While loops
count = 0
while count < 5:
    print(count)
    count += 1
```

## 📝 Lists & Dictionaries

```python
# Lists (ordered collections)
fruits = ["apple", "banana", "orange"]
fruits.append("grape")      # Add item
print(fruits[0])           # First item: "apple"
print(len(fruits))         # Length: 4

# Dictionaries (key-value pairs)
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person["name"])      # "Alice"
person["job"] = "Engineer" # Add new key
```

## 🔧 Functions

```python
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Alice")
print(message)

# Function with default parameter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

## 📁 File Operations

```python
# Write to file
with open("data.txt", "w") as file:
    file.write("Hello, World!")

# Read from file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

## ⚠️ Error Handling

```python
try:
    age = int(input("Enter age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number")
```

## 🧮 Common Operations

```python
# Math
result = 10 + 5    # Addition
result = 10 - 5    # Subtraction
result = 10 * 5    # Multiplication
result = 10 / 5    # Division
result = 10 ** 2   # Power (10²)
result = 10 % 3    # Remainder (1)

# String operations
text = "Hello, World!"
print(text.upper())        # "HELLO, WORLD!"
print(text.lower())        # "hello, world!"
print(text.replace("Hello", "Hi"))  # "Hi, World!"
print(len(text))           # 13

# List operations
numbers = [1, 2, 3, 4, 5]
print(max(numbers))        # 5
print(min(numbers))        # 1
print(sum(numbers))        # 15
```

## 🎯 Quick Patterns

```python
# Check if item in list
if "apple" in fruits:
    print("Found apple!")

# Loop with index
for i, item in enumerate(fruits):
    print(f"{i}: {item}")

# List comprehension (advanced)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Multiple assignment
x, y = 10, 20
name, age = "Alice", 25
```

## 🚀 Import Libraries

```python
# Import entire module
import random
number = random.randint(1, 10)

# Import specific function
from random import randint
number = randint(1, 10)

# Common imports
import os          # Operating system interface
import json        # Work with JSON data
import datetime    # Date and time operations
```

## 💡 Best Practices

- **Use descriptive variable names**: `user_name` not `x`
- **Add comments**: `# This calculates the total`
- **Use f-strings**: `f"Hello, {name}!"` instead of `"Hello, " + name + "!"`
- **Handle errors**: Use try/except for user input
- **Keep functions small**: One task per function
- **Use `with` for files**: Automatically closes files

---

*Keep this handy while coding! 🐍✨*
