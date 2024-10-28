from  task import Task
from todo_list import Todo_List

todo_list = Todo_List()

todo_list.add_task("Buy groceries")
todo_list.add_task("Finish coding project")

todo_list.show_tasks()

todo_list.delete_task(1)

todo_list.show_tasks()

todo_list.complete_task(1)

todo_list.show_tasks()