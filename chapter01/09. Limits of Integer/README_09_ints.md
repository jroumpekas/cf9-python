# ➕ How `+` Works on Integers (the `__add__` Method)

This short lesson reveals what really happens when you write `a + b`. In Python, operators are backed by special "dunder" (double-underscore) methods, so `a + b` is actually a call to `a.__add__(b)`. We prove it by getting the same result both ways.

---

## 1. Learning Objectives

- Add two integers using the `+` operator.
- Understand that `+` is implemented by the special method `__add__`.
- Call `a.__add__(b)` directly and confirm it matches `a + b`.
- Recognize that "dunder" methods power Python's operators.
- Appreciate that everything in Python, including `int`, is an object with methods.

---

## 2. Prerequisites

- Knowing how to declare integer variables.
- Familiarity with `print()`.
- A basic idea of what a method is (a function attached to an object).

---

## 3. Key Concepts

- **Operator**: A symbol like `+` that performs an operation on values.
- **Dunder method**: A method named with leading and trailing double underscores, e.g. `__add__`, used by Python internally.
- **`a + b` ⇔ `a.__add__(b)`**: The operator is syntactic sugar for the method call.
- **Everything is an object**: Even an integer like `10` has methods you can call.

---

## 4. Lecture Outline

### 0:00–0:06 — Normal Addition
- `a = 10`, `b = 20`, then `print(a + b)`.

### 0:06–0:14 — What `+` Calls Behind the Scenes
- Introducing `__add__`.
- `print(a.__add__(b))` gives the same result.

### 0:14–0:20 — Why This Matters
- Operators are customizable via dunder methods (a preview of operator overloading).

---

## 5. Code Demos

```python
a = 10
b = 20

print(a + b)

print(a.__add__(b))
```

**Expected output:**

```
30
30
```

> 💡 Both lines print `30`. The first uses the friendly `+` syntax; the second calls the method that `+` uses internally. You will almost always write `a + b` — but knowing about `__add__` explains how Python lets your own classes support `+` later on.

---

## 6. Exercises

### 1. (Level 1, MCQ)
`a + b` is equivalent to which method call?
- a) `a.add(b)`
- b) `a.__add__(b)`
- c) `add(a, b)`
- d) `a.__plus__(b)`

<details>
<summary>Solution</summary>

**Answer:** b) `a.__add__(b)`.
</details>

---

### 2. (Level 1, Short Answer)
What does `print((5).__add__(3))` output?

<details>
<summary>Solution</summary>

`8` — it is the same as `5 + 3`.
</details>

---

### 3. (Level 2, Coding)
Without using the `+` symbol, add `7` and `12` and print the result.

<details>
<summary>Solution</summary>

```python
print((7).__add__(12))  # 19
```
</details>

---

### 4. (Level 2, Short Answer)
Strings also support `+`. What dunder method do you think `"a" + "b"` calls?

<details>
<summary>Solution</summary>

`"a".__add__("b")` — the same `__add__` method, defined on the `str` type to mean concatenation.
</details>

---

### 5. (Level 3, Coding)
Show that subtraction has its own dunder method by computing `20 - 5` via the method instead of the operator.

<details>
<summary>Solution</summary>

```python
print((20).__sub__(5))  # 15
```
</details>

---

## 7. Further Reading

- [Python Data Model: Emulating numeric types (`__add__`, etc.)](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)
- [Python Official Documentation: Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python Tutorial: Classes (special methods preview)](https://docs.python.org/3/tutorial/classes.html)

---

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Dimitris - your.email@example.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a> (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
