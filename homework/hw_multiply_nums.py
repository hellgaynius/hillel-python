number_input = input('Enter a number: ')

def multiply_digits(number):
    if int(number) <= 9:
        return number
    multiplied_number = 1
    for char in number:
        multiplied_number *= int(char)
    print(multiplied_number)
    return multiply_digits(str(multiplied_number))

result = multiply_digits(number_input)
print(result)
