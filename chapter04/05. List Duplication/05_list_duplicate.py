my_list = [1, 2, "hello", [3, 4, 5]]

print("At the start")
for item in my_list:
    print(f"{item} : {id(item)}")

# Create a new list by repeating the original list twice
new_list = my_list * 2
print(f"New list: {new_list}")
print("--------------")

new_list[0] = 100
print(f"Duplicated list: {new_list}")

new_list[3][0] = 300
print(f"Modifieded list: {new_list}")
