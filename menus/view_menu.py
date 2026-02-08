from storage import storage


def view_menu():
    tasks = storage.load_tasks()

    for task in tasks:
        print(f"{task.name}\n")

    input()
