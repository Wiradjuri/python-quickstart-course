# Advanced Interactive Calculator
# This calculator can perform multiple operations and handles errors gracefully

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def get_operation():
    """Get a valid operation from user input"""
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = input("Choose operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        else:
            print("Please enter a valid operation (+, -, *, /)")

def calculate(num1, num2, operation):
    """Perform the calculation and return the result"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return None  # Division by zero
        return num1 / num2

def main():
    """Main calculator program"""
    print("=== Python Calculator ===")
    print("Perform calculations with +, -, *, /")
    print("Type 'quit' at any time to exit\n")
    
    while True:
        try:
            # Get first number
            num1 = get_number("Enter first number: ")
            
            # Get second number
            num2 = get_number("Enter second number: ")
            
            # Get operation
            operation = get_operation()
            
            # Perform calculation
            result = calculate(num1, num2, operation)
            
            # Display result
            if result is None:
                print("Error: Cannot divide by zero!")
            else:
                print(f"Result: {num1} {operation} {num2} = {result}")
            
            # Ask if user wants to continue
            print()
            continue_calc = input("Continue? (y/n): ").lower()
            if continue_calc != 'y' and continue_calc != 'yes':
                break
            print()  # Add blank line for readability
            
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue
    
    print("Thanks for using the calculator!")

# Run the calculator
if __name__ == "__main__":
    main()
