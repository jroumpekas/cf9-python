import math

class Point:
    """
    A class representing a point in 2D space.

    Attributes:
    x (float): The x-coordinate of the point.
    y (float): The y-coordinate of the point.

    """
    def __init__(self, x: float = 0, y: float = 0):
      self.x = x
      self.y = y

    def __str__(self):
     return f"({self.x}), ({self.y})"   

    def distance(self, other):
      return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

def main():
    p1 = Point(10, 20)
    p2 = Point(30, 40)

    print(f"Point 1: {p1}") #print(p1)
    print(f"Point 2: {p2}") #print(p2)

    print(f"Distance p1:p2 = {p1.distance(p2)}")

    p1.x = 0
    p1.y = 3

    p2.x = 4
    p2.y = 0

    print(f"Distance p1:p2 = {p1.distance(p2)}")


if __name__ == "__main__":
        main()  
