# ❓ The Ternary (Conditional) Operator

This lesson introduces Python's **ternary operator** — a one-line `if`/`else` expression — in both its simple and chained forms. It also revisits the `try`/`except` input pattern and highlights a subtle pitfall: using variables that may never have been assigned if conversion fails.

---

## 1. Learning Objectives

- Write a value-producing conditional with `X if condition else Y`.
- Chain ternaries to cover three or more cases.
- Compare the ternary form against a traditional `if`/`elif`/`else`.
- Recognise the bug where an exception leaves `a`/`b` unbound before they're used.

---

## 2. Prerequisites

- Comfort with `if`/`elif`/`else`.
- Familiarity with `int(input(...))` and `try`/`except`.

---

## 3. Key Concepts

- **Ternary syntax**: `value_if_true if condition else value_if_false`. It is an *expression* (it produces a value), unlike a statement.
- **Simple use**: `result = "positive" if a > 0 else "non-positive"`.
- **Chained ternary**: `A if c1 else B if c2 else C` — evaluated left to right; the first true condition wins.
- **Readability**: Chained ternaries beyond two levels get hard to read; a normal `if`/`elif`/`else` is often clearer.
- **Unbound-variable pitfall**: If `int(input(...))` raises and `except` only prints, then `a`/`b` were never assigned and the later `compare_integers(a, b)` raises `NameError`.

---

## 4. Lecture Outline

### 0:00–0:08 — Classic `if`/`elif`/`else`
- `compare_integers` prints one of three messages.

### 0:08–0:16 — The Input Block & Its Pitfall
- `int(input(...))` inside `try`; what happens on bad input.

### 0:16–0:24 — Simple Ternary
- `"positive" if a > 0 else "non-positive"`.

### 0:24–0:34 — Chained Ternary
- Three-way decision in a single expression.

---

## 5. Code Demos

> ⚠️ **Pitfall to fix first.** In the uploaded file, if the user types something non-numeric, `except ValueError` prints a message but execution **continues** to `compare_integers(a, b)` — where `a` and `b` were never assigned → `NameError`. The robust fix is to `return` (or loop) inside `except`. (There's also a small typo, `"inpit"`, corrected below.)

```python
def compare_integers(a, b):
    if a == b:
        print("The numbers are equal")
    elif a > b:
        print("The first number is greater than the second number.")
    else:  # a < b
        print("The first number is less than the second number.")

def main():
    try:
        a = int(input("Please enter the first number to compare:  "))
        b = int(input("Please enter the second number to compare: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return                       # stop before using unbound a/b

    compare_integers(a, b)

    # 1. Ternary operator (simple example)
    result = "positive" if a > 0 else "non-positive"
    print(result)

    # 2. Ternary operator (extended / chained example)
    result = (
        "The numbers are equal." if a == b else
        "The first number is greater than the second number." if a > b else
        "The first number is less than the second number."
    )
    print(result)

if __name__ == "__main__":
    main()
```

**Example run:**

```
Please enter the first number to compare:  7
Please enter the second number to compare: 3
The first number is greater than the second number.
positive
The first number is greater than the second number.
```

> 💡 **Read a ternary out loud.** `"positive" if a > 0 else "non-positive"` reads as "use `'positive'` if `a > 0`, otherwise `'non-positive'`". The condition sits in the middle — different from C-style `?:` where it comes first.

> 🧭 **When to chain vs when to stop.** A two-branch ternary is clean. The three-branch chained version above works, but once you have three or more outcomes, a regular `if`/`elif`/`else` (like `compare_integers`) is usually more readable and easier to debug.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `"yes" if 3 > 5 else "no"` evaluate to?
- a) `"yes"`
- b) `"no"`
- c) `True`
- d) Error

<details>
<summary>Solution</summary>

**Answer:** b) `"no"`. The condition `3 > 5` is `False`, so the `else` value is chosen.
</details>

---

### 2. (Level 1, Short Answer)
Rewrite this as a ternary: `if n % 2 == 0: label = "even"` / `else: label = "odd"`.

<details>
<summary>Solution</summary>

```python
label = "even" if n % 2 == 0 else "odd"
```
</details>

---

### 3. (Level 2, Short Answer)
Why does the original program risk a `NameError` after invalid input?

<details>
<summary>Solution</summary>

If `int(input(...))` raises `ValueError`, `a` (and/or `b`) is never assigned. The `except` only prints, so execution continues to `compare_integers(a, b)`, which uses the unbound name → `NameError`. Adding `return` in `except` prevents this.
</details>

---

### 4. (Level 2, Coding)
Use a ternary to set `sign` to `-1`, `0`, or `1` for a number `n` (chained ternary).

<details>
<summary>Solution</summary>

```python
sign = -1 if n < 0 else (0 if n == 0 else 1)
print(sign)
```
</details>

---

### 5. (Level 3, Coding)
Convert the chained ternary in the demo back into an equivalent `if`/`elif`/`else` and decide which you find clearer.

<details>
<summary>Solution</summary>

```python
if a == b:
    result = "The numbers are equal."
elif a > b:
    result = "The first number is greater than the second number."
else:
    result = "The first number is less than the second number."
```
For three branches, most developers find the `if`/`elif`/`else` form easier to scan than the nested ternary — the ternary shines mainly for two-way choices.
</details>

---

## 7. Further Reading

- [Python Docs: Conditional Expressions (ternary)](https://docs.python.org/3/reference/expressions.html#conditional-expressions)
- [Python Tutorial: `if` Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
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
