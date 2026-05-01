from string import ascii_letters

letters = input('Enter 2 letters divided by hyphen: ').split('-')

start = ascii_letters.index(letters[0])
end = ascii_letters.index(letters[1])

result = ascii_letters[start:end+1]
print(result)