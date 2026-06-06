# 🔢 Integer Limits and `sys.maxsize`

This lesson looks at how large integers can get in Python and introduces `sys.maxsize` from the `sys` module. An important takeaway is that Python integers have **arbitrary precision** — they are not capped by a fixed maximum the way they are in many other languages — so `sys.maxsize` means something more specific than "the biggest possible integer".

---

## 1. Learning Objectives

- Import and read a value from the `sys` module (`sys.maxsize`).
- Understand what `sys.maxsize` actually represents on a given platform.
- Learn that Python `int` values are unbounded (limited only by available memory).
- Convert a number to a string and measure its length with `len(str(n))`.
- Distinguish between platform-dependent values and true language limits.

---

## 2. Prerequisites

- Comfort importing a module and printing values.
- Knowing the `int` and `str` types.
- Familiarity with the `len()` function on strings.

---

## 3. Key Concepts

- **`sys.maxsize`**: The largest value a variable of the platform's native "size" type can hold — typically `2**63 - 1` on a 64-bit system. It is mainly the maximum size for things like list indices, **not** a hard ceiling on integers.
- **Arbitrary-precision integers**: Python `int` has no fixed maximum or minimum; values can grow as large as memory allows.
- **`str(n)`**: Converts a number to its text form so it can be measured or displayed.
- **`len(...)`**: Counts characters; on `str(max_int)` it tells you how many digits the number has.

---

## 4. Lecture Outline

### 0:00–0:07 — Importing `sys` and Reading `maxsize`
- `import sys` and `print("Max int:", sys.maxsize)`.

### 0:07–0:14 — What `maxsize` Really Means
- It is platform-dependent (commonly `2**63 - 1`).
- Why it is not the same as "the maximum integer in Python".

### 0:14–0:20 — Python Integers Have No Fixed Limit
- You can compute `sys.maxsize ** 2` and Python handles it fine.
- So there is no real "minimum int" either.

### 0:20–0:26 — Counting Digits with `len(str(...))`
- Turning the number into a string and measuring its length.

---

## 5. Code Demos

```python
import sys

max_int = sys.maxsize
print("Max int:", max_int)

min_int = sys.maxsize - 1
print("Min int:", min_int)

print(len(str(max_int)))
```

**Expected output (on a typical 64-bit system):**

```
Max int: 9223372036854775807
Min int: 9223372036854775806
19
```

(The final line prints `19`, because `9223372036854775807` has 19 digits.)

> ⚠️ **A note on `min_int`.** In this demo `min_int = sys.maxsize - 1` is simply `sys.maxsize` minus one — it is **not** the smallest possible integer in Python. Unlike languages such as C or Java, Python integers are unbounded, so there is no true minimum or maximum `int`. `sys.maxsize` is best understood as a platform word-size limit, not a cap on integer values. To prove integers can exceed it, try:
>
> ```python
> print(sys.maxsize * sys.maxsize)  # far larger than maxsize, and still valid
> ```

---

## 6. Exercises

### 1. (Level 1, MCQ)
On a 64-bit system, `sys.maxsize` is usually equal to:
- a) `2**31 - 1`
- b) `2**63 - 1`
- c) `2**64`
- d) Infinity

<details>
<summary>Solution</summary>

**Answer:** b) `2**63 - 1`.
</details>

---

### 2. (Level 1, Short Answer)
Does Python raise an error if you compute a number larger than `sys.maxsize`?

<details>
<summary>Solution</summary>

No. Python integers have arbitrary precision, so larger values are handled normally without overflow.
</details>

---

### 3. (Level 2, Coding)
Print how many digits are in `sys.maxsize`.

<details>
<summary>Solution</summary>

```python
import sys
print(len(str(sys.maxsize)))
```
</details>

---

### 4. (Level 2, Coding)
Compute and print `sys.maxsize` squared, then print how many digits that result has.

<details>
<summary>Solution</summary>

```python
import sys
big = sys.maxsize ** 2
print(big)
print("Digits:", len(str(big)))
```
</details>

---

### 5. (Level 3, Short Answer + Coding)
Explain in one sentence why "minimum int" is not a meaningful concept in Python, then write code that prints a negative number much smaller than `-sys.maxsize`.

<details>
<summary>Solution</summary>

Because Python integers are unbounded, there is no fixed smallest value — they can be as negative as memory allows.

```python
import sys
print(-(sys.maxsize ** 2))
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize)
- [Python Official Documentation: Integer (numeric types)](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [PEP 237: Unifying Long Integers and Integers](https://peps.python.org/pep-0237/)

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
