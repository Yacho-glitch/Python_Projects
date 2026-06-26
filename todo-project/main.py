from task_manager import TaskManager
from storage import save_tasks, load_tasks
from utils import get_string, get_date, confirm, clear_screen

manager = TaskManager()

old_tasks = load_tasks()
for task in old_tasks:
    manager.tasks.append(task)

while True:
    clear_screen()

    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("\nChoose (1-5): ")

    if (choice == "1"):
        title = get_string("Enter task title: ")
        date = get_date()
        manager.add_task(title, date)
        print("\n✅ Task added!")

    elif (choice == "2"):
        manager.show_all_tasks()

    elif (choice == "3"):
        manager.show_all_tasks()
        index = int(input("Which task number? ")) - 1
        manager.mark_done(index)
        print("\n✅ Task marked as done!")

    elif (choice == "4"):
        manager.show_all_tasks()
        index = int(input("WHich task number? "))

        if confirm("Are you sure you want to delete"):
            manager.delete_task(index)
            print("\n✅ Task deleted!")

    elif (choice == "5"):
        if confirm("Save before quitting"):
            save_tasks(manager.get_tasks())
        print("\n👋 Goodbye!")
        break

    else:
        print("\n❌ Invalid choice! Please type 1-5.")