# 🌀 Fibonacci Numbers (Iterative)

This lesson computes the nth **Fibonacci number** iteratively, using a temporary variable to advance the two running values. The Fibonacci sequence is `0, 1, 1, 2, 3, 5, 8, …`, where each number is the sum of the two before it.

---

## 1. Learning Objectives

- Understand the Fibonacci recurrence: `F(n) = F(n-1) + F(n-2)`.
- Compute it iteratively with two state variables `a` and `b`.
- Use a temporary variable to update both values without losing data.
- Spot the edge case (`n = 0`) and the missing input validation in the uploaded version.

---

## 2. Prerequisites

- Comfort with `for` loops and `range`.
- Familiarity with variable assignment and `int(input(...))`.

---

## 3. Key Concepts

- **The recurrence**: Each term is the sum of the previous two, seeded by `F(0) = 0`, `F(1) = 1`.
- **Two-variable state**: `a` and `b` hold consecutive Fibonacci numbers as the loop advances.
- **The `temp` swap**: `temp = a; a = b; b = temp + b` advances the pair. (Python lets you do this more elegantly — see lesson 12.)
- **Loop range**: `range(2, n + 1)` runs `n - 1` times for `n >= 2`; for `n` of 0 or 1 it's empty.

---

## 4. Lecture Outline

### 0:00–0:10 — Seeding `a` and `b`
- `a = 0`, `b = 1`.

### 0:10–0:20 — Advancing the Pair
- The `temp` dance inside `range(2, n + 1)`.

### 0:20–0:30 — Printing `b` and Its Edge Case
- `b` holds `F(n)`… except for `n = 0`.

---

## 5. Code Demos

```python
def main():
    n = int(input("Please insert an int: "))

    a = 0
    b = 1

    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp + b

    print(f"The {n}th Fibonacci number is {b}")

if __name__ == "__main__":
    main()
```

**Example runs:**

```
Please insert an int: 7
The 7th Fibonacci number is 13

Please insert an int: 1
The 1th Fibonacci number is 1
```

> ⚠️ **Edge case: `n = 0` gives the wrong answer.** With `n = 0`, the loop `range(2, 1)` is empty, so `b` keeps its starting value `1` and the program prints `1`. But `F(0)` is defined as `0`. For `n = 1` it happens to be correct (`F(1) = 1`). A robust version handles `n <= 0` explicitly:
> ```python
> if n <= 0:
>     print(0)
> else:
>     # ... the loop, then print(b)
> ```

> ⚠️ **No input validation.** If the user types something non-numeric, `int(input(...))` raises `ValueError` and the program crashes. Wrapping it in `try`/`except` (as in lessons 08–10) makes it safe.

> 💡 **Sequence check.** For `n = 7`: the sequence is `0, 1, 1, 2, 3, 5, 8, 13` (indices 0–7), so `F(7) = 13` — matching the output.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is `F(6)` in the sequence `0, 1, 1, 2, 3, 5, 8, …`?
- a) 5
- b) 8
- c) 13
- d) 6

<details>
<summary>Solution</summary>

**Answer:** b) 8. (Index 6, counting from `F(0) = 0`.)
</details>

---

### 2. (Level 1, Short Answer)
Why does the uploaded program print `1` instead of `0` when `n = 0`?

<details>
<summary>Solution</summary>

Because `range(2, 0 + 1)` is empty, the loop never runs, and `b` keeps its initial value of `1`. The code doesn't special-case `n = 0`, where the answer should be `0`.
</details>

---

### 3. (Level 2, Coding)
Add the `n <= 0` guard and `try`/`except` validation so the program is correct and crash-proof.

<details>
<summary>Solution</summary>

```python
def main():
    try:
        n = int(input("Please insert an int: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    if n <= 0:
        print("The 0th Fibonacci number is 0")
        return
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f"The {n}th Fibonacci number is {b}")
```
</details>

---

### 4. (Level 2, Coding)
Replace the three-line `temp` swap with Python's tuple-swap idiom.

<details>
<summary>Solution</summary>

```python
a, b = b, a + b
```
This single line does the same advance — the right-hand side is fully evaluated before assignment, so no temporary is needed.
</details>

---

### 5. (Level 3, Coding)
Print the whole sequence up to `F(n)` instead of just the last value.

<details>
<summary>Solution</summary>

```python
a, b = 0, 1
seq = [a]
for _ in range(n):
    seq.append(b)
    a, b = b, a + b
print(seq[:n + 1])
```
</details>

---

## 7. Further Reading

- [Python Tutorial: First Steps Towards Programming (Fibonacci)](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)
- [Python Docs: `range`](https://docs.python.org/3/library/stdtypes.html#range)
- [Python Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

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
