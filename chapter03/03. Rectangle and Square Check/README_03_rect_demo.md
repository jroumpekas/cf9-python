# 📐 Functions, `input()` Pitfalls & `try`/`except`

This lesson defines a small `is_square()` function and wires it up to user input. It's an excellent teaching example because the uploaded version contains the **single most common beginner bug in Python**: forgetting that `input()` always returns a **string**, which makes the surrounding `try`/`except` do nothing.

---

## 1. Learning Objectives

- Write a boolean-returning function (`is_square`).
- Understand that `input()` **always** returns a `str`, never a number.
- Convert input with `int(...)` and wrap *that* conversion in `try`/`except`.
- See why an exception leaves variables **unbound**, causing a later `NameError`.
- Handle invalid input safely by stopping before using the missing values.

---

## 2. Prerequisites

- Comfort defining functions with type hints and return values.
- Familiarity with `if`/`else`.
- Basic awareness of exceptions (`try`/`except`).

---

## 3. Key Concepts

- **`input()` returns `str`**: `input("...")` gives you text. `"10"` is **not** `10`.
- **Where to convert**: `int(input(...))` is what can raise `ValueError`, so the conversion is what belongs inside `try`.
- **A dead `try`/`except`**: If you never call `int()`, no `ValueError` can ever occur, so the `except` is unreachable.
- **Unbound variables after an exception**: If `int(...)` raises and you only `print` in `except`, the variables were never assigned — using them afterwards raises `NameError`.
- **Comparing strings vs ints**: `"10" == "10"` is `True`, but `is_square` was meant to compare *numbers*; comparing the raw strings hides the missing conversion.

---

## 4. Lecture Outline

### 0:00–0:08 — The `is_square` Function
- `return length == width`.

### 0:08–0:18 — The Input Bug
- `input()` returns strings; no `int()` means the `try`/`except` is dead code.

### 0:18–0:28 — The Knock-On `NameError`
- What happens to `length`/`width` if conversion fails.

### 0:28–0:38 — The Corrected Flow
- Convert inside `try`, `return` on failure, then compare.

---

## 5. Code Demos

> ⚠️ **What's wrong with the uploaded version.** It reads `length = input(...)` and `width = input(...)` with **no `int()` conversion**. Because `input()` only ever returns strings, the `except ValueError` can never trigger — it's unreachable. Worse, `is_square` then compares two *strings*. And if you *did* add `int()` and the user typed `"abc"`, the `except` would print a message but execution would fall through to `is_square(length=length, ...)` where `length` was never assigned → **`NameError`**. The trailing `pass` is also a leftover that does nothing.

Here is the corrected, robust version:

```python
def is_square(length: int, width: int) -> bool:
    """Check if a rectangle is a square (equal length and width)."""
    return length == width

def my_add(a, b):
    return a + b

def main():
    try:
        length = int(input("Give me the length of the rectangle: "))
        width = int(input("Give me the width of the rectangle: "))
    except ValueError:
        print("Invalid input. Please enter valid integers for length and width.")
        return                       # stop here — don't use unbound variables

    if is_square(length, width):
        print("The rectangle is square")
    else:
        print("The rectangle is NOT square")

if __name__ == '__main__':
    main()
```

**Example run (valid input):**

```
Give me the length of the rectangle: 10
Give me the width of the rectangle: 10
The rectangle is square
```

**Example run (invalid input):**

```
Give me the length of the rectangle: abc
Invalid input. Please enter valid integers for length and width.
```

> 💡 **The golden rule.** `input()` → always a string. If you need a number, convert it: `int(input(...))` or `float(input(...))`. Put the conversion inside `try`, and on failure either `return`, `continue` (in a loop), or `raise` — never fall through to code that assumes the value exists.

> 🧩 **Bonus — the commented-out `my_add`.** The file hints at a neat idea: `my_add(100, 200)` returns `300`, but `my_add("Hello", "CF9 friends")` returns `"HelloCF9 friends"`. The same `+` operator does arithmetic on numbers and concatenation on strings — a great illustration of operator behaviour depending on operand types.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What type does `input("Age: ")` return when the user types `25`?
- a) `int`
- b) `float`
- c) `str`
- d) `bool`

<details>
<summary>Solution</summary>

**Answer:** c) `str`. It returns the string `"25"`; you must call `int()` to get the number `25`.
</details>

---

### 2. (Level 1, Short Answer)
Why was the original `except ValueError` block unreachable?

<details>
<summary>Solution</summary>

Because no conversion was attempted. `input()` returns a string without raising, so no `ValueError` is ever produced — there's nothing for the `except` to catch.
</details>

---

### 3. (Level 2, Short Answer)
If you add `int()` but only `print` inside `except` (no `return`), what error appears for input `"abc"`?

<details>
<summary>Solution</summary>

A `NameError`. The conversion raised before `length` was assigned, the `except` only printed a message, and then `is_square(length, width)` tried to use the never-assigned `length`.
</details>

---

### 4. (Level 2, Coding)
Rewrite the input handling inside a loop so the program keeps asking until the user enters valid integers.

<details>
<summary>Solution</summary>

```python
while True:
    try:
        length = int(input("Length: "))
        width = int(input("Width: "))
        break                      # valid -> leave the loop
    except ValueError:
        print("Please enter whole numbers.")
```
</details>

---

### 5. (Level 3, Coding)
Extend `is_square` to also reject non-positive dimensions, returning `False` if either side is `<= 0`.

<details>
<summary>Solution</summary>

```python
def is_square(length: int, width: int) -> bool:
    if length <= 0 or width <= 0:
        return False
    return length == width
```
</details>

---

## 7. Further Reading

- [Python Docs: `input`](https://docs.python.org/3/library/functions.html#input)
- [Python Docs: `int`](https://docs.python.org/3/library/functions.html#int)
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
