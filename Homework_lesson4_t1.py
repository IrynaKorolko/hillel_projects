original_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
list_null = []
list_not_null = []
for el in original_list:
    if el != 0:
        list_not_null.append(el)
    else:
        list_null.append(el)
print(list_not_null + list_null)
