# 🎓 Your First Class: `Student`

This lesson is the gateway to **Object-Oriented Programming (OOP)** in Python. We define a `Student` class with a constructor (`__init__`), store data in **instance attributes**, and create an object from the class.

---

## 1. Learning Objectives

- Define a class with the `class` keyword.
- Write a constructor `__init__(self, ...)` that runs when an object is created.
- Understand the role of `self` (the current instance).
- Store data in **instance attributes** (`self.firstname`, `self.lastname`).
- Create (instantiate) an object and read its attributes.

---

## 2. Prerequisites

- Comfort with functions and parameters.
- Familiarity with f-strings for output.
- Awareness of type hints (`firstname: str`).

---

## 3. Key Concepts

- **Class**: A blueprint describing what data and behaviour its objects will have.
- **`__init__`**: The constructor — automatically called when you write `Student(...)`. It initialises the new object.
- **`self`**: The first parameter of every instance method; it refers to the object being created/used. You never pass it explicitly.
- **Instance attribute**: Data attached to a specific object, e.g. `self.firstname = firstname`.
- **Instantiation**: `student = Student("Bob", "M.")` creates a new `Student` object.
- **`pass`**: A placeholder that does nothing — the trailing `pass` statements in this file are harmless leftovers and can be removed.

---

## 4. Lecture Outline

### 0:00–0:08 — Declaring the Class
- `class Student:` plus a docstring describing it.

### 0:08–0:18 — The Constructor
- `def __init__(self, firstname: str, lastname: str):` assigns the two attributes.

### 0:18–0:26 — Creating an Object
- `student = Student("Bob", "M.")`.

### 0:26–0:32 — Reading Attributes
- `student.firstname` and `student.lastname` via f-strings.

---

## 5. Code Demos

```python
class Student:
    """
    A class that represents a student with a first name and a last name.

    Attributes:
        firstname (str): The first name of the student.
        lastname (str): The last name of the student.
    """

    def __init__(self, firstname: str, lastname: str):
        """Initialize a Student with the provided first and last name."""
        self.firstname = firstname
        self.lastname = lastname

def main():
    # Create a student object
    student = Student("Bob", "M.")

    print(f"First name: {student.firstname}")
    print(f"Last name: {student.lastname}")

    # TODO: friends

if __name__ == "__main__":
    main()
```

**Expected output:**

```
First name: Bob
Last name: M.
```

> 💡 **What is `self`, really?** When you write `Student("Bob", "M.")`, Python creates a blank object and passes it as `self` to `__init__`. So `self.firstname = firstname` means "store `'Bob'` on *this particular* student". A second student created later has its own separate `firstname`.

> 🧹 **About the `pass` statements:** the original file had two `pass` lines (inside `__init__` and after it). `pass` only matters when a block would otherwise be empty. Since `__init__` already has real statements, those `pass` lines do nothing and can be deleted.

---

## 6. Exercises

### 1. (Level 1, MCQ)
When is `__init__` called?
- a) Only when you call it by name
- b) Automatically, when you create an object
- c) Once per program
- d) Never

<details>
<summary>Solution</summary>

**Answer:** b) Automatically, the moment you write `Student(...)`.
</details>

---

### 2. (Level 1, Short Answer)
What does `self` refer to inside `__init__`?

<details>
<summary>Solution</summary>

`self` refers to the specific object currently being created/operated on. Each object gets its own `self`, so attributes set via `self.x = ...` belong to that one object.
</details>

---

### 3. (Level 2, Coding)
Add a third attribute `student_id` to the constructor and print it in `main`.

<details>
<summary>Solution</summary>

```python
class Student:
    def __init__(self, firstname, lastname, student_id):
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id

student = Student("Bob", "M.", 12345)
print(student.student_id)   # 12345
```
</details>

---

### 4. (Level 2, Coding)
Add a method `full_name(self)` that returns `"Bob M."`.

<details>
<summary>Solution</summary>

```python
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

print(Student("Bob", "M.").full_name())   # Bob M.
```
</details>

---

### 5. (Level 3, Coding)
Implement the `# TODO: friends`: give each student a `friends` list (starting empty) and an `add_friend(self, name)` method that appends to it.

<details>
<summary>Solution</summary>

```python
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.friends = []          # each student starts with no friends

    def add_friend(self, name):
        self.friends.append(name)

s = Student("Bob", "M.")
s.add_friend("Alice")
s.add_friend("Carol")
print(s.friends)   # ['Alice', 'Carol']
```
</details>

---

## 7. Further Reading

- [Python Tutorial: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Tutorial: Class and Instance Variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- [Python Docs: `object.__init__`](https://docs.python.org/3/reference/datamodel.html#object.__init__)

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
