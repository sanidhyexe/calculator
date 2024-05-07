

print()
print("Welcome to Calculator app")

def nadd(a,b):
    result = a + b
    print(f"{a} + {b} = {result}")
def nsubtract(a,b):
    result = a - b
    print(f"{a} - {b} = {result}")
def ndivide(a,b):
    result = a / b
    print(f"{a} / {b} = {result}")
def nmulti(a,b):
    result = a * b
    print(f"{a} x {b} = {result}")
def calculate():
    while True:
        a = int(input("Enter the First Number : "))
        b = int(input("Enter the Second Number : "))
        print()
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Exit")
        print()
        choice = int(input("Enter your choice : "))
        if choice == 1:
            nadd(a,b)
            print()
        elif choice == 2:
            nsubtract(a,b)
            print()
        elif choice == 3:
            ndivide(a,b)
            print()
        elif choice == 4:
            nmulti(a,b)
            print()
        else:
            break
def main():
    calculate()
try:
     if __name__ == "__main__":
        main()
        print()
except:
     print()
     print("Something went wrong")
     print()
     print("Please try again")
     print()