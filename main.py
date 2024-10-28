from  task import Task
from todo_list import Todo_List

todo_list = Todo_List()

while True:
    print("1. show tasks")
    print("2. create task")
    print("3. complete task")
    print("4. delete task")
    print("5. exit")

    choice = input("Choose an option: ")

    if choice == "1":
        todo_list.show_tasks()
    if choice == "2":
        description = input("please input task description: ")
        todo_list.add_task(description)
    if choice == "3":
        try:
            index = int(input("Please input number of task to be completed: "))
            todo_list.complete_task(index)
        except ValueError:
            print("Please enter a valid number")
    if choice == "4":
        try:
            index = int(input("Please input number of task to be deleted: "))
            todo_list.delete_task(index)
        except ValueError:
            print("Please enter a valid number")
    if choice == "5":
        exit()
