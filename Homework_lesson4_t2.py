import random
my_list = []
for i in range (7):
    my_list.append(random.randint(3, 10))
print(my_list)
new_list_index1 = my_list[-1]
new_list_index2 = my_list[-3]
new_list_index3 = my_list[-2]
new_list = [new_list_index1, new_list_index2, new_list_index3]
print(new_list)