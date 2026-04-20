import string

user_input = input('Enter text for hashtag: ')
hashtag = user_input.title()

for char in [*string.punctuation, ' ']:
    hashtag = hashtag.replace(char, '')

print(f'#{hashtag[:139]}') # всього 140 символів з решіткою включно
