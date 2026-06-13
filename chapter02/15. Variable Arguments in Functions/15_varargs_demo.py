def print_cities(*cities):
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", ", ".join(cities))
    pass

def main():
    print_cities("Athens", "Paris", "London")
    print_cities("Athens")
    print_cities()

if __name__ == "__main__":
    main()    