import json
import os

# File where tasks will be saved
FILE_NAME = "todo.json"

# Load existing tasks or create empty list
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

# Add new task
def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks()
    print("✅ Task added!")

# View all tasks
def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")

# Mark task completed
def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark complete: ")) - 1
        tasks[task_num]["completed"] = True
        save_tasks()
        print("✅ Task marked complete!")
    except:
        print("⚠️ Invalid number.")

# Delete task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        tasks.pop(task_num)
        save_tasks()
        print("🗑️ Task deleted!")
    except:
        print("⚠️ Invalid number.")

# Main CLI Loop
while True:
    print("\n📝 To-Do App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
