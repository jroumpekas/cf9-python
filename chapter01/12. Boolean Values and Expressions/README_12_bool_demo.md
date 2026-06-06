# 🔘 Booleans and the Truth About `True`

This lesson works with boolean values, the `or` operator, and a surprising-but-useful fact: in Python, `bool` is a subtype of `int`, so `True` behaves like `1` and `False` like `0` in arithmetic. We confirm this with a couple of small experiments.

---

## 1. Learning Objectives

- Declare boolean variables and print their type and value.
- Combine booleans with the `or` operator.
- Understand that `bool` is a subclass of `int` in Python.
- Predict the result of arithmetic involving `True` and `False`.
- Read `type(x)` output for booleans.

---

## 2. Prerequisites

- Knowing the boolean literals `True` and `False`.
- Familiarity with `print()` and `type()`.
- Basic arithmetic operators.

---

## 3. Key Concepts

- **`bool`**: A type with exactly two values, `True` and `False`.
- **`or`**: Returns `True` if at least one operand is truthy.
- **`bool` is a subclass of `int`**: `True` equals `1` and `False` equals `0`.
- **Arithmetic with booleans**: `True + True` is `2`; `True * 15` is `15`.
- **`type(x)`**: Shows `<class 'bool'>` for boolean values.

---

## 4. Lecture Outline

### 0:00–0:06 — Declaring Booleans
- `a = True`, `b = False`, then printing their types and values.

### 0:06–0:12 — The `or` Operator
- `result = a or b` evaluates to `True`.

### 0:12–0:20 — Booleans Are Integers in Disguise
- `True + True` → `2`.
- `True * 15` → `15`.
- Why this works: `bool` inherits from `int`.

---

## 5. Code Demos

```python
a = True
b = False

print(type(a), ":", a)
print(type(b), ":", b)

result = a or b
print(result)

# Extra useful and nice information!
print(True + True)
print(True * 15)
```

**Expected output:**

```
<class 'bool'> : True
<class 'bool'> : False
True
2
15
```

> 💡 `True + True` gives `2` because `True` counts as `1`. This is genuinely handy: you can count how many conditions are true by adding booleans together, e.g. `sum([x > 0, y > 0, z > 0])`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `True + False` evaluate to?
- a) `True`
- b) `1`
- c) `0`
- d) An error

<details>
<summary>Solution</summary>

**Answer:** b) `1` (because `True` is `1` and `False` is `0`).
</details>

---

### 2. (Level 1, Short Answer)
What is the result of `False or False`, and what is its type?

<details>
<summary>Solution</summary>

`False`, of type `bool`.
</details>

---

### 3. (Level 2, Coding)
Use boolean arithmetic to count how many of the values `5`, `-2`, and `8` are positive, and print the count.

<details>
<summary>Solution</summary>

```python
count = (5 > 0) + (-2 > 0) + (8 > 0)
print(count)  # 2
```
</details>

---

### 4. (Level 2, Short Answer)
Explain why `True * 15` equals `15`.

<details>
<summary>Solution</summary>

Because `bool` is a subclass of `int` and `True` equals `1`, so `True * 15` is the same as `1 * 15`.
</details>

---

### 5. (Level 3, Coding)
Given a list of exam scores, print how many are passing (>= 50) using boolean summation.

<details>
<summary>Solution</summary>

```python
scores = [42, 75, 50, 33, 91]
passing = sum(score >= 50 for score in scores)
print("Passing:", passing)  # 3
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Boolean values](https://docs.python.org/3/library/stdtypes.html#boolean-values)
- [Python Official Documentation: Boolean Operations (`and`, `or`, `not`)](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python Data Model: `bool` as a subclass of `int`](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

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
