# ⚡ Lambda Function Demo

This lesson demonstrates how to define a simple **lambda function**.

A lambda function is a small anonymous function that is often used for short one-line operations.

---

## 1. Learning Objectives

- Understand what a lambda function is.
- Create a lambda function with two parameters.
- Use the exponentiation operator `**`.
- Compare lambda functions with normal functions.
- Know when lambda functions are useful.

---

## 2. Prerequisites

- Functions.
- Variables.
- Arithmetic operators.

---

## 3. Key Concepts

- **Lambda function**: A small anonymous function.
- **Anonymous function**: A function without a formal `def` name.
- **Expression**: Lambda functions contain one expression.
- **Exponentiation**: `base ** exp`.
- **Callable variable**: A variable can reference a function.

---

## 4. Lecture Outline

### 0:00–0:08 — Lambda Syntax
- Introduce `lambda base, exp: base ** exp`.

### 0:08–0:16 — Assigning a Lambda
- Store the lambda in `power_to`.

### 0:16–0:24 — Calling the Lambda
- Call `power_to(2, 10)`.

### 0:24–0:32 — Normal Function Equivalent
- Compare with a regular `def`.

---

## 5. Code Demo

```python
power_to = lambda base, exp: base ** exp

print(power_to(2, 10))
```

Equivalent normal function:

```python
def power_to(base, exp):
    return base ** exp
```

---

## 6. Expected Output

```text
1024
```

---

## 7. Exercises

### 1. Level 1 — MCQ
What does this lambda return?

```python
lambda base, exp: base ** exp
```

- a) The sum of base and exp
- b) The base raised to the exponent
- c) The exponent divided by base
- d) A string

<details>
<summary>Solution</summary>

**Answer:** b) The base raised to the exponent.
</details>

---

### 2. Level 1 — Short Answer
What is the result of `power_to(3, 2)`?

<details>
<summary>Solution</summary>

It returns `9`.
</details>

---

### 3. Level 2 — Coding
Create a lambda that doubles a number.

<details>
<summary>Solution</summary>

```python
double = lambda x: x * 2
print(double(5))
```
</details>

---

### 4. Level 2 — Short Answer
When should lambda functions be used?

<details>
<summary>Solution</summary>

They are useful for short, simple functions, especially when passed into functions like `map()`, `filter()`, or `sorted()`.
</details>

---

## 8. Further Reading

- [Python Docs: Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
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
