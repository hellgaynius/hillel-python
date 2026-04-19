print("Введіть перше число:")
number_1 = int(input())

print("Введіть друге число:")
number_2 = int(input())

print("Введіть операцію (+, -, *, /):")
operation = input()

operations_map = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

if number_2 == 0 and operation == "/":
    print('No zero division in this universe')
else:
    print(operations_map[operation](number_1, number_2))
