def get_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input
        else:
            print("❌ Cannot be empty!")
            continue