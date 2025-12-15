lst = [2, 3, 6, 7, 8]
length_lst = len(lst)
if length_lst == 0:
    print([], [])
else:
    middle_index = (length_lst + 1) // 2
    first_list = lst[:middle_index]
    second_list = lst[middle_index:]
    result = [first_list, second_list]
    print(f"Початковий список: {lst}")
    print(f"Результат: {result}")