# task.py

class Task:
    def __init__(self, title, date):
        self.title = title
        self.date = date
        self.done = False # New task = not done

    def mark_done(self):
        self.done = True

    def mark_undone(self):
        self.done = False

    def show(self):
        if (self.done):
            return f"[X] {self.title} ({self.date})"
        else:
            return f"[ ] {self.title} ({self.date})"

    
# task = Task("Buy milk", "2025-05-12")
# task.mark_done()             
# print(task.show())

# task2 = Task("reading book", "2023-08-01")
# print(task2.show())

# task3 = Task("Playing video game", "2015-05-05")
# task3.mark_undone()
# print(task3.show())