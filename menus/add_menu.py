from utils import clear
from storage import add_task


def add_menu():
    clear()
    task_name = input("Название: ")

    if task_name == "":
        clear()
        print("Некорректное значение")
        input()
        return
    task_desc = input("Описание: ")

    add_task(task_name, task_desc)