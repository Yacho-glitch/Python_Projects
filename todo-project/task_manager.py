from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, date):
        new_task = Task(title, date)
        self.tasks.append(new_task)

    def show_all_tasks(self):
        if not self.tasks: # OR if len(self.tasks) == 0
            print("No tasks yet!")
            return
        else:
            print("-----Tasks📝-----")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task.show()}")
            print("---------------------")

if __name__ == "__main__":
    manager = TaskManager()
    manager.show_all_tasks()

    manager.add_task("Learn Java", "2027-18-03")
    manager.add_task("Learn French", "2023-05-05")

    manager.show_all_tasks()

    # print(f"Number of tasks: {len(manager.tasks)}")
    # print(manager.tasks[0].show())