my_list = [1, 2, "hello", [3, 4, 5]]

new_list = my_list[:]

print(f"Are new_list and my_List the same object: {my_list is new_list}")

new_list[0] = 100

print(my_list)
print(new_list)

new_list[3][0] = 300 

print(my_list)
print(new_list)