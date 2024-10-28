from task import Task
import json
import os

class Todo_List:

    def __init__(self):
        self.tasks = []
        try:
            filename = "tasks.json"
            # Check if the file is empty
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                with open(filename, "r") as file:
                    data = json.load(file)
                    self.tasks = [Task(item["description"]) for item in data]
                    for task, item in zip(self.tasks, data):
                        if item["completed"]:
                            task.mark_completed()
            else:
                # If file is missing or empty, create it and initialize with an empty list
                print("No tasks.json file found or file is empty. A new one will be created.")
                with open(filename, 'w') as file:
                    json.dump([], file)
        except FileNotFoundError:
            # Handle case where the file doesn't exist, just in case
            print("No tasks.json file found. A new one will be created.")
            with open(filename, 'w') as file:
                json.dump([], file)

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

    def save_tasks(self):
        data = [{"description": task.description, "completed": task.completed} for task in self.tasks]
        with open("tasks.json", "w") as file:
            json.dump(data, file)
        print("Tasks saved!")

