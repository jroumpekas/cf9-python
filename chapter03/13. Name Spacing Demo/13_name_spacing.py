def name_spacing(num: int):
  if not isinstance(num, int):
     print("The number of spaces must be an integer. ")
     return
  
  if num < 0:
     print("The number of spaces has to be positive")
     return
  
  name = input("Please give a name: ").strip()

  if not name:
     print("No name provided")
     return
  
  spaced_name = (' ' * num).join(name)
  print(spaced_name)

def main():
    name_spacing(4)

if __name__ == "__main__":
    main()