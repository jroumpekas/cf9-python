# 📍 Point Class with Properties

This lesson builds a `Point` class using properties, setter validation, a computed property, and a movement method.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `31_point_class.py` | Defines a 2D point with validated properties, distance calculation, movement, and string representation. |

---

## 1. Learning Objectives

- Use `@property` and setters.
- Validate numeric coordinates.
- Calculate distance from origin.
- Move a point.
- Customize object printing with `__str__()`.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Properties**: Control access to `x` and `y`.
- **Validation**: Rejects non-numeric coordinate values.
- **Computed property**: `distance_from_origin` is calculated from x and y.
- **Movement**: `move(dx, dy)` changes the point coordinates.

---

## 4. Code Demo

```python
import math

class Point:
    @property
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"
```

---

## 5. Expected Output / Behaviour

```text
Point(x=3, y=4)
3
4
5.0
Point(x=5, y=5)
Point(x=10, y=5)
TypeError: x must be a number
```

The script intentionally assigns `p.x = "Hello"`, which raises a `TypeError` because the setter accepts only numbers.

---

## 6. Exercises

### 1. Level 1 — Short Answer
Explain the main idea of this script in your own words.

<details>
<summary>Solution</summary>

The script demonstrates one focused Python concept through a small runnable example.
</details>

---

### 2. Level 2 — Coding
Add one extra test case to the script and run it again.

<details>
<summary>Solution</summary>

Add one more function call or one more input example inside `main()`.
</details>

---

## 7. Further Reading

- [Python Docs: Tutorial](https://docs.python.org/3/tutorial/)
- [Python Docs: Standard Library](https://docs.python.org/3/library/)

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

---

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

---

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: These are Python scripts and require a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
