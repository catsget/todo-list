from rich.table import Table
from rich import box


def get_colored_status(status: str):
    new_status = None
    if status == "Завершенная":
        new_status = f"[green]{status}[/green]"
    else:
        new_status = f"[red]{status}[/red]"

    return new_status


def create_task_table(task_id):
    table = Table(
        title=f"Задание №{task_id}", show_lines=True, box=box.ROUNDED, padding=(0, 4)
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
    table = create_task_table(task_id)

    table.add_row(task.name, task.desc, get_colored_status(task.status))

    console.print(table)
    input()
