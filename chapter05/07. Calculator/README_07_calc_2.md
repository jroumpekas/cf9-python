# 🧮 Calculator with Inner Functions, `reduce()`, and `match/case`

This lesson demonstrates a menu-driven calculator. The `calculate()` function returns a dictionary of operation functions, and `match/case` chooses which one to execute.

---

## 1. Learning Objectives

- Use inner functions for calculator operations.
- Use `functools.reduce()` for rolling calculations.
- Return a dictionary of functions.
- Use `match/case` as a menu dispatcher.
- Call functions stored inside a dictionary.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, loops, and simple terminal execution.

---

## 3. Key Concepts

- **Inner functions**: Functions defined inside `calculate()`.
- **Function dictionary**: A dictionary whose values are functions.
- **`reduce()`**: Combines values step by step.
- **`match/case`**: Clean menu-style branching.
- **Function call**: Use `operations['add']()` to execute the stored function.

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
import functools

def calculate(args):
    def plus():
        return functools.reduce(lambda x, y: x + y, args)

    def minus():
        return functools.reduce(lambda x, y: x - y, args)

    def mul():
        return functools.reduce(lambda x, y: x * y, args)

    def div():
        if 0 not in args[1:]:
            return args[0] / sum(args[1:])
        return "Division by zero error"

    return {
        "add": plus,
        "subtract": minus,
        "multiply": mul,
        "division": div
    }

def main():
    ints_list = [26, 5, 4, 3, 2, 1]
    operations = calculate(ints_list)

    choice = 1
    match choice:
        case 1:
            print(f"Addition result: {operations['add']()}")
        case 2:
            print(f"Subtraction result: {operations['subtract']()}")
        case 3:
            print(f"Multiplication result: {operations['multiply']()}")
        case 4:
            print(f"Division result: {operations['division']()}")
```

---

## 6. Expected Output

```text
Addition result: 41
```


## ⚠️ Known Issues in the Original Script

The original script should call the functions stored in the dictionary:

```python
operations["add"]()
```

not just access them:

```python
operations["add"]
```

Also, the original f-strings use double quotes inside double quotes, which can create syntax errors. Use single quotes inside the dictionary key, for example:

```python
f"{operations['add']()}"
```


---

## 7. Exercises

### 1. Level 1 — MCQ
What is stored in `operations["add"]`?

- a) A number
- b) A function
- c) A list
- d) A string

<details>
<summary>Solution</summary>

**Answer:** b) A function.
</details>

---

### 2. Level 2 — Coding
Add a `maximum()` operation.

<details>
<summary>Solution</summary>

```python
def maximum():
    return max(args)

operations = {
    "add": plus,
    "subtract": minus,
    "multiply": mul,
    "division": div,
    "maximum": maximum
}
```
</details>

---

## 8. Further Reading

- [Python Docs: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)
- [Python Docs: match statement](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)

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
