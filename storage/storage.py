import json
from models import Task
from utils import to_dict, to_object

tasks = []


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = []

            for task in json.load(file):
                tasks.append(to_object(task))

            if tasks != []:
                return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    except Exception as e:
        print(e)
        input()


def add_task(task_name: str):
    global tasks

    if not tasks:
        load_tasks()

    try:
        new_task = Task(name=task_name)
        tasks.append(new_task)
        with open("tasks.json", "w") as file:
            json.dump([to_dict(t) for t in tasks], file)

    except Exception as e:
        print(e)
        input()
