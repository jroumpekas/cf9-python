# 🔎 Finding Minimum Values in Dictionaries

This lesson shows how the `key` argument changes the behaviour of `min()` when working with dictionaries.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `28_find_min_value.py` | Uses `min()` with different key functions to find different minimum values. |

---

## 1. Learning Objectives

- Use `min()` on dictionary keys.
- Use `key=student_grades.get` to find the lowest grade.
- Find the alphabetically smallest key.
- Find the shortest name with `key=len`.
- Handle an empty dictionary safely.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **`min()`**: Finds the smallest item according to a comparison rule.
- **`key` argument**: Controls what Python compares.
- **Dictionary values**: `student_grades.get` returns each student grade.
- **Edge case**: The script checks if the dictionary is empty.

---

## 4. Code Demo

```python
student_with_lowest_grade = min(student_grades, key=student_grades.get)
student_with_smallest_name = min(student_grades)
student_with_shortest_name = min(student_grades, key=len)
```

---

## 5. Expected Output / Behaviour

```text
Student with the lowest grade: David (Grade: 68)
Student with the smallest name (alphabetically): Alice
Student with the shortest name: Bob (Length: 3)
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
