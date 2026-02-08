def int_input(text: str):
    try:
        number = int(input(text))
        return number
    except ValueError:
        return None