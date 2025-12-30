def common_elements():
    common = set([i for i in range(1, 101) if i % 3 == 0]) & set([i for i in range(1, 101) if i % 5 == 0])
    return common