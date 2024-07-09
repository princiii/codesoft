tasks=[]

def add_task():
    t=input("Enter your task here: ")
    tasks.append(t)
    print(f"Your task {t} has been added !")

def delete_task():
    display_task()
    try:
        del_task=int(input("Enter number you want to delete: "))
        if del_task > 0 and del_task <= len(tasks):
            deleted_task = tasks.pop(del_task-1)
        print(f"Task {deleted_task} has been removed !")
        #else:
            #print("Invalid task number! Please enter a valid number.")
    except ValueError:
        print("Invalid Input !")

def display_task():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


if __name__ == "__main__":
    while True:
        print("TO DO LIST !!")
        print("--------------")
        print("What do you want to do today?")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Display the list")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                delete_task()
            elif choice == 3:
                display_task()
            elif choice == 4:
                print("Goodbye! Visit again!")
                break
            else:
                print("Invalid Input! Please try again.")
        except ValueError:
            print("Invalid Input! Please enter a number.")