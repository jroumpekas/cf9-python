def is_square(length:int, width:int) -> bool:

    """Check if rectangle is square...

    """
    return length == width

def my_add(a, b):
   return a + b

def main():
   # print(is_square(10, 10))

    # print(my_add(100, 200)) #300
    # print(my_add("Hello", "CF9 friends"))


  try:  
    length = input("Give me the length of the rectangle: ")
    width = input("Give me the width of the rectangle: ")
  except ValueError:
    print("Invalid input. Please enter valid integers for length and width. ")  
   
  if is_square(length=length, width=width):
    print("The rectangle is square")
  else:
    print("The rectangle is NOT square")

    pass

if __name__ == '__main__':
  main()