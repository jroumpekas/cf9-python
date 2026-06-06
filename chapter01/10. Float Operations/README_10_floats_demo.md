# 🔬 Floats, `type()`, and Scientific Notation

This lesson introduces floating-point numbers, how to inspect a value's type with `type()`, and how to write very small numbers using scientific (exponential) notation. It also contains a subtle f-string typo that is worth studying, because it shows how easy it is to print something other than what you intended.

---

## 1. Learning Objectives

- Declare floating-point variables and display them.
- Inspect a value's type at runtime with `type()`.
- Read and write numbers in scientific notation (e.g. `2.5e-3`).
- Embed expressions inside f-strings with `{...}`.
- Spot a common f-string mistake where the value prints but the function call is missing.

---

## 2. Prerequisites

- Knowing the difference between `int` and `float`.
- Basic f-string usage.
- Comfort reading console output carefully.

---

## 3. Key Concepts

- **`float`**: A number with a fractional part, stored in binary floating-point form.
- **`type(x)`**: Returns the type object of `x`, e.g. `<class 'float'>`.
- **Scientific notation**: `2.5e-3` means 2.5 × 10⁻³ = `0.0025`.
- **f-string expressions**: `{type(x)}` runs the call; `{x}` just inserts the value.
- **Literal text vs. code in f-strings**: Anything outside `{}` is printed exactly as typed.

---

## 4. Lecture Outline

### 0:00–0:06 — Declaring a Float and Printing It
- `PI = 3.1415926`, then `print("Value of PI:", PI)`.

### 0:06–0:12 — Inspecting the Type
- `f"Type of PI: {type(PI)}"` correctly shows `<class 'float'>`.

### 0:12–0:18 — Scientific Notation
- `small_num = 2.5e-3` prints as `0.0025`.

### 0:18–0:25 — A Subtle Typo
- The final line writes `type{small_num}` instead of `{type(small_num)}`.
- Result: it prints the literal word `type` followed by the value, not the type.

---

## 5. Code Demos

```python
PI = 3.1415926

print("Value of PI:", PI)
print(f"Type of PI: {type(PI)}")

small_num = 2.5e-3
print(f"Value of small_num: {small_num}")
print(f"Type of small_num: type{small_num}")
```

**Actual output:**

```
Value of PI: 3.1415926
Type of PI: <class 'float'>
Value of small_num: 0.0025
Type of small_num: type0.0025
```

> ⚠️ **Look closely at the last line.** It prints `type0.0025`, not the type. The text `type` is outside the braces (so it is printed literally), and `{small_num}` just inserts the value `0.0025`. The intended line was:
>
> ```python
> print(f"Type of small_num: {type(small_num)}")
> ```
>
> which prints `Type of small_num: <class 'float'>`. This is a great reminder that inside an f-string, the function call must be **inside** the `{}`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What value is `2.5e-3`?
- a) `2500`
- b) `0.0025`
- c) `25`
- d) `0.25`

<details>
<summary>Solution</summary>

**Answer:** b) `0.0025` (2.5 × 10⁻³).
</details>

---

### 2. (Level 1, Short Answer)
What does `type(3.14)` return?

<details>
<summary>Solution</summary>

`<class 'float'>`.
</details>

---

### 3. (Level 2, Coding)
Fix the buggy last line so it correctly prints the type of `small_num`.

<details>
<summary>Solution</summary>

```python
small_num = 2.5e-3
print(f"Type of small_num: {type(small_num)}")
```
</details>

---

### 4. (Level 2, Coding)
Write the number 12,000 using scientific notation and print it.

<details>
<summary>Solution</summary>

```python
big = 1.2e4
print(big)  # 12000.0
```
</details>

---

### 5. (Level 3, Coding)
Print both the value and the type of a float on one line, e.g.:
`0.5 is of type <class 'float'>`

<details>
<summary>Solution</summary>

```python
x = 0.5
print(f"{x} is of type {type(x)}")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `type()`](https://docs.python.org/3/library/functions.html#type)
- [Python Official Documentation: Numeric literals](https://docs.python.org/3/reference/lexical_analysis.html#floating-point-literals)
- [Python Tutorial: Floating Point Arithmetic — Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)

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
