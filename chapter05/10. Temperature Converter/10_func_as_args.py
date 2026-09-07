def calculator(n1, n2, operation):
    """
    A calculator function that applies a passed function (operation) to two numbers.

    Args:
        n1 (_type_): _description_
        n2 (_type_): _description_
        operation (function): A function that takes two integers and return an integer.

    Returns"
      int: The result of applying the operation function to n1 and n2.    
    """
    try:
        return operation(n1, n2)
    except TypeError as e:
        print(f"Error: {e}. Ensure the 'operation' is a fucntion taking two integers. ")
        # return None

def add(no1, no2):
    return no1 + no2

def subtract(no1, no2):
    return no1 - no2

def multiply(no1, no2):
    return no1 * no2

def divide(no1, no2):
    if no2 == 0:
      raise ValueError("Division by zero is not allowed.")
    return no1 / no2

def main():
    print("Addition: ", calculator(5, 3, add))
    print("Subtraction: ", calculator(5, 3, subtract))              
    print("Multiplication: ", calculator(5, 3, multiply))              
    print("Division: ", calculator(5, 3, divide)) 


if __name__ == "__main__":
    main()                               