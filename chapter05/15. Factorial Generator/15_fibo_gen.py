def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
   fib = fibonacci()

   for i in range(10):
       print(f"fibo(i) = {next(fib)}")

if __name__ == "__main__":
    main()

