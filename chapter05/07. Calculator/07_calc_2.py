import functools
 
def calculate(args):
    def plus():
        return functools.reduce(lambda x, y: x + y, args)
   
    def minus():
        return functools.reduce(lambda x, y: x -y, args)
   
    def mul():
        return functools.reduce(lambda x, y: x * y, args)
   
    def div():
        if not 0  in args[1:]:
            return args[0] / sum(args[1:])
        else:
            return "Division by zero error"
   
    return {
        "add": plus,
        "subtract": minus,
        "multiply": mul,
        "division": div
    }
 
 
def main():
    ints_list = [26, 5, 4, 3, 2, 1]
 
    operations = calculate(ints_list)
 
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
 
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input.")
            continue
       
        match choice:
            case 1:
                print(f"Addition result: {operations["add"]}")
            case 2:
                print(f"Subtraction result: {operations["subtract"]}")
            case 3:
                print(f"Multiplication result: {operations["multiply"]}")
            case 4:
                print(f"Divition result: {operations["division"]}")
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice! Please try again!")
 
if __name__ == "__main__":
    main()
 