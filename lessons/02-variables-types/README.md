# Lesson 2: Variables & Data Types 📦

**Time: 10 minutes | Difficulty: Beginner**

Variables are like labeled boxes that store information. In this lesson, you'll learn how to create and use variables with different types of data.

## 🎯 What You'll Learn

- What variables are and how to create them
- Different data types (text, numbers, true/false)
- How to work with variables
- Converting between data types

## 🚀 Let's Start Coding!

### Step 1: Creating Variables

Variables store data that you can use later:

```python
# Creating variables
name = "Alice"
age = 25
height = 5.6
is_student = True

# Using variables
print("Name:", name)
print("Age:", age)
print("Height:", height, "feet")
print("Is student:", is_student)
```

**Key Points:**
- Variable names should be descriptive
- Use `=` to assign values
- No need to declare the type - Python figures it out!

### Step 2: Data Types in Python

Python has several built-in data types:

```python
# String (text)
message = "Hello, Python!"
favorite_food = 'Pizza'  # Single or double quotes work

# Integer (whole numbers)
score = 100
temperature = -5

# Float (decimal numbers)
price = 19.99
pi = 3.14159

# Boolean (True or False)
is_sunny = True
is_raining = False

# Check the type of a variable
print(type(message))    # <class 'str'>
print(type(score))      # <class 'int'>
print(type(price))      # <class 'float'>
print(type(is_sunny))   # <class 'bool'>
```

### Step 3: Working with Variables

```python
# You can change variable values
counter = 0
print("Counter:", counter)  # Counter: 0

counter = 10
print("Counter:", counter)  # Counter: 10

# Math with variables
x = 5
y = 3
sum_result = x + y
print("Sum:", sum_result)   # Sum: 8

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)  # Full name: John Doe
```

### Step 4: Getting User Input (Always Strings!)

```python
# input() always returns a string
user_input = input("Enter a number: ")
print("You entered:", user_input)
print("Type:", type(user_input))  # Always <class 'str'>

# Converting strings to numbers
number = int(user_input)  # Convert to integer
print("As number:", number)
print("Type:", type(number))  # <class 'int'>
```

### Step 5: Type Conversion

```python
# Converting between types
age_str = "25"
age_num = int(age_str)      # String to integer
print("Age as number:", age_num)

price_str = "19.99"
price_num = float(price_str)  # String to float
print("Price as number:", price_num)

score = 95
score_str = str(score)      # Number to string
print("Score as string:", score_str)

# Boolean conversions
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False (empty string)
print(bool("hi"))   # True (non-empty string)
```

## 💡 Variable Naming Rules

✅ **Good variable names:**
```python
user_name = "Alice"
total_score = 100
is_valid = True
```

❌ **Avoid these:**
```python
x = "Alice"        # Not descriptive
2name = "Bob"      # Can't start with number
user-name = "Eve"  # No hyphens (use underscore)
```

## 🏋️ Practice Exercise

Create a simple calculator that:
1. Asks the user for two numbers
2. Converts them to floats
3. Calculates and displays: sum, difference, product, and quotient

**Example Output:**
```
Enter first number: 10
Enter second number: 3
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.333333333333333
```

**Solution:** Check `calculator.py` if you get stuck.

## ✅ What You've Learned

- ✅ How to create and use variables
- ✅ Different data types: strings, integers, floats, booleans
- ✅ Converting between data types
- ✅ Getting user input and converting it
- ✅ Good variable naming practices

## 🚀 Next Step

**[👉 Continue to Lesson 3: Control Flow](../03-control-flow/README.md)**

---

*You're building a solid foundation! Keep going! 🐍✨*
