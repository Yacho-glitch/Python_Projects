def get_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input
        else:
            print("❌ Cannot be empty!")
            continue

def get_date():
    while True:
        user_date = input("Enter date (YYYY-MM-DD) : ")

        if (len(user_date) != 10):
            print("❌ Must be 10 characters!")
            continue
        
        if (user_date[4] != "-" or user_date[7] != "-"):
            print("❌ Must use - as separator!")
            continue

        try:
            year = int(user_date[0:4])
            month = int(user_date[5:7])
            day = int(user_date[8:10])
        except ValueError:
            print("❌ Year, month, day must be numbers!")
            continue

        if (month < 1 or month > 12):
            print("❌ Month must be 01-12!")
            continue

        if (day < 1 or day > 31):
            print("❌ Day must be 01-31!")
            continue

        return user_date

def confirm(question):
    while True:
        answer = input(f"{question}? (y/n) : ")
        answer = answer.lower().strip()

        if (answer == "y" or answer == "yes"):
            return True
        elif (answer == "n" or answer == "no"):
            return False
        else:
            print("❌ Please type (y/n)")

if __name__ == "__main__":
    result = confirm("Are you sure")
    print(f"User said: {result}")
            


