numbers = [10, 20, 30 , 40, 50]

iterator = iter(numbers)

 
while True:
    try:
        print("Calling next()...")
        item = next(iterator)
        print("Got item:", item)
    except StopIteration:
        print("No more items... StopIteration raised.")
        break