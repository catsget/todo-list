from utils import clear, int_input

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
        print("test1")
        input()
    elif user_choice == 2:
        print("test2")
        input()
    elif user_choice == "":
        pass
    else:
        print("Некорректное значение")
        input()