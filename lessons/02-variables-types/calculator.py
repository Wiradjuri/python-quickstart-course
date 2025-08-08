# Exercise Solution: Simple Calculator
# This program asks for two numbers and performs basic math operations

print("=== Simple Calculator ===")

# Get user input
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

# Convert strings to floats
num1 = float(first_number)
num2 = float(second_number)

# Perform calculations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Display results
print("\nResults:")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
