def common_elements():
    divided_by_3 = set()
    divided_by_5 = set()
    for num in range(0, 100):
        if num % 3 == 0:
            divided_by_3.add(num)
        if num % 5 == 0:
            divided_by_5.add(num)
    return divided_by_3.intersection(divided_by_5)

# верхнє вирішення - за умовами задачі.
# трохи простіший варіант з одним if:

# def common_elements2():
#     divided_by_3_and_5 = set()
#     for num in range(0, 100):
#         if num % 3 == 0 and num % 5 == 0:
#             divided_by_3_and_5.add(num)
#     return divided_by_3_and_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
