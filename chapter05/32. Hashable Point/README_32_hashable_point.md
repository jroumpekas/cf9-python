# 🔐 Hashable Point Class

This lesson demonstrates how to make custom objects hashable and usable as dictionary keys.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `32_hashable_point.py` | Implements `__eq__`, `__hash__`, and `__repr__` so Point objects can be dictionary keys. |

---

## 1. Learning Objectives

- Implement value-based equality with `__eq__()`.
- Implement `__hash__()` using a tuple.
- Use custom objects as dictionary keys.
- Understand why equal objects should have equal hashes.
- Use `__repr__()` for readable output.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **`__eq__()`**: Defines when two points are equal.
- **`__hash__()`**: Returns a hash value based on coordinates.
- **Hashable object**: Can be used as a dictionary key.
- **Dictionary key update**: Equal keys update the same dictionary entry.

---

## 4. Code Demo

```python
class Point:
    def __eq__(self, other):
        return isinstance(other, Point) and self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash((self._x, self._y))

    def __repr__(self):
        return f"Point({self._x}, {self._y})"
```

---

## 5. Expected Output / Behaviour

```text
p1 == p3: True
p1 == p2: False
Point(1, 2): Point 3
Point(3, 4): Point 2
```


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
