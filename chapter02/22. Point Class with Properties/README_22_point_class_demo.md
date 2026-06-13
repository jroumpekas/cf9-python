# 🧱 An Advanced `Point`: Encapsulation, Dunder Methods & Properties

This lesson levels up the `Point` class with the full toolkit of Pythonic OOP: **private attributes**, **operator overloading** (`__eq__`, `__lt__`, `__repr__`), a **class method** that counts instances, and **properties** that give controlled access to private data.

---

## 1. Learning Objectives

- Use the `__` (double-underscore) name-mangling convention for **private** attributes.
- Track how many objects exist with a **class-level attribute** and a `@classmethod`.
- Overload operators by implementing `__eq__` (`==`) and `__lt__` (`<`).
- Provide a developer-facing string with `__repr__`, separate from `__str__`.
- Expose private data safely with `@property` getters and setters.

---

## 2. Prerequisites

- Comfort with classes, `__init__`, `__str__` (see `20`–`21`).
- Familiarity with the idea of "magic"/dunder methods.
- Awareness of `isinstance()` for type checks.

---

## 3. Key Concepts

- **Private attribute (`self.__x`)**: The leading `__` triggers *name mangling* — Python renames it to `_Point__x`, discouraging access from outside the class.
- **Class attribute (`__count`)**: Shared by **all** instances; incremented in `__init__` to count objects.
- **`@classmethod`**: Receives the class (`cls`) instead of an instance; `get_count()` reads the shared counter.
- **`__eq__`**: Defines what `==` means for two points (same `x` and same `y`).
- **`__lt__`**: Defines what `<` means — here, a point is "less than" another based on both coordinates.
- **`__repr__` vs `__str__`**: `__str__` is for users (`print`), `__repr__` is for developers/debugging (shown in the REPL and in lists).
- **`@property` / `@x.setter`**: Let you read `p.x` and write `p.x = 5` while the data stays private under the hood.

---

## 4. Lecture Outline

### 0:00–0:08 — Privacy & the Instance Counter
- `__x`, `__y`, and `Point.__count += 1`.

### 0:08–0:18 — `__str__`, `__repr__`, `__eq__`
- Two string forms plus equality.

### 0:18–0:28 — Overloading `<` with `__lt__`
- Comparing both coordinates.

### 0:28–0:38 — Class Method & Properties
- `get_count()`, then `@property` getters/setters for `x` and `y`.

---

## 5. Code Demos

```python
class Point:
    __count = 0                      # class-level: shared by all instances

    def __init__(self, x=0, y=0):
        self.__x = x                 # private instance attribute
        self.__y = y
        Point.__count += 1           # one more Point exists

    def __str__(self):
        return f"({self.__x}, {self.__y})"        # user-facing

    def __repr__(self):
        return f"Point(x={self.__x},y={self.__y})"  # developer-facing

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.__x <= other.__x and self.__y < other.__y) \
                or (self.__x < other.__x and self.__y <= other.__y)
        return False

    @classmethod
    def get_count(cls):
        return cls.__count

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

def main():
    p1 = Point(11, 20)
    p2 = Point(11, 20)

    print(p1 < p2)        # False — identical points, neither is strictly "less"
    print(p1 == p2)       # True  — same coordinates
    print(Point.get_count())   # 2  — two points created so far

if __name__ == "__main__":
    main()
```

**Expected output (with the extra prints above):**

```
False
True
2
```

> 💡 **Why does `p1 < p2` print `False` here?** Both points are `(11, 20)`. `__lt__` requires one coordinate to be strictly smaller while the other is smaller-or-equal. With everything equal, neither branch is satisfied, so the result is `False` — which is the correct behaviour for two identical points (neither is "less than" the other).

> 🔍 **`__str__` vs `__repr__`.** Try `print(p1)` → uses `__str__` → `(11, 20)`. Now put `p1` in a list and print the list: `print([p1])` → uses `__repr__` → `[Point(x=11,y=20)]`. The repr is meant to be unambiguous for debugging.

> 🔐 **Name mangling, not true privacy.** `self.__x` is renamed to `self._Point__x`. You *can* still reach it from outside as `p1._Point__x`, but the mangling signals "internal — don't touch". The `@property` is how you offer the *sanctioned* way in.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does the leading `__` in `self.__x` do?
- a) Makes the attribute truly inaccessible
- b) Triggers name mangling (`_Point__x`) to discourage outside access
- c) Makes it a class attribute
- d) Nothing

<details>
<summary>Solution</summary>

**Answer:** b) It triggers name mangling, signalling the attribute is internal. It is not truly private.
</details>

---

### 2. (Level 1, Short Answer)
What is the difference between `__str__` and `__repr__`?

<details>
<summary>Solution</summary>

`__str__` produces a readable, user-facing string (used by `print`). `__repr__` produces an unambiguous, developer-facing string (used in the REPL, in containers, and as a debugging fallback).
</details>

---

### 3. (Level 2, Coding)
Using the `@property`, read `p1.x` and then set it to `99`. Confirm the change.

<details>
<summary>Solution</summary>

```python
p1 = Point(11, 20)
print(p1.x)     # 11   (getter)
p1.x = 99       # setter
print(p1.x)     # 99
```
</details>

---

### 4. (Level 2, Short Answer)
Why is `__count` declared at the class level (`Point.__count`) rather than inside `__init__` as `self.__count`?

<details>
<summary>Solution</summary>

Because it must be **shared across all instances** to count the total number of points. An instance attribute (`self.__count`) would give every object its own separate counter, defeating the purpose.
</details>

---

### 5. (Level 3, Coding)
Add a setter validation: make the `x` setter reject non-numeric values by raising `TypeError`.

<details>
<summary>Solution</summary>

```python
@x.setter
def x(self, x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    self.__x = x
```
This is the main reason properties exist: you can run logic when an attribute is read or written.
</details>

---

## 7. Further Reading

- [Python Tutorial: Private Variables & Name Mangling](https://docs.python.org/3/tutorial/classes.html#private-variables)
- [Python Docs: `@property`](https://docs.python.org/3/library/functions.html#property)
- [Python Docs: `@classmethod`](https://docs.python.org/3/library/functions.html#classmethod)
- [Python Docs: Special method names (dunders)](https://docs.python.org/3/reference/datamodel.html#special-method-names)

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
