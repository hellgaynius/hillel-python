from string import punctuation

def is_palindrome(text):
    for char in [*punctuation, ' ']:
        text = text.replace(char, '')
    text = text.lower()
    if text == text[::-1]:
        return True
    return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
assert is_palindrome('did') == True, 'Test4'
print("ОК")
