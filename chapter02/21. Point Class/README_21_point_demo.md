# 📍 A `Point` Class: `__str__`, Methods & the `math` Module

This lesson builds a `Point` class representing a location in 2D space. It introduces the `__str__` "magic method" for pretty printing and a `distance()` method that uses the `math` module to apply the Pythagorean theorem.

---

## 1. Learning Objectives

- Define a class with default constructor values (`x=0`, `y=0`).
- Implement `__str__` so `print(point)` shows a friendly representation.
- Write an instance method (`distance`) that takes **another object** as a parameter.
- Use `math.sqrt` and `math.pow` to compute Euclidean distance.
- Mutate an object's attributes after creation (`p1.x = 0`).

---

## 2. Prerequisites

- Comfort with classes, `__init__`, and `self` (see `20_class_demo.py`).
- Familiarity with importing modules (`import math`).
- Awareness of the Pythagorean theorem.

---

## 3. Key Concepts

- **`__str__(self)`**: The "to-string" magic method. When you `print(p1)` or use `f"{p1}"`, Python calls `__str__` to get the text.
- **Default coordinates**: `def __init__(self, x=0, y=0)` lets you create `Point()` at the origin.
- **Method taking another object**: `distance(self, other)` compares *this* point (`self`) with `other`.
- **Euclidean distance**: √((x₁−x₂)² + (y₁−y₂)²), implemented with `math.sqrt` and `math.pow`.
- **Attribute mutation**: `p1.x = 0` changes the point in place after it was created.

---

## 4. Lecture Outline

### 0:00–0:08 — Class & Constructor
- `class Point:` with `__init__(self, x=0, y=0)`.

### 0:08–0:16 — Friendly Printing
- `__str__` returns a string like `(10), (20)`.

### 0:16–0:26 — The `distance` Method
- `math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))`.

### 0:26–0:34 — Mutating Points & Re-measuring
- Set `p1` to (0, 3) and `p2` to (4, 0) → distance `5.0`.

---

## 5. Code Demos

```python
import math

class Point:
    """A point in 2D space with x and y coordinates."""

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

    print(f"Point 1: {p1}")    # uses __str__
    print(f"Point 2: {p2}")

    print(f"Distance p1:p2 = {p1.distance(p2)}")

    p1.x = 0
    p1.y = 3
    p2.x = 4
    p2.y = 0

    print(f"Distance p1:p2 = {p1.distance(p2)}")   # the classic 3-4-5 triangle

if __name__ == "__main__":
    main()
```

**Expected output:**

```
Point 1: (10), (20)
Point 2: (30), (40)
Distance p1:p2 = 28.284271247461902
Distance p1:p2 = 5.0
```

> 💡 **The 3-4-5 triangle.** After mutation, `p1` is at (0, 3) and `p2` at (4, 0). The horizontal gap is 4, the vertical gap is 3, and √(3² + 4²) = √25 = **5.0** — the most famous right triangle in mathematics, popping out of your code.

> 🎨 **A note on the `__str__` format.** The string `"({self.x}), ({self.y})"` prints as `(10), (20)`. A more conventional point format is `(10, 20)` — i.e. `f"({self.x}, {self.y})"`. Both are valid; just pick the one that reads best to you. (The next lesson, `22_point_class_demo.py`, uses the conventional form.)

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which method is called when you run `print(p1)`?
- a) `__init__`
- b) `__str__`
- c) `distance`
- d) `print`

<details>
<summary>Solution</summary>

**Answer:** b) `__str__`.
</details>

---

### 2. (Level 1, Short Answer)
Why can you write `Point()` with no arguments?

<details>
<summary>Solution</summary>

Because the constructor declares default values `x=0` and `y=0`, so omitting them creates a point at the origin `(0, 0)`.
</details>

---

### 3. (Level 2, Coding)
Compute the distance of a point from the origin without creating a second point.

<details>
<summary>Solution</summary>

```python
origin = Point()              # (0, 0)
p = Point(3, 4)
print(p.distance(origin))     # 5.0
```
</details>

---

### 4. (Level 2, Coding)
Rewrite `distance` using the `**` exponent operator instead of `math.pow`.

<details>
<summary>Solution</summary>

```python
def distance(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
```
</details>

---

### 5. (Level 3, Coding)
Add a `move(self, dx, dy)` method that shifts the point by `dx` and `dy`, then test it.

<details>
<summary>Solution</summary>

```python
def move(self, dx, dy):
    self.x += dx
    self.y += dy

p = Point(1, 1)
p.move(2, 3)
print(p)   # (3), (4)
```
</details>

---

## 7. Further Reading

- [Python Docs: `math.sqrt` and `math.pow`](https://docs.python.org/3/library/math.html)
- [Python Docs: `object.__str__`](https://docs.python.org/3/reference/datamodel.html#object.__str__)
- [Python Tutorial: Classes](https://docs.python.org/3/tutorial/classes.html)

---

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a> (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
