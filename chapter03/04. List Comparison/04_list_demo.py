def compare_lists(list1, list2):
    print(f"{list1} is {list2}: {list1 is list2}") # check the identity
    print(f"{list1} == {list2}: {list1 == list2}") # check the content
    

def main():
    my_ints = [10, 20, 30]
    your_ints = [10, 20, 30]

    compare_lists(my_ints, your_ints)

if __name__ == "__main__":
    main()