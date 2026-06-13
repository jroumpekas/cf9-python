# ✅ Truthy and Falsy Values & Chained Comparisons

This lesson explains which values Python treats as `False` in a boolean context (**falsy**) and which it treats as `True` (**truthy**). It also demonstrates how to validate a range with the standard `and` operator and with Python's elegant **chained comparison** syntax.

---

## 1. Learning Objectives

- List the built-in **falsy** values in Python.
- Understand that every other value is **truthy**.
- Use `type()` to inspect the type of an empty `dict` and an empty `set`.
- Validate that a number falls inside a range using `and`.
- Rewrite the same check using a **chained comparison** (`0 <= a <= 10`).

---

## 2. Prerequisites

- Familiarity with variables and the primitive types (`int`, `float`, `str`).
- Comfort writing a basic `if` / `else` block.
- Awareness of comparison operators (`<`, `<=`, `>=`, `==`).

---

## 3. Key Concepts

- **Falsy values**: `0`, `0.0`, `0j`, `""`, `[]`, `()`, `{}`, `set()`, `None`, and `False` all evaluate to `False` when used in a condition.
- **Truthy values**: Everything else (any non-zero number, any non-empty container, etc.) evaluates to `True`.
- **`{}` vs `set()`**: `{}` creates an **empty dictionary**, *not* an empty set. To create an empty set you must call `set()`.
- **`type(x)`**: Returns the class of an object, e.g. `<class 'dict'>` or `<class 'set'>`.
- **Chained comparison**: `0 <= a <= 10` is read as `(0 <= a) and (a <= 10)`. It is shorter, faster, and evaluates `a` only once.

---

## 4. Lecture Outline

### 0:00–0:05 — The Falsy Family
- Reviewing the list of falsy values written in the comment.

### 0:05–0:12 — Empty Dict vs Empty Set
- `empty_dict = {}` → `<class 'dict'>`.
- `empty_set = set()` → `<class 'set'>`.

### 0:12–0:20 — Range Check with `and`
- `if a >= 0 and a <= 10:` prints `is valid`.

### 0:20–0:28 — The Pythonic Chained Comparison
- `if 0 <= a <= 10:` does the same thing, more cleanly.

---

## 5. Code Demos

```python
# Falsy - Truthy values
# Falsy examples: 0, 0.0, 0j, "", [], (), False, None, {}

empty_dict = {}
print(type(empty_dict))

empty_set = set()
print(type(empty_set))

print("-------------\n")

a = 5

if a >= 0 and a <= 10:
    print("is valid")
else:
    print("is not valid")

# chained comparison
if 0 <= a <= 10:
    print("is valid")
else:
    print("is not valid")
```

**Expected output:**

```
<class 'dict'>
<class 'set'>
-------------

is valid
is valid
```

> 💡 **Why is `{}` a dict and not a set?** Dictionaries existed in Python long before set literals. To keep backward compatibility, the empty braces `{}` were reserved for the empty dictionary, so the only way to make an empty set is `set()`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which of the following is **truthy**?
- a) `0`
- b) `""`
- c) `[0]`
- d) `None`

<details>
<summary>Solution</summary>

**Answer:** c) `[0]`. The list is not empty (it contains one element, the number `0`), so the *list itself* is truthy — even though its single element is falsy.
</details>

---

### 2. (Level 1, Short Answer)
What does `print(type({}))` output, and how would you create a truly empty **set**?

<details>
<summary>Solution</summary>

`print(type({}))` outputs `<class 'dict'>`. To create an empty set you must call `set()` — for example `empty_set = set()`.
</details>

---

### 3. (Level 2, Coding)
Write an `if`/`else` that prints `"empty"` when a variable `data` is any falsy value and `"has content"` otherwise. Test it with `data = []`.

<details>
<summary>Solution</summary>

```python
data = []
if data:
    print("has content")
else:
    print("empty")
```
Output: `empty`
</details>

---

### 4. (Level 2, Coding)
Rewrite the check `if score >= 50 and score <= 100:` using a chained comparison.

<details>
<summary>Solution</summary>

```python
if 50 <= score <= 100:
    print("pass")
```
</details>

---

### 5. (Level 3, Coding)
Given `temp = 18`, print `"comfortable"` if the temperature is strictly between 16 and 25 (exclusive on both ends) using a single chained comparison, otherwise print `"adjust thermostat"`.

<details>
<summary>Solution</summary>

```python
temp = 18
if 16 < temp < 25:
    print("comfortable")
else:
    print("adjust thermostat")
```
Output: `comfortable`
</details>

---

## 7. Further Reading

- [Python Docs: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Python Docs: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
- [Python Docs: Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

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
