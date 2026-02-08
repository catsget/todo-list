from utils import clear
from storage import add_task


def add_menu():
    clear()
    task_name = input("Название: ")

    clear()
    if task_name != "":
        add_task(task_name)

    else:
        print("Некорректное значение")
        input()
