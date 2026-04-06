# 1. Квадрат числа.

print('1. "Квадрат числа". Введіть число:')
result = int(input()) ** 2
print('Квадрат:', result)

# 2. “Середнє трьох чисел”

print('2. “Середнє трьох чисел”. Введіть три числа через кому:')
three_numbers = input()
split_three_numbers = three_numbers.replace(' ', '').split(',')
num_list = list(map(int, split_three_numbers))
average = sum(num_list) / len(num_list)
print('your average:', round(average, 1))

# 3. “Перетворення хвилин у години”

def get_ending(number, forms):
    number = abs(number) % 100
    if 11 <= number <= 14:
        return forms[2]
    number = number % 10
    if number == 1:
        return forms[0]
    elif 2 <= number <= 4:
        return forms[1]
    else:
        return forms[2]

print('3. “Перетворення хвилин у години”. Введіть кількість хвилин:')
mins_input = int(input())
hours, mins = divmod(mins_input, 60)
hour_ending = get_ending(hours, ('година', 'години', 'годин'))
min_ending = get_ending(mins, ('хвилина', 'хвилини', 'хвилин'))
print(f"{hours} {hour_ending} {mins} {min_ending}")

# 4. “Розрахунок знижки”

print('4. “Розрахунок знижки”. Введіть ціну:')
price = int(input())
print('Введіть знижку (%):')
discount = int(input())
if discount == 100:
    print('Забирайте задарма!')
elif discount > 100:
    print('Знижка не може бути більше 100%')
else:
    print(f'Ціна зі знижкою: {round(price - (price * (discount / 100)), 2)}')

# 5. “Остання цифра числа”

print('5. “Остання цифра числа”. Введіть число:')
another_number = input()
print(f"Остання цифра: {another_number[-1]}")

# 6. “Периметр прямокутника”

print('6. “Периметр прямокутника”. Введіть висоту:')
height = int(input())
print('Введіть ширину:')
width = int(input())
print(f'Периметр: {(height + width) * 2}')

# 7. Виведення числа в стовпчик

print('7. Виведення числа в стовпчик. Введіть 4-значне число:')
four_digit_num = int(input())
digit_1, remainder_1 = divmod(four_digit_num, 1000)
print(digit_1)
digit_2, remainder_2 = divmod(remainder_1, 100)
print(digit_2)
digit_3, remainder_3 = divmod(remainder_2, 10)
print(digit_3)
print(remainder_3)
