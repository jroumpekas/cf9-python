# ✖️ Nested Loops: Building a Multiplication Table

This lesson uses a `for` loop inside another `for` loop to print a multiplication table. The outer loop picks a row number, the inner loop runs through the columns, and we control the layout with the `end` argument so each row stays on one line.

---

## 1. Learning Objectives

- Write a nested loop (a loop inside another loop).
- Understand how the inner loop runs fully for each step of the outer loop.
- Use `range(start, stop)` and remember the `stop` value is excluded.
- Control line layout with `end='|'` and a bare `print()` to end the row.
- Read and predict the output of two-dimensional iteration.

---

## 2. Prerequisites

- Comfort with a single `for` loop and `range()`.
- Familiarity with f-strings and the `end` argument.
- Basic multiplication.

---

## 3. Key Concepts

- **Nested loop**: A loop placed inside the body of another loop.
- **Outer vs. inner**: For every single iteration of the outer loop, the inner loop completes all of its iterations.
- **`range(1, 4)`**: Produces `1, 2, 3` (the `4` is excluded).
- **`range(1, 11)`**: Produces `1` through `10`.
- **`end='|'`**: Separates inner-loop outputs with a pipe instead of a newline; `print()` afterward moves to the next row.

---

## 4. Lecture Outline

### 0:00–0:07 — The Outer Loop
- `for i in range(1, 4)` chooses the current multiplier (1, 2, 3).

### 0:07–0:15 — The Inner Loop
- `for j in range(1, 11)` runs 1–10 for each `i`.
- Printing `f"{i} * {j} = {i * j}"`.

### 0:15–0:22 — Controlling the Layout
- `end='|'` keeps a row on one line.
- A bare `print()` ends the row; a final `print()` adds a blank line.

---

## 5. Code Demos

```python
# Multiplication table

for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end='|')
    print()
print()
```

**Expected output:**

```
1 * 1 = 1|1 * 2 = 2|1 * 3 = 3|1 * 4 = 4|1 * 5 = 5|1 * 6 = 6|1 * 7 = 7|1 * 8 = 8|1 * 9 = 9|1 * 10 = 10|
2 * 1 = 2|2 * 2 = 4|2 * 3 = 6|2 * 4 = 8|2 * 5 = 10|2 * 6 = 12|2 * 7 = 14|2 * 8 = 16|2 * 9 = 18|2 * 10 = 20|
3 * 1 = 3|3 * 2 = 6|3 * 3 = 9|3 * 4 = 12|3 * 5 = 15|3 * 6 = 18|3 * 7 = 21|3 * 8 = 24|3 * 9 = 27|3 * 10 = 30|

```

> 💡 The key idea: the inner loop finishes all 10 columns before the outer loop moves to the next row. That is why you get three full rows of ten entries each.

---

## 6. Exercises

### 1. (Level 1, MCQ)
How many times does the inner `print()` run in total in the demo?
- a) 3
- b) 10
- c) 13
- d) 30

<details>
<summary>Solution</summary>

**Answer:** d) 30 — 3 outer iterations × 10 inner iterations.
</details>

---

### 2. (Level 1, Short Answer)
What numbers does `range(1, 4)` produce?

<details>
<summary>Solution</summary>

`1, 2, 3`. The stop value `4` is not included.
</details>

---

### 3. (Level 2, Coding)
Print a multiplication table for `5` (i.e. `5 x 1` through `5 x 10`), one product per line.

<details>
<summary>Solution</summary>

```python
for j in range(1, 11):
    print(f"5 * {j} = {5 * j}")
```
</details>

---

### 4. (Level 2, Coding)
Use a nested loop to print a 3×3 grid of asterisks:

```
* * *
* * *
* * *
```

<details>
<summary>Solution</summary>

```python
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()
```
</details>

---

### 5. (Level 3, Coding)
Print the full multiplication tables from 1 to 9, each table on its own line, neatly separated.

<details>
<summary>Solution</summary>

```python
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:>3}", end=" ")
    print()
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `range()`](https://docs.python.org/3/library/stdtypes.html#range)
- [Python Tutorial: `for` Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Reference: Nested code blocks and indentation](https://docs.python.org/3/reference/compound_stmts.html)

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
