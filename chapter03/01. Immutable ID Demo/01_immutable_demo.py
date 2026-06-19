def print_id(variable_name, variable):
    """Prints the id of the given variable.

    Args:
        variable_name (_type_): _description_
        variable (_type_): _description_
    """
    print(f"id({variable_name}) = {id(variable)}")


def main():
    a = 10
    b = 10

    print_id("a", a)
    print_id("b", b) 

    print("Now i change the value of b. ")
    b= 20
    print_id("a", a)
    print_id("b", b)
    print(a, b)

    str1 = "CF9"
    str2 = "CF9"

    print_id("str1", str1)
    print_id("str2", str2)

    
if __name__ == '__main__':
    main()