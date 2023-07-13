def list():
    
    mylist = ["Complete Python", "Build To do List"];
    print(mylist);

    print(mylist[1]);

list()

def append():
    
    mylist1 = ["Complete Python", "Build To do List"];
    print(mylist1);
    
    mylist1.append("learn Django");
    print(mylist1);

append()


def insert():
    
    mylist2 = ["Complete Pyon", "Build To do List"];
    print(mylist2);
    
    mylist2.insert(1, "learn Django");
    print(mylist2);
insert()


def show_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def mark_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()







