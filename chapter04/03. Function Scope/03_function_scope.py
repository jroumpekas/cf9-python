a = 10
b = 20

def add_numbers(x: int, y: int) -> int:
    x = 100
    return x + y

def main():
    result = add_numbers(a, b)

    print(result)
    print(f"a = {a}")

if __name__ == "__main__":
    main()