from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        number_of_task = 0
        new_tasks = []
        for task in self.tasks:
            if task.completed:
                number_of_task += 1
                continue

            new_tasks.append(task)
            

        self.tasks = new_tasks.copy()

        return f"Cleared {number_of_task} tasks."

    def view_section(self) -> str:
        result = []
        result.append(f"Section {self.name}:")
        for task in self.tasks:
            result.append(task.details())

        return "\n".join(result)
