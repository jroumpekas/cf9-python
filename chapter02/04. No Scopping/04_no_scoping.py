import random

random_numbers = []

for i in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)

print(random_numbers)

for num in random_numbers:
    if num % 2 == 0:
        even = num
        name = "Katerina"
        
print(f"Even: {even}")
print(name)
print(num)        