# Falsy - Truthy values
#Falsy examples: 0, 0.0, 0j, "", [], (), False, None, {},

empty_dict = {}
print(type(empty_dict))

empty_set = set()
print(type(empty_set))

print("-------------\n")

a = 5

if a >= 0 and a <= 10:
    print("is valid")
else:
    print("is not valid")

#chained comparison

if 0 <= a <= 10:
    print("is valid")
else:
    print("is not valid")        