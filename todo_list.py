from task import Task

class Todo_List:

    def __init__(self):
        self.tasks = []
    
    def show_tasks(self):
        if not self.tasks:
            print("Tasks are empty")
            return
        for index, task in enumerate(self.tasks):
            print(f"#{index + 1}: {task}")
    
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def delete_task(self, index):
        removed_task = self.tasks.pop(index - 1)
        print(f"task: {removed_task} was removed")

    def complete_task(self, index):
        task = self.tasks[index - 1]
        task.mark_completed()

