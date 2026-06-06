# 🧮 String Formatting and the `math` Module

This lesson shows several ways to build formatted text in Python: simple concatenation, old-style `%` formatting, and the modern `str.format()` method. Along the way we use `math.pi` from the `math` module to practice controlling the number of decimal places and field widths.

---

## 1. Learning Objectives

- Import and use a value from the standard library (`math.pi`).
- Join strings and numbers with the `+` operator, converting numbers with `str()`.
- Format output using old-style `%` formatting (`%s`, `%d`, `%6.2f`).
- Format output using `str.format()` with positional, indexed, and precision specifiers.
- Reorder arguments inside a format string using index numbers.

---

## 2. Prerequisites

- Familiarity with variables and the primitive types.
- Comfort calling `print()` with one or more arguments.
- Awareness that numbers and strings are different types.

---

## 3. Key Concepts

- **`import math`**: Brings in the math module so you can use `math.pi`.
- **Concatenation (`+`)**: Joins strings; numbers must first be turned into strings with `str()`.
- **`%` formatting**: A placeholder style where `%s` is a string, `%d` an integer, and `%6.2f` a float in a 6-wide field with 2 decimals.
- **`str.format()`**: A method where `{}` placeholders are filled by the arguments to `format()`.
- **Format spec**: Inside the braces, `{:.3f}` sets 3 decimals and `{0:2d}` sets index 0 as a 2-wide integer.
- **Index reordering**: `{1}` and `{0}` let you place arguments in any order.

---

## 4. Lecture Outline

### 0:00–0:05 — Importing `math` and Printing `pi`
- `import math`, then `print("PI =", math.pi)`.

### 0:05–0:11 — String Concatenation
- Building a sentence with `+` and converting `age` with `str(age)`.

### 0:11–0:18 — Old-Style `%` Formatting
- `"%6.2f" % math.pi` for width and precision.
- `"%s is %d years old" % (name, age)` with multiple values.

### 0:18–0:26 — Modern `str.format()`
- Precision: `"{:.3f}".format(math.pi)`.
- Width: `"{0:2d}".format(age)`.
- Reordering: `"{1} is {0} years old".format(name, age)`.

---

## 5. Code Demos

```python
import math
name = "Alice"
age = 20

print("CF9")

print("PI =", math.pi)

print(name + " is " + str(age) + " years old. ")

print("PI = %6.2f" % math.pi)

print("%s is %d years old" % (name, age))

print("Python 3 style using string format")
print("Age is {0:2d}".format(age))
print("PI is {:.3f}".format(math.pi))

print("{1} is {0} years old".format(name, age))
```

**Expected output:**

```
CF9
PI = 3.141592653589793
Alice is 20 years old. 
PI =   3.14
Alice is 20 years old
Python 3 style using string format
Age is 20
PI is 3.142
20 is Alice years old
```

> 💡 Notice the very last line: `{1}` came before `{0}`, so the arguments printed in reverse order — a handy reason to use indexes.

---

## 6. Exercises

### 1. (Level 1, MCQ)
In `"%d"`, what type of value does `%d` expect?
- a) A string
- b) A float
- c) An integer
- d) A boolean

<details>
<summary>Solution</summary>

**Answer:** c) An integer.
</details>

---

### 2. (Level 1, Short Answer)
Why does `print("Age: " + age)` fail when `age = 20`, while `print("Age: " + str(age))` works?

<details>
<summary>Solution</summary>

You cannot concatenate a string with an integer directly. `str(age)` converts the number to a string first, so both sides of `+` are strings.
</details>

---

### 3. (Level 2, Coding)
Using `str.format()`, print `math.pi` rounded to 2 decimal places, like `Pi rounded: 3.14`.

<details>
<summary>Solution</summary>

```python
import math
print("Pi rounded: {:.2f}".format(math.pi))
```
</details>

---

### 4. (Level 2, Coding)
Given `city = "Athens"` and `temp = 31`, use `%` formatting to print:
`Athens is 31 degrees`

<details>
<summary>Solution</summary>

```python
city = "Athens"
temp = 31
print("%s is %d degrees" % (city, temp))
```
</details>

---

### 5. (Level 3, Coding)
Using indexed placeholders, print `name` and `age` in this exact order:
`20 belongs to Alice`

<details>
<summary>Solution</summary>

```python
name = "Alice"
age = 20
print("{1} belongs to {0}".format(name, age))
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `math` module](https://docs.python.org/3/library/math.html)
- [Python Official Documentation: Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
- [Python Tutorial: Fancier Output Formatting](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)

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
