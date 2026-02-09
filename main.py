from menus import main_menu
from storage import load_tasks


def main():
    load_tasks()
    while True:
        try:
            main_menu()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
