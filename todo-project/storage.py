import json

def save_tasks(tasks_list):
    dicts_list = []

    for task in tasks_list:
        task_dict = {
            "title" : task.title,
            "date" : task.date,
            "done" : task.done
        }

        dicts_list.append(task_dict)

    with open("tasks.json", "w") as file:
        json.dump(dicts_list, file, indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            dicts_list = json.load(file)

            tasks_list = []

            for task_dict in dicts_list:
                task = Task(task_dict["title"], task_dict["date"])
                task.done = task_dict["done"]
                tasks_list.append(task)

            return tasks_list    
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    from task import Task

    task1 = Task("Buy milk", "2025-06-12")
    task2 = Task("Learn Python", "2024-03-04")
    task2.mark_done()

    tasks = [task1, task2]
    save_tasks(tasks)
    print("Saved! Check tasks.json file.")

    loaded = load_tasks()
    print("\nLoaded tasks:")
    for task in loaded:
        print(task.show())