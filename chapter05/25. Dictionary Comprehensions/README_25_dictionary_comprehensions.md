# 🔑 Dictionary Comprehensions Demo

This lesson demonstrates dictionary comprehensions through square-number examples.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `25_dictionary_comprehensions.py` | Creates dictionaries of numbers and squares with direct expressions and helper functions. |

---

## 1. Learning Objectives

- Create a dictionary comprehension.
- Use numbers as keys.
- Use calculated values.
- Add filtering conditions.
- Call a helper function inside a comprehension.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Dictionary comprehension**: Compact syntax for building dictionaries.
- **Key-value pairs**: Each number becomes a key and its square becomes the value.
- **Filtering**: An `if` condition can keep only selected items.
- **Helper function**: A function such as `square()` can make code clearer.

---

## 4. Code Demo

```python
numbers = [1, 2, 3, 4, 5]

squares_dict = {number: number ** 2 for number in numbers}
print(squares_dict)

even_squares_dict = {number: number ** 2 for number in numbers if number % 2 == 0}
print(even_squares_dict)
```

---

## 5. Expected Output / Behaviour

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{2: 4, 4: 16}
```

Small note: the comment in the original file includes even numbers up to 10, but the actual list contains only 1 through 5.

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
