tasks=[]

def show_tasks():
    if not tasks:
        print("\n NO tasks available. \n")

    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            status="✅" if task['complete'] else"❌"
            print(f"{i+1}.[{status}] {task['name']}")

    print()

def add_task():
    task=input("Enter Task: ")
    tasks.append({"name": task, "complete":False})
    print("Task added!\n")

def mark_complete():
    show_tasks()
    try:
        index=int(input("Enter task number to mark complete: ")) -1
        if 0<=index<len(tasks):
            tasks[index]['complete']=True
            print("Task marked as complete!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    show_tasks()
    try:
        index=int(input("Enter task number to delete: "))-1
        if 0<=index<len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Deleted task: {delete_task['name']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("====To-Do List ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice =="1":
            add_task()
        elif choice=="2":
            show_tasks()
        elif choice=="3":
            mark_complete()
        elif choice=="4":
            delete_task()
        elif choice=="5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__=="__main__":
    main()