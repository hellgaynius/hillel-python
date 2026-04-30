import string
import keyword

input_var = input('Enter variable name: ')

starts_w_num = input_var[0].isdigit()
has_capitalized_letters = any(char.isupper() for char in input_var)
is_reserved_word = input_var in keyword.kwlist

forbidden_chars = string.punctuation.replace('_', ' ')
has_forbidden_chars = any(char in forbidden_chars for char in input_var)

underscore_index = input_var.find('_')

if underscore_index == -1 or len(input_var) == 1:
    has_double_underscore = False
else:
    has_double_underscore = input_var[underscore_index+1] == '_'

is_valid = not starts_w_num and not has_forbidden_chars and not has_double_underscore and not has_capitalized_letters and not is_reserved_word

print(is_valid)
