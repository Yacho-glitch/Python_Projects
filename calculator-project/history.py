# This file saves calculation history

def save_history(history_list):
    file = open('history.txt', 'w')

    for item in history_list:
        file.write(item + "\n")

    file.close()


def load_history():
    try:
        file = open('history', 'r')
        lines = file.readlines() # Read all lines
        file.close()

        clean_list = []
        for line in file:
            clean_line = line.strip()
            clean_list.append(clean_list)

        return clean_list
     
    except FileNotFoundError:
        return []