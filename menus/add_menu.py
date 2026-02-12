from utils import clear
from storage import add_task


def add_menu(console):
    clear()
    task_name = input("Название: ")

    if task_name == "":
        clear()
        console.print("[red]Некорректное значение[/red]")
        input()
        return
    task_desc = input("Описание: ")

    add_task(task_name, task_desc)