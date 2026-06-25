def add(a: int, b: int, c: int = 0) -> int:
    return a + b + c

def full_opt_add(a: int = 0, b: int = 0, c: int = 0) -> int:
    return a + b + c

def main():
    print(add(10, 20)) #30
    print(add(10))

    print(full_opt_add(1, 2, 3))
    print(full_opt_add(c = 3, a = 2, b = 1))

if __name__ == "__main__":
    main()    