def int_input(text: str):
    try:
        user_input = input(text)
        number = int(user_input)
        return number
    except ValueError:
        return user_input