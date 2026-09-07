def avg(*args):
    # 1st approach
    # if not len(args):
    #     return 0
    # sum = 0
    # for arg in args:
    #     sum += arg
    # return sum / len(args)
 
    # 2nd approach
    # if not args: return 0
    # return sum(args) / len(args)
 
    # 3rd approach
    return sum(args) / len(args) if args else 0
 
 
 
def main():
    print(avg())
    print(avg(10))
    print(avg(10, 20))
 
if __name__ == "__main__":
    main()