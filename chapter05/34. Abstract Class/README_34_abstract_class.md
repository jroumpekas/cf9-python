# 🏗️ Abstract Classes with `ABC` and `abstractmethod`

This lesson demonstrates abstract base classes and how they define required methods for subclasses.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `34_abstract_class.py` | Defines abstract DAO and inventory APIs and implements concrete classes. |

---

## 1. Learning Objectives

- Import `ABC` and `abstractmethod`.
- Define abstract methods.
- Implement a concrete Student DAO.
- Implement a concrete Inventory class.
- Understand interface-like design in Python.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Abstract class**: Defines required behaviour for subclasses.
- **`@abstractmethod`**: Marks methods that concrete classes must implement.
- **DAO pattern**: Organizes insert, update, delete, and get operations.
- **Concrete implementation**: A subclass that provides working methods.

---

## 4. Code Demo

```python
from abc import ABC, abstractmethod

class AbstractStudentDAO(ABC):
    @abstractmethod
    def insert(self, student):
        raise NotImplementedError()

class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}

    def insert(self, student):
        student_id = student["id"]
        self.students[student_id] = student
```

---

## 5. Expected Output / Behaviour

```text
Inserted student with ID: 1
Updated student with ID: 1
Retrieved student: {'id': 1, 'name': 'John Smith'}
Deleted student with ID: 1
Added item: Laptop
Removed item: Laptop
Item not found: Tablet
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
