from menus import main_menu


def main():
    while True:
        try:
            main_menu()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
