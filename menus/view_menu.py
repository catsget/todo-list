from storage import storage
from rich.console import Console
from rich.table import Table
from rich import box
import menus
from utils import clear, int_input

console = Console()


def get_colored_status(status: str):
    new_status = None
    if status == "Завершенная":
        new_status = f"[green]{status}[/green]"
    else:
        new_status = f"[red]{status}[/red]"

    return new_status


def create_task_table():
    table = Table(title="Задания", show_lines=True, box=box.ROUNDED, padding=(0, 4))

    table.add_column(
        "ID", justify="center", header_style="green bold", style="green", no_wrap=True
    )
    table.add_column(
        "Название",
        justify="center",
        header_style="magenta bold",
        style="magenta",
        no_wrap=True,
    )
    table.add_column(
        "Описание",
        justify="center",
        header_style="cyan bold",
        style="cyan",
        no_wrap=True,
    )
    table.add_column(
        "Статус", justify="center", header_style="white bold", style="red", no_wrap=True
    )

    return table


def view_menu():
    while True:
        clear()
        try:
            table = create_task_table()
            tasks = storage.tasks

            if not tasks:
                return

            for task in tasks:
                task_id = str(tasks.index(task))
                table.add_row(task_id, task.name, task.desc, get_colored_status(task.status))

            console.print(table)

            user_choice = int_input("Выбор: ")

            if isinstance(user_choice, int):
                task = tasks[user_choice]

                menus.edit_menu(task)
            else:
                break
        except Exception as e:
            print(e)
            input()
