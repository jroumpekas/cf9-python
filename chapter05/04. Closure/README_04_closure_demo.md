# 🔐 Closure Demo — Department ID Generator

This lesson demonstrates closures and `nonlocal` using a department ID generator. Each returned function remembers its own counter.

---

## 1. Learning Objectives

- Understand closures.
- Use `nonlocal` inside an inner function.
- Preserve state between calls.
- Create independent ID generators.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, loops, and simple terminal execution.

---

## 3. Key Concepts

- **Closure**: An inner function that remembers values from its enclosing scope.
- **`nonlocal`**: Allows modification of an enclosing variable.
- **State**: Data remembered between calls.
- **Function factory**: A function that returns another function.

---

## 4. Lecture Outline

### 0:00–0:08 — Introduce the Example
- Read the input data and identify the goal of the script.

### 0:08–0:20 — Main Logic
- Walk through the important Python concepts used in the code.

### 0:20–0:32 — Output and Behaviour
- Run the script and explain the result.

### 0:32–0:40 — Improvements
- Discuss small fixes, cleaner structure, or extra validation.

---

## 5. Code Demo

```python
def department_id_generator(department):
    last_id = 0

    def generate_id():
        nonlocal last_id
        last_id += 1
        return f"{department}-{last_id}", last_id

    return generate_id

def main():
    python_id_gen = department_id_generator("Python")
    android_id_gen = department_id_generator("Android")

    print(python_id_gen())
    print(python_id_gen())
    print(python_id_gen())

    print("-------------------")

    print(android_id_gen())
    print(android_id_gen())
```

---

## 6. Expected Output

```text
('Python-1', 1)
('Python-2', 2)
('Python-3', 3)
-------------------
('Android-1', 1)
('Android-2', 2)
```


---

## 7. Exercises

### 1. Level 1 — Short Answer
Why does `python_id_gen()` remember the previous ID?

<details>
<summary>Solution</summary>

Because it is a closure and keeps access to `last_id` from the outer function.
</details>

---

### 2. Level 2 — Coding
Create a `Java` generator and print two IDs.

<details>
<summary>Solution</summary>

```python
java_id_gen = department_id_generator("Java")
print(java_id_gen())
print(java_id_gen())
```
</details>

---

## 8. Further Reading

- [Python Docs: nonlocal](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement)

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
