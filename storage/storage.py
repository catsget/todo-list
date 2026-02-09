import json
from models import Task
from utils import to_dict, to_object

tasks = []


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = []

            for task in json.load(file, ):
                tasks.append(to_object(task))

    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    
    return tasks


def add_task(task_name: str, task_desc: str):
    global tasks

    try:
        new_task = Task(name=task_name, desc=task_desc)
        tasks.append(new_task)
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump([to_dict(t) for t in tasks], file, ensure_ascii=False, indent=2)

    except Exception as e:
        print(e)
        input()
