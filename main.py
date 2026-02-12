from menus import main_menu
from storage import load_tasks


def main():
    load_tasks()
    main_menu()


if __name__ == "__main__":
    main()
