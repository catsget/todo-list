from storage import storage
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def colored_status(status: str):
    new_status = None
    if status == "Завершенная":
        new_status = f"[green]{status}[/green]"
    else:
        new_status = f"[red]{status}[/red]"
    
    return new_status


def view_menu():
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
        "Описание", justify="center", header_style="cyan bold", style="cyan", no_wrap=True
    )
    table.add_column(
        "Статус", justify="center", header_style="red bold", style="red", no_wrap=True
    )

    tasks = storage.tasks

    if not tasks:
        return

    for task in tasks:
        task_id = tasks.index(task)
        table.add_row(str(task_id), task.name, task.desc, colored_status(task.status))

    console.print(table)

    input()
