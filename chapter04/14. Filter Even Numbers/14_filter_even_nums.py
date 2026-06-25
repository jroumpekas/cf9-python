numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# Even numbers iterator
even_numbers_iter = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers_iter)
 
# for num in even_numbers_iter:
#     print(num, end="\t")
# print()
# print("-----------------------------")
# for num in even_numbers_iter:
#     print(num, end="\t")
# print()
even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers))

for num in even_numbers_list:
    print(num, end="\t")
print()    