import random

my_list = [random.randint(1,100) for i in range(random.randint(3, 10))]
list_selection = [my_list[i] for i in (0, 2, -1)]
print(my_list)
print(list_selection)
