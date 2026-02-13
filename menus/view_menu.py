from storage import storage
from rich.table import Table
from rich import box
import menus
from utils import clear, int_input


def get_colored_status(status: str):
    new_status = None
    if status == "Завершенное":
        new_status = f"[green]{status}[/green]"
    else:
        new_status = f"[red]{status}[/red]"

    return new_status


def create_tasks_table():
    table = Table(title="Задания", show_lines=True, box=box.ROUNDED, padding=(0, 4))

    table.add_column("ID", vertical="middle", justify="center", header_style="green bold", style="green")
    table.add_column(
        "Название",
        vertical="middle",
        justify="center",
        header_style="magenta bold",
        style="magenta",
    )
    table.add_column(
        "Описание",
        vertical="middle",
        justify="center",
        header_style="cyan bold",
        style="cyan",
    )
    table.add_column("Статус", vertical="middle", justify="center", header_style="white bold", style="red")

    return table


def view_menu(console):
    while True:
        clear()
        try:
            table = create_tasks_table()
            tasks = storage.tasks

            if not tasks:
                print("У вас нет заданий")
                input()
                break

            for task in tasks:
                task_id = str(tasks.index(task))
                table.add_row(
                    task_id, task.name, task.desc, get_colored_status(task.status)
                )

            console.print(table)
            print("Нажмите ENTER чтобы вернуться в главное меню\n")

            user_choice = int_input("Выбор: ")

            if isinstance(user_choice, int) and user_choice <= (len(tasks) - 1):
                task = tasks[user_choice]
                task_id = tasks.index(task)

                menus.edit_menu(task, console, task_id)
            elif isinstance(user_choice, str):
                break
            else:
                clear()
                console.print("[red]Неправильный номер[/red]")
                input()
        except Exception as e:
            print(e)
            input()
