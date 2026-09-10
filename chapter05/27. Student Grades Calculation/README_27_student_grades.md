# 🎓 Student Average Grades with Dictionary Comprehension

This lesson calculates average grades and keeps only students above a threshold entered by the user.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `27_student_grades.py` | Filters students whose average grade is greater than a user-provided threshold. |

---

## 1. Learning Objectives

- Store students and grades in a dictionary.
- Validate integer input.
- Calculate averages.
- Filter dictionaries with comprehensions.
- Format averages to two decimals.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Input validation**: A loop repeats until the user enters an integer.
- **Average calculation**: Uses `sum(grades) / len(grades)`.
- **Threshold filtering**: Keeps only students above the given threshold.
- **Dictionary comprehension**: Builds a filtered dictionary of student averages.

---

## 4. Code Demo

```python
average_grades = {
    student: round(sum(grades) / len(grades), 2)
    for student, grades in students.items()
    if grades and sum(grades) / len(grades) > threshold
}
```

---

## 5. Expected Output / Behaviour

```text
Please insert the threshold (integer): 80

Students with average grade greater than 80:
Alice: 85.00
Bob: 87.33
Diana: 97.67
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
