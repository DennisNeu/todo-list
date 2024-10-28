from task import Task

class Todo_List:

    def __init__(self):
        self.tasks = []
    
    def show_tasks(self):
        if not self.tasks:
            print("Tasks are empty")
            return
        for task in self.tasks:
            print(task)
    
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        