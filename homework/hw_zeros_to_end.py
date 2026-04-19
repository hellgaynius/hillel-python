list_1 = [0, 1, 0, 12, 3]
list_2 = [0]
list_3 = [1, 0, 13, 0, 0, 0, 5]
list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

lists = [list_1, list_2, list_3, list_4]

# Expected results
# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

def zeros_to_end(l):
    for index, num in enumerate(l):
        if num == 0:
            l.pop(index)
            l.append(num)
    print(l)

for l in lists:
    zeros_to_end(l)
