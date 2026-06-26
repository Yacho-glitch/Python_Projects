from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self,title, date):
        new_task = Task(title, date)
        self.tasks.append(new_task)

if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Learn Java", "2027-18-03")
    manager.add_task("Learn French", "2023-05-05")

    print(f"Number of tasks: {len(manager.tasks)}")
    print(manager.tasks[0].show())