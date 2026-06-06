# 🟦 Primitive Data Types in Python

This lesson introduces Python's four core primitive data types — `int`, `float`, `bool`, and `str` — by declaring one variable of each type and printing their values. We focus on how to assign values, how Python infers the type automatically, and how the `print()` function displays them individually and together.

---

## 1. Learning Objectives

- Declare variables of the four primitive types: integer, float, boolean, and string.
- Understand how Python infers a variable's type from the value you assign (dynamic typing).
- Display values using `print()`, both one per line and several on the same line.
- Recognize how `print()` separates multiple arguments with spaces by default.
- Use a printed separator line to make console output easier to read.

---

## 2. Prerequisites

- Python installed and the ability to run a `.py` file from an IDE or terminal.
- Basic understanding of what a variable is.
- Familiarity with running a script and reading console output.

---

## 3. Key Concepts

- **Variable**: A named reference to a value stored in memory (e.g. `num = 10`).
- **`int`**: A whole number with no decimal part, such as `10`.
- **`float`**: A number with a decimal point, such as `1.85`.
- **`bool`**: A truth value, either `True` or `False`.
- **`str`**: A sequence of characters enclosed in quotes, such as `"Hello Coding Factory"`.
- **Dynamic typing**: You do not declare the type explicitly; Python determines it from the assigned value.
- **`print()` arguments**: When given several values, `print()` shows them on one line separated by a single space.

---

## 4. Lecture Outline

### 0:00–0:05 — What Are Primitive Types?
- The idea of a "primitive" (basic, built-in) type.
- The four we use here: `int`, `float`, `bool`, `str`.

### 0:05–0:12 — Declaring One Variable of Each Type
- `num = 10` → integer.
- `height = 1.85` → float.
- `is_raining = True` → boolean (note the capital `T`).
- `hello_message = "Hello Coding Factory"` → string.

### 0:12–0:18 — Printing Values Individually
- Calling `print()` once per variable.
- Each value appears on its own line.

### 0:18–0:25 — Printing on a Single Line and Using a Separator
- Passing all variables to one `print()` call.
- How the default space separator works.
- Printing a line of dashes to visually divide output blocks.

---

## 5. Code Demos

```python
# Define an integer variable with a value of 10
num = 10

# Define a floating-point variable for height in meters
height = 1.85

# Boolean variable to indicate whether it is raining or not
is_raining = True

# String variable containing a welcome message
hello_message = "Hello Coding Factory"

# Print individual variables to the console
print(num)
print(height)
print(is_raining)
print(hello_message)

# Print a separator to distinguish different outputs
print("--------------------")

# Print all variables in one line separated by spaces
print(num, height, is_raining, hello_message)
```

**Expected output:**

```
10
1.85
True
Hello Coding Factory
--------------------
10 1.85 True Hello Coding Factory
```

> 💡 Tip: You can confirm a variable's type at any time with `type(num)`, which returns `<class 'int'>`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which of the following values is a `bool` in Python?
- a) `"True"`
- b) `1.0`
- c) `True`
- d) `0xA`

<details>
<summary>Solution</summary>

**Answer:** c) `True`. Option a) is a string, b) is a float, and d) is an integer written in hexadecimal.
</details>

---

### 2. (Level 1, Short Answer)
What is the output of the following code?

```python
a = 5
b = 2.5
print(a, b)
```

<details>
<summary>Solution</summary>

**Output:** `5 2.5` — the two values appear on one line separated by a single space.
</details>

---

### 3. (Level 2, Coding)
Declare a variable `temperature` with the float value `36.6` and print the line:
`Body temperature: 36.6`

<details>
<summary>Solution</summary>

```python
temperature = 36.6
print("Body temperature:", temperature)
```
</details>

---

### 4. (Level 2, Coding)
Create one variable of each primitive type describing a book: a title (`str`), number of pages (`int`), price (`float`), and whether it is available (`bool`). Print all four on a single line.

<details>
<summary>Solution</summary>

```python
title = "Clean Code"
pages = 464
price = 29.99
available = True

print(title, pages, price, available)
```
</details>

---

### 5. (Level 3, Coding)
Using the variables from this lesson, print the booleans first, then a dashed separator, then the text values. Match this output:

```
True
--------------------
Hello Coding Factory
```

<details>
<summary>Solution</summary>

```python
is_raining = True
hello_message = "Hello Coding Factory"

print(is_raining)
print("--------------------")
print(hello_message)
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Official Documentation: `print()` function](https://docs.python.org/3/library/functions.html#print)
- [Python Tutorial: An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)

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
