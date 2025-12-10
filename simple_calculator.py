def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def main():
    print("=" * 40)
    print("Python Calculator")
    print("=" * 40)

    while True:
        print("\nOperations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == '6':
            print("Thank you for using the calculator!")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
            elif choice == '5':
                result = power(num1, num2)
                print(f"\n{num1} ^ {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()