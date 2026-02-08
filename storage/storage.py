import json
from models import Task

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            json_data = json.load(file)
            
            if json_data != []:
                tasks = [Task.model_validate(item) for item in json_data]
                return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    except Exception as e:
        print(e)

def add_task(task_name: str):
    global tasks

    if not tasks:
        load_tasks()
    
    try:
        new_task = Task(name=task_name)
        tasks.append(new_task)

        tasks_dict = [task.model_dump() for task in tasks]

        with open("tasks.json", "w") as file:
            json.dump(tasks_dict, file)

    except Exception as e:
        print(e)
