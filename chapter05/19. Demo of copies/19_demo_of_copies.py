import copy
 
def main():
    ages = [1, [2, 3, 4], 5]
 
    # Method 1. Shallow copy using list slicing
    ages_slice = ages[:]
 
    # Method 2. Shallow copy using list's copy method
    ages_cp = ages.copy()
 
    # Method 3. Shallow copy using list() constructor
    ages_list = list(ages)
 
    # Method 4. Deep copy
    ages_deep_copy = copy.deepcopy(ages)
 
    print(f"Original list: {ages}")
    print(f"Shallow copy with slicing: {ages_slice}")
    print(f"Shallow copy with list copy method: {ages_cp}")
    print(f"Deep copy: {ages_deep_copy}")
 
    ages[0] = 100
    ages[1][0] = 200
 
    print(f"Original list: {ages}")
    print(f"Shallow copy with slicing: {ages_slice}")
    print(f"Shallow copy with list copy method: {ages_cp}")
    print(f"Deep copy: {ages_deep_copy}")
 
 
if __name__ == "__main__":
    main()