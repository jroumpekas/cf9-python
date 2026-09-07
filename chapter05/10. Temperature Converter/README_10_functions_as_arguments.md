# 🧮 Functions as Arguments — Calculator Demo

This lesson demonstrates how to pass functions as arguments in Python.

The script defines a generic `calculator()` function that receives two numbers and an operation function, then applies that operation to the numbers.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `10_func_as_args.py` | Calculator that accepts another function as the operation argument. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Understand that functions are first-class objects in Python.
- Pass a function as an argument to another function.
- Create reusable calculator logic.
- Define separate operation functions.
- Handle errors with `try / except`.
- Raise a `ValueError` for division by zero.

---

## 2. Prerequisites

- Functions.
- Parameters and return values.
- Basic arithmetic.
- Exceptions.
- `try / except`.

---

## 3. Key Concepts

### Functions as First-Class Objects

In Python, functions can be:

- stored in variables,
- passed as arguments,
- returned from other functions,
- stored in lists or dictionaries.

Example:

```python
calculator(5, 3, add)
```

Here, `add` is passed as a function object.

---

### Higher-Order Function

A function that accepts another function as an argument is called a higher-order function.

```python
def calculator(n1, n2, operation):
    return operation(n1, n2)
```

---

### Operation Functions

Each arithmetic operation is defined separately:

```python
def add(no1, no2):
    return no1 + no2
```

This keeps the calculator flexible.

---

## 4. Lecture Outline

### 0:00–0:08 — Calculator Function
- Define a function that receives another function.

### 0:08–0:20 — Arithmetic Operations
- Define `add`, `subtract`, `multiply`, and `divide`.

### 0:20–0:32 — Passing Functions
- Call `calculator(5, 3, add)`.

### 0:32–0:42 — Error Handling
- Handle invalid operations and division by zero.

---

## 5. Code Demo

```python
def calculator(n1, n2, operation):
    try:
        return operation(n1, n2)
    except TypeError as e:
        print(f"Error: {e}. Ensure the 'operation' is a function taking two numbers.")

def add(no1, no2):
    return no1 + no2

def subtract(no1, no2):
    return no1 - no2

def multiply(no1, no2):
    return no1 * no2

def divide(no1, no2):
    if no2 == 0:
        raise ValueError("Division by zero is not allowed.")
    return no1 / no2

def main():
    print("Addition:", calculator(5, 3, add))
    print("Subtraction:", calculator(5, 3, subtract))
    print("Multiplication:", calculator(5, 3, multiply))
    print("Division:", calculator(5, 3, divide))

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output

```text
Addition: 8
Subtraction: 2
Multiplication: 15
Division: 1.6666666666666667
```

---

## 7. Important Note About Division by Zero

The `divide()` function explicitly prevents division by zero:

```python
if no2 == 0:
    raise ValueError("Division by zero is not allowed.")
```

A test example:

```python
print(calculator(5, 0, divide))
```

would raise:

```text
ValueError: Division by zero is not allowed.
```

---

## 8. Suggested Improvement

The `calculator()` function currently catches only `TypeError`.

To also handle division by zero gracefully, you can add `ValueError`:

```python
def calculator(n1, n2, operation):
    try:
        return operation(n1, n2)
    except TypeError as e:
        print(f"Type error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
```

---

## 9. Exercises

### 1. Level 1 — MCQ

What is passed as the third argument here?

```python
calculator(5, 3, add)
```

- a) A string
- b) A function
- c) A list
- d) A dictionary

<details>
<summary>Solution</summary>

**Answer:** b) A function.
</details>

---

### 2. Level 1 — Short Answer

Why is this calculator flexible?

<details>
<summary>Solution</summary>

Because it can apply any operation function that receives two numbers.
</details>

---

### 3. Level 2 — Coding

Add a modulo operation.

<details>
<summary>Solution</summary>

```python
def modulo(no1, no2):
    return no1 % no2

print("Modulo:", calculator(5, 3, modulo))
```
</details>

---

### 4. Level 2 — Coding

Use a lambda directly as the operation.

<details>
<summary>Solution</summary>

```python
print(calculator(5, 3, lambda x, y: x ** y))
```
</details>

---

### 5. Level 3 — Challenge

Create a dictionary of operations and let the user choose one.

<details>
<summary>Solution</summary>

```python
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

choice = "add"
print(calculator(5, 3, operations[choice]))
```
</details>

---

## 10. Further Reading

- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Docs: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

---

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

---

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
