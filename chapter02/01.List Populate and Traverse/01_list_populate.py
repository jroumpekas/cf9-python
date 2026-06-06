ages = [19, 23, 34, 45]

print("Initial list of ages:", ages)

#Read: Iterating over a list with enhanced for

for age in ages:
    print(ages, end=" ")
print()

# enumerate()
#Read: Iterate over a list using enumerate -> (index,value)
a, b = (10,20)
for index, value in enumerate(ages):
    print(f"Index: {index}, Value: {value}")