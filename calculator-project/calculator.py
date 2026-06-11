# This file it's about the calculator class and its methods

class Calculator:

    def __init__(self):
        # Create an empty list to store calculations
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return f"{a} + {b} = {result}"
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return f"{a} - {b} = {result}"
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return f"{a} * {b} = {result}"
    
    def divide(self, a, b):
        if (b == 0):
            return "Error: Cannot divide by zero!"
        else:
            result = a / b 
            self.history.append(f"{a} / {b} = {result}")
            return f"{a} / {b} = {result}"
        
    def show_history(self):
        if len(self.history) == 0:
            print("No calculations yet!")
            return
        else:
            print("-----History📝-----")
            for index, item in enumerate(self.history, start=1):
                print(f"{index}. {item}")
            print("--------------------")
        

calc = Calculator()
print(calc.divide(4,6))
print(calc.add(2,2))
print(calc.multiply(2,6))
print(calc.subtract(-1,5))
calc.show_history()

print("---------")

calcTwo = Calculator()
print(calcTwo.divide(5,0))
calcTwo.show_history()