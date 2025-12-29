def common_elements():
    list1 = [i for i in range(1, 101) if i % 3 == 0]
    list2 = [i for i in range(1, 101) if i % 5 == 0]
    common = set(list1) & set(list2)
    return common