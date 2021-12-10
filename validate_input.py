def validate_input(prompt='', type=int):
    not_valid = True
    while not_valid:
        try:
            user_input = type(input(prompt))
        except ValueError:
            print(f'Try again. Your input should be {type}.')
            continue
        else:
            return user_input