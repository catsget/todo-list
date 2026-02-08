from utils import clear, int_input
import menus

def main_menu():
    clear()
    print(
        "Todo-list v1.0",
        "",
        "1. Просмотреть задачи",
        "2. Добавить задачу",
        "",
        sep="\n"
    )
    user_choice = int_input("Выбор: ")

    clear()
    if user_choice == 1:
        menus.view_menu()
    elif user_choice == 2:
        menus.add_menu()
    elif user_choice == "":
        pass
    else:
        print("Некорректное значение")
        input()