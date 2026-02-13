from rich.console import Console
from utils import clear, int_input
import menus

console = Console()


def main_menu():
    while True:
        try:
            clear()
            print("Todo-list v1.0\n")
            console.print("[cyan bold]1. Просмотреть задания[/]")
            console.print("[magenta bold]2. Добавить задание[/]\n")
            console.print("[red bold]Нажмите CTRL+C чтобы выйти[/]\n")

            user_choice = int_input("Выбор: ")

            clear()
            if user_choice == 1:
                menus.view_menu(console)
            elif user_choice == 2:
                menus.add_menu(console)
            elif user_choice == "":
                pass
            else:
                console.print("[red bold]Некорректное значение[/]")
                input()
        except KeyboardInterrupt:
            print()
            break