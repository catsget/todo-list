from rich.console import Console
from utils import clear, int_input
import menus

console = Console()


def main_menu():
    while True:
        try:
            clear()
            print("Todo-list v1.0\n")
            print("1. Просмотреть задачи")
            print("2. Добавить задачу\n")
            console.print("[red bold]Нажмите CTRL+C чтобы выйти[/]\n")

            user_choice = int_input("Выбор: ")

            clear()
            if user_choice == 1:
                menus.view_menu(console)
            elif user_choice == 2:
                menus.add_menu(console)
            else:
                print("Некорректное значение")
                input()
        except KeyboardInterrupt:
            break