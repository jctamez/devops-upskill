# main.py

import calculator

def main():
    print("Simple Calculator")
    
    while True:
        print("\nOptions:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '5':
            print("Exiting...")
            break
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            result = calculator.add(num1, num2)
        elif choice == '2':
            result = calculator.subtract(num1, num2)
        elif choice == '3':
            result = calculator.multiply(num1, num2)
        elif choice == '4':
            try:
                result = calculator.divide(num1, num2)
            except ValueError as e:
                print(e)
                continue
        else:
            print("Invalid option. Try again.")
            continue
        
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()
