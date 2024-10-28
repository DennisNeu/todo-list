class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self) -> str:
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.description}"

    def mark_completed(self):
        self.completed = True

    def delete(self):
        self.delete() 