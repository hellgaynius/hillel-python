num = int(input('Enter a number between 0 and 8640000: '))

days, remainder = divmod(num, 24 * 60 * 60)
hours, remainder = divmod(remainder, 60 * 60)
mins, remainder = divmod(remainder, 60)
sec = remainder

def parse(val):
    return str(val).zfill(2)

print(f'{days} days, {parse(hours)}:{parse(mins)}:{parse(sec)}')
