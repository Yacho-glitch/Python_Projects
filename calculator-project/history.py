# This file saves calculation history

def save_history(history_list):
    file = open('history.txt', 'w')

    for item in history_list:
        file.write(item + "\n")

    file.close()


