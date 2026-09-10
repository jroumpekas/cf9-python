# 📦 Tuple Immutability & Mutable Elements

This lesson explains why a tuple item cannot be reassigned, while a list inside a tuple can still be modified.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `24_unmodifiable_tuples.py` | Shows that tuples are immutable but can contain mutable objects. |

---

## 1. Learning Objectives

- Create tuples.
- Understand tuple immutability.
- Catch `TypeError` when reassigning tuple elements.
- Modify a list stored inside a tuple.
- Inspect values and object ids.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Tuple immutability**: A tuple does not support item assignment.
- **Mutable nested object**: A list inside a tuple can change in place.
- **`TypeError`**: Raised when trying to replace a tuple element.
- **`id()`**: Shows object identity.

---

## 4. Code Demo

```python
my_tuple = (1, 2, [3, "CF"], "Hello")

try:
    my_tuple[2] = [1, 2, 3]
except TypeError as e:
    print(f"Error: {e}")

my_tuple[2][0] = 300
print("Modified my_tuple:", my_tuple)
```

---

## 5. Expected Output / Behaviour

```text
Error: 'tuple' object does not support item assignment
Modified my_tuple: (1, 2, [300, 'CF'], 'Hello')
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
