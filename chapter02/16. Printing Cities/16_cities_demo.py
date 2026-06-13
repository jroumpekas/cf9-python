def print_cities(*cities: str, seperator: str = ", ") -> None:

    """Homework"""
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", seperator.join(cities))
    pass

def main():
    print_cities("Athens", "Paris", "London", seperator="\t")
    print("Athens", "Paris", "London", sep="\t")
    print_cities()

if __name__ == "__main__":
    main()    