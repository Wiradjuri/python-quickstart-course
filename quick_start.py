#!/usr/bin/env python3
"""
Python QuickStart Course - Quick Start Script
This script helps you get started with the course immediately!
"""

import os
import sys

def print_banner():
    """Print a welcome banner"""
    print("=" * 60)
    print("🐍 PYTHON QUICKSTART COURSE 🐍")
    print("=" * 60)
    print("Welcome to the fastest way to learn Python!")
    print("This script will help you get started immediately.\n")

def check_python_version():
    """Check if Python version is suitable"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected - Perfect!")
        return True
    else:
        print(f"⚠️  Python {version.major}.{version.minor}.{version.micro} detected")
        print("   Recommended: Python 3.6 or higher")
        return False

def show_course_structure():
    """Display the course structure"""
    print("\n📚 COURSE STRUCTURE:")
    print("├── 📖 lessons/")
    print("│   ├── 01-hello-python/     (10 min)")
    print("│   ├── 02-variables-types/  (10 min)")
    print("│   └── ... more lessons")
    print("├── 🚀 projects/")
    print("│   ├── calculator/")
    print("│   ├── todo-app/")
    print("│   └── data-analyzer/")
    print("├── 📋 cheatsheet.md")
    print("└── 📚 resources.md")

def show_quick_options():
    """Show quick start options"""
    print("\n🚀 QUICK START OPTIONS:")
    print("1. Start with Lesson 1 (Recommended)")
    print("2. Try Interactive Lesson 1")
    print("3. Jump to Calculator Project")
    print("4. View Python Cheatsheet")
    print("5. Test Python Installation")
    print("6. Exit")

def run_lesson_1():
    """Interactive Python Learning Experience - Complete Course"""
    print("\n🎓 WELCOME TO INTERACTIVE PYTHON LEARNING!")
    print("=" * 60)
    print("This is your complete Python learning journey.")
    print("We'll teach you Python step by step with hands-on activities!")
    print("=" * 60)
    
    # Lesson 1: Hello Python
    print("\n📚 LESSON 1: Hello Python & Basic Syntax")
    print("-" * 50)
    print("Let's start with your very first Python program!")
    print("\nIn Python, we use print() to display text on the screen.")
    print("Here's the most famous program in programming:")
    
    input("\nPress Enter to see the code...")
    
    print("\n💻 CODE:")
    print('print("Hello, World!")')
    print('print("Welcome to Python!")')
    
    input("\nPress Enter to run this code...")
    
    print("\n🚀 OUTPUT:")
    print("Hello, World!")
    print("Welcome to Python!")
    
    print("\n✅ Congratulations! You just learned:")
    print("   • How to use print() function")
    print("   • How to display text with quotes")
    print("   • Your first Python program!")
    
    # Activity 1
    print("\n🏋️ ACTIVITY 1: Try it yourself!")
    print("Let's make it interactive. We'll ask for your name.")
    
    while True:
        try_activity = input("\nWould you like to try the activity? (y/n): ").lower()
        if try_activity in ['y', 'yes']:
            print("\n💻 Here's the code we'll run:")
            print('name = input("What\'s your name? ")')
            print('print("Hello, " + name + "!")')
            
            input("\nPress Enter to run it...")
            
            # Run the interactive code
            name = input("What's your name? ")
            print("Hello, " + name + "!")
            
            print(f"\n🎉 Excellent, {name}! You just learned:")
            print("   • How to get user input with input()")
            print("   • How to store data in variables")
            print("   • How to combine text with +")
            break
        elif try_activity in ['n', 'no']:
            print("No problem! Let's continue to the next lesson.")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")
    
    # Progress to Lesson 2
    print("\n" + "=" * 60)
    print("📚 LESSON 2: Variables & Data Types")
    print("-" * 50)
    print("Now let's learn about storing different types of information!")
    
    while True:
        continue_lesson = input("\nReady for Lesson 2? (y/n): ").lower()
        if continue_lesson in ['y', 'yes']:
            run_lesson_2_interactive()
            break
        elif continue_lesson in ['n', 'no']:
            print("That's okay! You can continue anytime.")
            print("📖 To review what you learned, check: lessons/01-hello-python/README.md")
            input("\nPress Enter to return to main menu...")
            return
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def run_lesson_2_interactive():
    """Interactive Lesson 2: Variables & Data Types"""
    print("\nIn Python, we can store different types of information:")
    print("   • Text (strings) - like names and messages")
    print("   • Numbers (integers) - like age and count")
    print("   • Decimal numbers (floats) - like prices and measurements")
    print("   • True/False values (booleans) - like yes/no questions")
    
    input("\nPress Enter to see examples...")
    
    print("\n💻 CODE EXAMPLES:")
    print('name = "Alice"        # String (text)')
    print('age = 25              # Integer (whole number)')
    print('height = 5.6          # Float (decimal)')
    print('is_student = True     # Boolean (True/False)')
    
    print("\n🚀 Let's see what these look like:")
    name = "Alice"
    age = 25
    height = 5.6
    is_student = True
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}")
    print(f"Is student: {is_student}")
    
    # Activity 2
    print("\n🏋️ ACTIVITY 2: Create your own variables!")
    
    while True:
        try_activity = input("\nWould you like to try creating variables? (y/n): ").lower()
        if try_activity in ['y', 'yes']:
            print("\nLet's create variables about you!")
            
            user_name = input("Enter your name: ")
            user_age = input("Enter your age: ")
            user_city = input("Enter your city: ")
            
            print(f"\n🎉 Great! Here are your variables:")
            print(f'user_name = "{user_name}"')
            print(f'user_age = {user_age}')
            print(f'user_city = "{user_city}"')
            
            print(f"\nAnd here's how we use them:")
            print(f"Hello {user_name}! You are {user_age} years old and live in {user_city}.")
            
            print("\n✅ You just learned:")
            print("   • How to create different types of variables")
            print("   • How to use variables in sentences")
            print("   • The difference between text and numbers")
            break
        elif try_activity in ['n', 'no']:
            print("No problem! Let's continue.")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")
    
    # Progress to Calculator Project
    print("\n" + "=" * 60)
    print("🚀 PROJECT TIME: Build a Calculator!")
    print("-" * 50)
    print("Now let's use what you learned to build something real!")
    
    while True:
        continue_project = input("\nReady to build a calculator? (y/n): ").lower()
        if continue_project in ['y', 'yes']:
            run_calculator_tutorial()
            break
        elif continue_project in ['n', 'no']:
            print("That's okay! You've learned a lot already.")
            print("📖 To review: check lessons/02-variables-types/README.md")
            input("\nPress Enter to return to main menu...")
            return
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def run_calculator_tutorial():
    """Interactive Calculator Building Tutorial"""
    print("\n🧮 Let's build a calculator step by step!")
    print("We'll use everything you've learned so far.")
    
    print("\nStep 1: Get two numbers from the user")
    print("Step 2: Choose what operation to do (+, -, *, /)")
    print("Step 3: Calculate and show the result")
    
    input("\nPress Enter to start building...")
    
    print("\n💻 Here's our calculator code:")
    print('num1 = float(input("Enter first number: "))')
    print('num2 = float(input("Enter second number: "))')
    print('operation = input("Choose (+, -, *, /): ")')
    print('')
    print('if operation == "+":')
    print('    result = num1 + num2')
    print('elif operation == "-":')
    print('    result = num1 - num2')
    print('elif operation == "*":')
    print('    result = num1 * num2')
    print('elif operation == "/":')
    print('    result = num1 / num2')
    print('')
    print('print(f"Result: {num1} {operation} {num2} = {result}")')
    
    input("\nPress Enter to try your calculator...")
    
    # Run the calculator
    print("\n🚀 YOUR CALCULATOR IS RUNNING:")
    print("=" * 40)
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero!")
                input("\nPress Enter to return to main menu...")
                return
        else:
            print("Invalid operation!")
            input("\nPress Enter to return to main menu...")
            return
        
        print(f"Result: {num1} {operation} {num2} = {result}")
        
        print("\n🎉 CONGRATULATIONS! You just built a working calculator!")
        print("✅ You learned:")
        print("   • How to get user input")
        print("   • How to work with numbers")
        print("   • How to make decisions with if/elif")
        print("   • How to perform calculations")
        print("   • How to handle errors")
        
        print("\n🚀 WHAT'S NEXT?")
        print("You now know the basics of Python! Here are your next steps:")
        print("   1. Practice with more exercises")
        print("   2. Learn about loops and lists")
        print("   3. Build more projects")
        print("   4. Explore Python libraries")
        
        print("\n📚 Resources for continued learning:")
        print("   • Check out resources.md for more tutorials")
        print("   • Use cheatsheet.md as a quick reference")
        print("   • Try building the advanced calculator project")
        
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    input("\nPress Enter to return to main menu...")

def run_interactive_lesson_1():
    """Run the interactive lesson 1"""
    print("\n🎯 Running Interactive Lesson 1...")
    print("=" * 40)
    
    # Import and run the interactive.py example
    lesson_path = "lessons/01-hello-python/interactive.py"
    if os.path.exists(lesson_path):
        print("Executing: lessons/01-hello-python/interactive.py")
        print("-" * 40)
        exec(open(lesson_path).read())
        print("-" * 40)
        print("✅ Great! You just created an interactive Python program!")
        print("✅ This program asked for your name and greeted you personally!")
        print("\n📖 Next steps:")
        print("   1. Try modifying the code to ask different questions")
        print("   2. Complete the lesson exercises")
        print("   3. Move on to Lesson 2: Variables & Data Types")
        
        input("\nPress Enter to continue...")
    else:
        print("❌ Interactive lesson file not found. Make sure you're in the course directory.")

def run_calculator():
    """Run the calculator project"""
    print("\n🧮 Running Calculator Project...")
    print("=" * 40)
    
    calc_path = "projects/calculator/simple_calculator.py"
    if os.path.exists(calc_path):
        print("Executing: projects/calculator/simple_calculator.py")
        print("-" * 40)
        exec(open(calc_path).read())
        print("-" * 40)
        print("✅ Calculator project completed!")
        print("📖 To learn more, check: projects/calculator/README.md")
        
        input("\nPress Enter to continue...")
    else:
        print("❌ Calculator project not found. Make sure you're in the course directory.")

def show_cheatsheet():
    """Display key parts of the cheatsheet"""
    print("\n📋 PYTHON CHEATSHEET (Quick Reference):")
    print("=" * 50)
    print("# Print to screen")
    print('print("Hello, World!")')
    print()
    print("# Variables")
    print('name = "Alice"')
    print('age = 25')
    print()
    print("# Get user input")
    print('name = input("What\'s your name? ")')
    print()
    print("# If statements")
    print('if age >= 18:')
    print('    print("Adult")')
    print('else:')
    print('    print("Minor")')
    print()
    print("📖 For complete cheatsheet, see: cheatsheet.md")
    
    input("\nPress Enter to continue...")

def test_python():
    """Test Python installation with a simple program"""
    print("\n🧪 TESTING PYTHON INSTALLATION:")
    print("=" * 40)
    
    try:
        # Test basic operations
        print("✅ Basic math: 2 + 2 =", 2 + 2)
        print("✅ String operations: 'Hello' + ' World' =", 'Hello' + ' World')
        print("✅ Lists: [1, 2, 3] =", [1, 2, 3])
        print("✅ Dictionaries: {'name': 'Python'} =", {'name': 'Python'})
        
        # Test imports
        import random
        print("✅ Random module: random number =", random.randint(1, 10))
        
        import datetime
        print("✅ Datetime module: current time =", datetime.datetime.now().strftime("%H:%M:%S"))
        
        print("\n🎉 Python installation is working perfectly!")
        
    except Exception as e:
        print(f"❌ Error testing Python: {e}")
    
    input("\nPress Enter to continue...")

def main():
    """Main function"""
    print_banner()
    
    # Check Python version
    check_python_version()
    
    # Show course structure
    show_course_structure()
    
    while True:
        show_quick_options()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                run_lesson_1()
            elif choice == "2":
                run_interactive_lesson_1()
            elif choice == "3":
                run_calculator()
            elif choice == "4":
                show_cheatsheet()
            elif choice == "5":
                test_python()
            elif choice == "6":
                print("\n👋 Happy coding! Start with lessons/01-hello-python/")
                print("🐍 Remember: The best way to learn Python is by coding!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-6.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy coding!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
