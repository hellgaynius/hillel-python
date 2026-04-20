from hw_calculator import calculate_user_input

is_continue = True

while is_continue:
    calculate_user_input()
    is_continue = (input('Type y or yes if continue calculating: ')).lower() in ['y', 'yes']
