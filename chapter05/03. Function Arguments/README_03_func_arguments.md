# 🧰 Function Arguments Demo

This lesson demonstrates positional arguments, optional parameters, `*args`, and `**kwargs` in one function.

---

## 1. Learning Objectives

- Understand positional arguments.
- Use optional/default parameters.
- Collect extra positional arguments with `*args`.
- Collect extra keyword arguments with `**kwargs`.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, loops, and simple terminal execution.

---

## 3. Key Concepts

- **Positional arguments**: Values matched by their position.
- **Optional parameters**: Parameters with default values.
- **`*args`**: Extra positional values as a tuple.
- **`**kwargs`**: Extra keyword values as a dictionary.

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
def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs):
    print("Pos arg1:", pos_arg1)
    print("Pos arg2:", pos_arg2)

    print("Opt arg1:", opt_arg1)
    print("Opt arg2:", opt_arg2)

    if args:
        print("Additional positional arguments:")
        for arg in args:
            print(arg)

    if kwargs:
        print("Additional keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

def main():
    test_args_func("Hello", "CF", opt_arg1="Python", opt_arg2=100)

    print("-" * 61)

    test_args_func(
        "Hello", "CF",
        100, 200,
        300, 400, 500,
        language="Python",
        lesson="Android Development"
    )
```

---

## 6. Expected Output

```text
Pos arg1: Hello
Pos arg2: CF
Opt arg1: Python
Opt arg2: 100
-------------------------------------------------------------
Pos arg1: Hello
Pos arg2: CF
Opt arg1: 100
Opt arg2: 200
Additional positional arguments:
300
400
500
Additional keyword arguments:
language: Python
lesson: Android Development
```


---

## 7. Exercises

### 1. Level 1 — MCQ
What does `**kwargs` collect?

- a) Extra positional arguments
- b) Extra keyword arguments
- c) Only numbers
- d) Only lists

<details>
<summary>Solution</summary>

**Answer:** b) Extra keyword arguments.
</details>

---

### 2. Level 2 — Coding
Call the function with a keyword argument called `topic`.

<details>
<summary>Solution</summary>

```python
test_args_func("A", "B", topic="Python")
```
</details>

---

## 8. Further Reading

- [Python Docs: Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)

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
