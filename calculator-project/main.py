# This file runs the program

from calculator import Calculator
from utils import get_number
from history import save_history, load_history

calc = Calculator()

old_history = load_history()

for item in old_history:
    calc.history.append(item)

while True:
    print("\n===== Calculator =====")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Show History")
    print("6. Quit")

    choice = input("\nChoose (1-6): ")

    if (choice == 1):
        a = get_number("Enter first number : ")
        b = get_number("Enter second number : ")
        result = calc.add(a, b)
        print(f"\n✅ Result: {result}")

    elif (choice == 2):
        a = get_number("Enter first number : ")
        b = get_number("Enter second number : ")
        result = calc.subtract(a, b)
        print(f"\n✅ Result: {result}")

    elif (choice == 3):
        a = get_number("Enter first number : ")
        b = get_number("Enter second number : ")
        result = calc.multiply(a, b)
        print(f"\n✅ Result: {result}")

    elif (choice == 4):
        a = get_number("Enter first number : ")
        b = get_number("Enter second number : ")
        result = calc.divide(a, b)
        print(f"\n✅ Result: {result}")

    elif (choice == 5):
        calc.show_history()

    elif (choice == 6):
        save_history(calc.history)
        print("\n👋 Goodbye! History saved.")
        break

    else:
        print("\n❌ Invalid choice! Please type 1-6.")

