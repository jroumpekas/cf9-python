# ❗ Factorial of a Number (`n!`)

This lesson computes the **factorial** of a non-negative integer — the product of all positive integers up to `n`. It's a clean, focused example of the multiplicative accumulator pattern plus input validation.

---

## 1. Learning Objectives

- Define factorial: `n! = 1 × 2 × … × n`, with `0! = 1`.
- Implement it iteratively with a product accumulator.
- Validate that the input is a **non-negative** integer.
- Format large results with thousands separators.

---

## 2. Prerequisites

- Comfort with `for` loops, `range`, and functions.
- Familiarity with `try`/`except` and manual `raise`.

---

## 3. Key Concepts

- **Factorial**: `5! = 1×2×3×4×5 = 120`. By definition, `0! = 1`.
- **Accumulator starts at 1**: The product identity, so `0!` (an empty loop) correctly yields `1`.
- **`range(1, n + 1)`**: Iterates `1` through `n` inclusive; for `n = 0` it's empty, leaving `factorial = 1`.
- **Validation**: `if n < 0: raise ValueError` rejects negatives, which have no factorial here.

---

## 4. Lecture Outline

### 0:00–0:10 — The Factorial Loop
- `factorial = 1`, multiply across `range(1, n + 1)`.

### 0:10–0:18 — The `0!` Edge Case
- Empty range leaves `factorial = 1`, which is exactly `0!`.

### 0:18–0:26 — Validation & Output
- Reject negatives; format with `:,`.

---

## 5. Code Demos

```python
def calculate_factorial(n):
    """Return n! (the product of 1..n). 0! is 1."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    try:
        n = int(input("Please insert a non-negative integer: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return

    factorial = calculate_factorial(n)
    print(f"{n}! = {factorial:,}")

if __name__ == "__main__":
    main()
```

**Example runs:**

```
Please insert a non-negative integer: 5
5! = 120

Please insert a non-negative integer: 0
0! = 1

Please insert a non-negative integer: 10
10! = 3,628,800
```

> 💡 **Why `0!` comes out as 1 for free.** When `n = 0`, `range(1, 1)` is empty, so the loop never runs and `factorial` keeps its starting value of `1` — which is the correct mathematical definition of `0!`. The starting value isn't arbitrary; it's the multiplicative identity.

> 🐍 **Python integers never overflow.** `100!` is a 158-digit number, and Python computes it exactly — integers have arbitrary precision. (In many other languages this would overflow a fixed-size integer.)

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is `0!`?
- a) `0`
- b) `1`
- c) Undefined
- d) Error

<details>
<summary>Solution</summary>

**Answer:** b) `1`, by definition.
</details>

---

### 2. (Level 1, Short Answer)
Why does the accumulator start at `1` rather than `0`?

<details>
<summary>Solution</summary>

Because factorial is a product. `1` is the multiplicative identity, so it doesn't distort the result and it correctly yields `1` for the empty case (`0!`). Starting at `0` would make every factorial `0`.
</details>

---

### 3. (Level 2, Coding)
Compare your function against Python's built-in `math.factorial` for `n = 6`.

<details>
<summary>Solution</summary>

```python
import math
print(calculate_factorial(6), math.factorial(6))   # 720 720
```
</details>

---

### 4. (Level 2, Coding)
Write a recursive version of factorial.

<details>
<summary>Solution</summary>

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```
The base case `n <= 1` stops the recursion (covers both `0!` and `1!`).
</details>

---

### 5. (Level 3, Coding)
How many digits does `100!` have? Compute it.

<details>
<summary>Solution</summary>

```python
import math
print(len(str(math.factorial(100))))   # 158
```
Converting the huge integer to a string and measuring its length is a neat way to count digits.
</details>

---

## 7. Further Reading

- [Python Docs: `math.factorial`](https://docs.python.org/3/library/math.html#math.factorial)
- [Python Docs: `range`](https://docs.python.org/3/library/stdtypes.html#range)
- [Python Tutorial: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

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
