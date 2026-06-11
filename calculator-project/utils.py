# This files has many Helper tools

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def get_number(prompt):
    while True:
        user_input = input(prompt)
        if is_number(user_input):
            number = float(user_input)

            if number.is_integer():
                return int(number)
            return number
        else:
            print("❌ That's not a number! Try again.")



# Tests only run when you type: py utils.py
if __name__ == "__main__":
    # Test is_number
    print(is_number("5"))       # True
    print(is_number("3.14"))    # True
    print(is_number("-2"))      # True
    print(is_number("abc"))     # False
    print(is_number(""))        # False
    print(is_number("5abc"))    # False

    # Test get_number
    print("\n--- Testing get_number ---")
    num = get_number("Enter a number : ")
    print(f"You entered : {num}")
    print(f"Type : {type(num)}")