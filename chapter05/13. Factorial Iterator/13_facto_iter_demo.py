class FactoIterator:
    def __init__(self, n):
       if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
       self.n = n
       self.result = 1
       self.order = 0 # Start from 0 to include 0!

    def __iter__(self):
       return self

    def __next__(self):
       if self.order > self.n:
          raise StopIteration

       if self.order == 0:
          # Hamdle the special case for 0!
          self.order += 1
          return 1

       self.result *= self.order
       self.order += 1
       return self.result   

def main():
 facto_iter = FactoIterator(5)

 a = next(facto_iter)
 print(f"a = {a}")

 b = next(facto_iter)
 print(f"b = {b}")

 print("-----------------")

#   for factorial in facto_iter:
#     print(factorial)

if __name__ == "__main__":
   main()    
    