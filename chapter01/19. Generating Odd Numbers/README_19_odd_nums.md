# 🔢 Generating Odd Numbers

This lesson is about generating odd numbers within a range using loops. It demonstrates loop control and the modulo operator, and shows a few idiomatic Python ways to produce a list of odd values.

> ℹ️ **Note:** the source file `19_odd_nums.py` is currently empty. The code below is a suggested implementation you can use to fill it in — adapt it to match what you cover in class.

---

## 1. Learning Objectives

- Loop over a range of numbers with `range()`.
- Identify odd numbers using the modulo operator (`% 2 != 0`).
- Generate odd numbers directly with a stepped `range(start, stop, step)`.
- Collect results into a list with `append()` or a list comprehension.
- Compare an explicit loop with a more concise comprehension.

---

## 2. Prerequisites

- Familiarity with `for` loops and `range()`.
- Understanding of the modulo operator (`%`).
- Knowing how to build a list.

---

## 3. Key Concepts

- **`range(start, stop, step)`**: Produces numbers from `start` up to (not including) `stop`, increasing by `step`.
- **Modulo test**: `n % 2 == 0` is even; `n % 2 != 0` (or `== 1`) is odd.
- **Stepping by 2**: `range(1, n, 2)` yields odd numbers directly without a test.
- **`list.append(x)`**: Adds an item to a list.
- **List comprehension**: `[n for n in range(...) if ...]` builds a list in one line.

---

## 4. Lecture Outline

### 0:00–0:07 — Odd Numbers via a Loop + Modulo
- Loop through a range and keep numbers where `n % 2 != 0`.

### 0:07–0:13 — Odd Numbers via a Stepped Range
- `range(1, n, 2)` skips the even numbers entirely.

### 0:13–0:20 — Building a List
- Collecting results with `append()`.
- The shorter list-comprehension equivalent.

---

## 5. Code Demos

```python
# Approach 1: loop with a modulo test
odd_numbers = []
for n in range(1, 21):
    if n % 2 != 0:
        odd_numbers.append(n)
print("Odd numbers:", odd_numbers)

# Approach 2: stepped range (no test needed)
print("Stepped range:", list(range(1, 21, 2)))

# Approach 3: list comprehension
odds = [n for n in range(1, 21) if n % 2 != 0]
print("Comprehension:", odds)
```

**Expected output:**

```
Odd numbers: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Stepped range: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Comprehension: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

> 💡 The stepped range (`range(1, 21, 2)`) is the cleanest way to generate odd numbers when you don't need to test each value individually.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which expression is `True` only for odd numbers?
- a) `n % 2 == 0`
- b) `n % 2 != 0`
- c) `n / 2 == 0`
- d) `n // 2 == 0`

<details>
<summary>Solution</summary>

**Answer:** b) `n % 2 != 0`.
</details>

---

### 2. (Level 1, Short Answer)
What does `list(range(1, 10, 2))` produce?

<details>
<summary>Solution</summary>

`[1, 3, 5, 7, 9]`.
</details>

---

### 3. (Level 2, Coding)
Print all odd numbers between 1 and 50 on one line, separated by spaces.

<details>
<summary>Solution</summary>

```python
for n in range(1, 51, 2):
    print(n, end=" ")
print()
```
</details>

---

### 4. (Level 2, Coding)
Use a list comprehension to build a list of odd numbers from 1 to 30.

<details>
<summary>Solution</summary>

```python
odds = [n for n in range(1, 31) if n % 2 != 0]
print(odds)
```
</details>

---

### 5. (Level 3, Coding)
Ask the user for a number `n` and print the sum of all odd numbers from 1 to `n`.

<details>
<summary>Solution</summary>

```python
n = int(input("Enter n: "))
total = sum(x for x in range(1, n + 1) if x % 2 != 0)
print("Sum of odds:", total)
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `range()`](https://docs.python.org/3/library/stdtypes.html#range)
- [Python Tutorial: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python Reference: Binary arithmetic operations (`%`)](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)

---

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Dimitris Roumpekas - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a> (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
