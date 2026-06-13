def get_average(*numbers):
    if not numbers:
        return "No numbers provided"
    else:
        average = sum(numbers) / len(numbers)
        return "{:.2f}".format(average)
    # return sum(numbers) / len(numbers)
    

def main():
    print(get_average(10, 20, 15))

    my_ints = [10, 20, 30]
    print()

if __name__ == "__main__":
    main()