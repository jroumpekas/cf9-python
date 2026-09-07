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
   
    return plus, minus, mul, div

def main():
    ints_list = [26, 5, 4, 3, 2, 1]

    plus, minus, mul, div = calculate(ints_list)

    print(f"plus: {plus()}")   # 26 + 5 + 4 + 3 + 2 +1
    print(f"minus: {minus()}") # 26 - 5 - 4 - 3 -2 -1
    print(f"mul: {mul()}")     # 26 * 5 * 4 * 3 * 2 * 1
    print(f"div: {div()}")     # 26 / (5 + 4 + 3 + 2 + 1)

if __name__ == "__main__":
    main()


 