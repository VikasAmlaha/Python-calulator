# Functions for the calculator
def display_menu():
    print("Press 1 and enter to add two numbers")
    print("Press 2 and enter to subtract two numbers")
    print("Press 3 and enter to multiply two numbers")
    print("Press 4 and enter to divide two numbers")
    print("Press 5 and enter to exit")

def add(first_number, second_number):
    print("Result: " + str(first_number + second_number))

def sub(first_number, second_number):
    print("Result: " + str(first_number - second_number))

def multiply(first_number, second_number):
    print("Result: " + str(first_number * second_number))

def divide(first_number, second_number):
    if second_number != 0:
        print("Result: " + str(first_number / second_number))
    else:
        print("Error: Cannot divide by zero.")

# Main calculator function
def calculator():
    while True:  # Infinite loop, will break when user chooses to exit
        display_menu()
        choice = int(input("Choose an option (1-5): "))
    
        if choice == 1:
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            add(first_number, second_number)
        elif choice == 2:
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            sub(first_number, second_number)
        elif choice == 3:
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            multiply(first_number, second_number)
        elif choice == 4:
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            divide(first_number, second_number)
        elif choice == 5:
            print("Thank you for using the calculator!")
            break  # Exit the loop and stop the program
        else:
            print("Invalid option, please try again.")

# Run the calculator
calculator()
