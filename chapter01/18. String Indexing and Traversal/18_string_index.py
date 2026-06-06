message = "Coding Factory"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

print(f"Number of letters inside the {message}: {len(message)}")


# Iterate over character in the string using enhanced for loop

for char in message:
    print(char, end=" ")

for i in range(1, 10 + 1):
    print(i, end=" ")
print()        