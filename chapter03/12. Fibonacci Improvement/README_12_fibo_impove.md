# 🔧 Fibonacci, Improved — and a Classic Indentation Bug

This lesson refactors the iterative Fibonacci into a reusable `fibo(n)` function and introduces Python's elegant **tuple-swap** idiom `a, b = b, a + b`. It's also a perfect case study of two bugs: a `return` that sits **inside** the loop, and a `main()` that does nothing.

---

## 1. Learning Objectives

- Extract Fibonacci logic into a reusable function with a clean base case.
- Use the tuple-swap idiom `a, b = b, a + b` (no temporary variable).
- Handle `n` of 0 and 1 with `if n in [0, 1]: return n`.
- Diagnose why a misplaced `return` makes the function wrong for `n >= 3`.
- Notice that an empty `main()` produces no output at all.

---

## 2. Prerequisites

- Familiarity with the iterative Fibonacci (lesson 11).
- Comfort with functions, `return`, and indentation rules.

---

## 3. Key Concepts

- **Base case**: `if n in [0, 1]: return n` returns 0 for `F(0)` and 1 for `F(1)` directly.
- **Tuple swap**: `a, b = b, a + b` evaluates the whole right side first, then assigns — advancing the pair in one line.
- **Indentation = scope**: A `return` indented *inside* the `for` body runs on the **first** iteration, exiting too early.
- **Empty `main`**: `def main(): pass` runs nothing, so even a correct `fibo` would print no output.

---

## 4. Lecture Outline

### 0:00–0:08 — The Base Case
- `if n in [0, 1]: return n`.

### 0:08–0:18 — The Bug: `return` Inside the Loop
- It returns after one pass — wrong for `n >= 3`.

### 0:18–0:28 — The Fix + Wiring Up `main`
- Dedent the `return`; make `main` actually call and print.

---

## 5. Code Demos

> ⚠️ **Two bugs in the uploaded version.** (1) `return b` is indented **inside** the `for` loop, so the function returns on the very first iteration — `fibo(3)` gives `1` instead of `2`, `fibo(5)` gives `1` instead of `5`. (2) `main()` is just `pass`, so running the file prints nothing.

The uploaded code (annotated):

```python
def fibo(n):
    if n in [0, 1]:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        return b          # BUG: inside the loop -> exits after 1 iteration

def main():
    pass                  # BUG: does nothing, so no output
```

The corrected version:

```python
def fibo(n):
    """Return the nth Fibonacci number (F(0)=0, F(1)=1)."""
    if n in [0, 1]:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b              # FIX: outside the loop -> returns the final value

def main():
    for n in range(10):
        print(f"F({n}) = {fibo(n)}")

if __name__ == "__main__":
    main()
```

**Expected output (corrected):**

```
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
```

> 💡 **Indentation is not cosmetic in Python.** Moving `return b` left by four spaces is the entire fix. Inside the loop it means "return on the first pass"; outside it means "return once the loop has finished". The interpreter decides scope purely from indentation.

> 🐍 **The tuple-swap idiom.** `a, b = b, a + b` first builds the right-hand tuple `(b, a + b)` using the *old* values, then unpacks it into `a` and `b`. That's why no temporary variable is needed — a cleaner replacement for the three-line `temp` dance in lesson 11.

---

## 6. Exercises

### 1. (Level 1, MCQ)
With the `return` inside the loop, what does `fibo(5)` return?
- a) 5
- b) 3
- c) 1
- d) 8

<details>
<summary>Solution</summary>

**Answer:** c) 1. After the first iteration `a, b = 1, 1`, and the misplaced `return` immediately gives back `1`.
</details>

---

### 2. (Level 1, Short Answer)
What single change fixes the `fibo` function?

<details>
<summary>Solution</summary>

Dedent `return b` so it sits **outside** the `for` loop (aligned with the `for`, not with its body). Then it returns only after all iterations complete.
</details>

---

### 3. (Level 2, Short Answer)
Even with `fibo` fixed, why would running the original file still print nothing?

<details>
<summary>Solution</summary>

Because `main()` contains only `pass`. It never calls `fibo` or prints anything. You must add code to `main` (e.g. read input or loop and print results).
</details>

---

### 4. (Level 2, Coding)
Explain, step by step, what `a, b = b, a + b` does when `a = 2, b = 3`.

<details>
<summary>Solution</summary>

Python first evaluates the right side using current values: `(b, a + b)` = `(3, 5)`. Then it assigns: `a = 3`, `b = 5`. Both updates use the *old* `a` and `b`, which is why no temporary is needed.
</details>

---

### 5. (Level 3, Coding)
Add input handling to `main` so it reads `n`, validates it, and prints `fibo(n)`.

<details>
<summary>Solution</summary>

```python
def main():
    try:
        n = int(input("n: "))
    except ValueError:
        print("Please enter an integer.")
        return
    if n < 0:
        print("n must be non-negative.")
        return
    print(f"F({n}) = {fibo(n)}")
```
</details>

---

## 7. Further Reading

- [Python Tutorial: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Docs: Assignment statements (tuple unpacking)](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)
- [Python Tutorial: `return` and loop bodies](https://docs.python.org/3/tutorial/controlflow.html)

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
