from utils import clear
from storage import add_task


def add_menu(console):
    while True:
        clear()
        task_name = console.input("[magenta bold]Название:[/] ")

        if len(task_name) == 0:
            clear()
            console.print("[red]Некорректное значение[/red]")
            input()
            return
        elif len(task_name) > 50:
            clear()
            console.print("[red]Длина названия не может быть длиннее 50 символов")
            input()
            continue

        break

    while True:
        clear()
        console.print(f"[magenta bold]Название:[/] {task_name}")
        task_desc = console.input("[cyan bold]Описание:[/] ")

        if len(task_desc) > 50:
            clear()
            console.print("[red]Длина описания не может быть длиннее 50 символов[/]")
            input()
            continue
        elif len(task_desc) == 0:
            task_desc = "Пусто"
        
        break
    
    add_task(task_name, task_desc)
