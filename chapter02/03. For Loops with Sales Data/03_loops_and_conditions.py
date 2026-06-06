#List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# fruit we want to check
fruit_to_check = "Orange"

for fruit in fruits:
    if fruits == fruit_to_check:
        print(f"{fruit_to_check} is in your list. ")
        break
    else:
        print(f"{fruit_to_check} is NOT in your list. ")  

# One-liner condition check
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} your list")          