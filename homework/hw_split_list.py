import math

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 3, 4, 5]
list_3 = [1, 2, 3]
list_4 = [1]
list_5 = []

# Expected result
# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

def split_list(l):
    list_len = len(l)
    divider = math.ceil(list_len / 2)
    return [l[:divider], l[divider:]]

print(split_list(list_1))
print(split_list(list_2))
print(split_list(list_3))
print(split_list(list_4))
print(split_list(list_5))
