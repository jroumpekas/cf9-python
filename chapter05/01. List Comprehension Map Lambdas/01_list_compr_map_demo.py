list_of_ints = [1, 2, 3, 4, 5, 6, 7]
 
# 1. Using list comprehension to square each number in the list
squared_list_compr = [number ** 2 for number in list_of_ints]
print(f"Squared Numbers: {squared_list_compr}")
 
# 2. Using map() witha a lambda function to square each number in the list
def square_function(num):
    return num ** 2
 
squared_nums_lambda = list(map(lambda number: number ** 2, list_of_ints))
print(f"Squared numbers with map(): {squared_nums_lambda}")
 
# 3. Using map() with a function to square each number in the list
squared_nums_func = list(map(square_function, list_of_ints))
print(f"Squared number from square_function: {squared_nums_func}")
 
# 4. Filter in list compr using if
squared_filtered_nums = [number ** 2 for number in list_of_ints if number % 2 == 0]
# squared_filtered_nums = [square_function(number) for number in list_of_ints if number % 2 == 0]
print(f"Squared using list compr and if: {squared_filtered_nums}")
 
# 5. Filtering and mapping using filter and map functions
filtered_mapped_squared = list(map(square_function, filter(lambda x: x % 2 == 0, list_of_ints)))
print(f"Squared nums using filter and map functions: {filtered_mapped_squared}")