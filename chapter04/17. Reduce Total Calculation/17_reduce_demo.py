from functools import reduce
 
num = int(input("Give me an it to calculate the factorial: "))
 
# reduce(lambda x, y: x * y, range(1, 5 + 1))
# First step: x=1, y=2 (result = 1 * 2)
# Second step: x = 2, y = 3 (result = 2 * 3)
# Third step: x = 6, y = 4 (result = 6 * 4)
# Fourth step: x = 24, y = 5 (result = 24 * 5) = 120
result = reduce(lambda x, y: x * y, range(1, num + 1)) # range(1, 6) -> 1, 2, 3, 4, 5
print(f"{num}! = {result}")
 
def print_and_multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result
 
new_result = reduce(print_and_multiply, range(1, 6))
print(f'Final result: {new_result}')

result = reduce(lambda x, y: print(f"{x} * {y} = {result}") or x * y, range(1, 6))
print(f"Final super wow result: {result}")