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
        pass

    