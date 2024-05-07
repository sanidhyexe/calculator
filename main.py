
print("/////////////////////////////////////////////////////////////////////////////////")
print()
print("--------------------------Welcome to Calculator app------------------------------")
print()

# This is the main function that will call the calculate function.
def main():
    calculate()

# This function handles the calculator operations
def calculate():
    while True:
        # Get user input for two numbers
        a = int(input("Enter the First Number : "))
        b = int(input("Enter the Second Number : "))
        print()

        # Display the available operations
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Exit")
        print()

        # Get user input for the operation choice
        choice = int(input("Enter your choice : "))

        # Perform the selected operation
        if choice == 1:
            nadd(a, b)
            print()
        elif choice == 2:
            nsubtract(a, b)
            print()
        elif choice == 3:
            ndivide(a, b)
            print()
        elif choice == 4:
            nmulti(a, b)
            print()
        else:
            # Exit the loop if the user chooses to exit
            break

# This function performs addition operation
def nadd(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

# This function performs subtraction operation
def nsubtract(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")

# This function performs division operation
def ndivide(a, b):
    result = a / b
    print(f"{a} / {b} = {result}")

# This function performs multiplication operation
def nmulti(a, b):
    result = a * b
    print(f"{a} x {b} = {result}")

# This block of code will run the main function if the script is executed directly
try:
    if __name__ == "__main__":
        main()
        print()
except:
    # Handle any exceptions that occur during execution
    print()
    print("Something went wrong")
    print()
    print("Please try again")
    print()