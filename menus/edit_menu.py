from rich.table import Table
from rich import box
from utils import clear, int_input
from storage import save_tasks, delete_task


def get_colored_status(status: str):
    new_status = None
    if status == "Завершенное":
        new_status = f"[green]{status}[/green]"
    else:
        new_status = f"[red]{status}[/red]"

    return new_status


def create_task_table(task_id):
    table = Table(
        title=f"Задание {task_id}", show_lines=True, box=box.ROUNDED, padding=(0, 4)
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


def edit_menu(task, console, task_id):
    while True:
        save_tasks()
        clear()
        table = create_task_table(task_id)

        table.add_row(task.name, task.desc, get_colored_status(task.status))

        console.print(table)
        console.print("\n1. [magenta bold]Изменить название[/]")
        console.print("2. [cyan bold]Изменить описание[/]")
        console.print("3. [green bold]Пометить как выполненное[/]")
        console.print("4. [red bold]Удалить задание[/]\n")
        print("Нажмите ENTER чтобы вернуться назад\n")

        choice = int_input("Выбор: ")

        if choice == 1:
            clear()
            new_name = input("Новое название: ")

            if len(new_name) > 0:
                task.name = new_name
                print("Название успешно изменено")
            else:
                print("Название не может быть пустым!")
            input()
        elif choice == 2:
            clear()
            new_desc = input("Новое описание: ")

            if len(new_desc) > 0:
                task.desc = new_desc
                print("Описание успешно изменено")
            else:
                print("Описание не может быть пустым!")
            input()
        elif choice == 3:
            if task.status == "Не завершенное":
                task.status = "Завершенное"
            else:
                task.status = "Не завершенное"
        elif choice == 4:
            clear()
            console.print("Вы уверены? [green bold]y[/] or [red bold]n[/]\n")
            confirm = input()

            if confirm == "y":
                delete_task(task_id)
                save_tasks()
                break
        elif isinstance(choice, str):
            break
