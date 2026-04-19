list_1 = [1, 3, 5]
list_2 = [6]
list_3 = []

lists = [list_1, list_2, list_3]

# Expected results
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

def do_calculations(l):
    numbers_sum = 0
    if len(l) == 0:
        print(0)
        return

    for index, num in enumerate(l):
        if index == 0 or index % 2 == 0:
            numbers_sum += num
    result = numbers_sum * l[-1]
    print(result)

for l in lists:
    do_calculations(l)
