def my_add(a: float | int, b: float | int) -> float | int:
    """
    Add two numbers and returns the result.
 
    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add.
   
    Returns:
        int | float: The sum of a and b.
 
    Raises:
        TypeError: If either a or b is not integer or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both a and b must be integers or floats")
   
    return a + b

def main():
    print(my_add(10, 20))
    print(my_add(5, 7.1))

    try:
        print(my_add("Hello", "CF9"))
    except TypeError as e:
        print(e)

    print(f"Annotations: {my_add.__annotations__}")
    print(f"Docs: {my_add.__doc__}")


print("----------------------------")
help(my_add)    

if __name__ == "__main__":
    main()