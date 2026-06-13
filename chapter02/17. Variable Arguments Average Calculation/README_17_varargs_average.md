# 🔢 Averaging an Arbitrary Number of Values with `*args`

This lesson applies `*args` to a numeric problem: computing the **average** of however many numbers you pass. It also revisits the "no arguments" guard and demonstrates formatting the result to two decimal places.

---

## 1. Learning Objectives

- Accept any number of numeric arguments with `*numbers`.
- Guard against the empty case (`if not numbers:`) to avoid a division-by-zero crash.
- Compute an average with `sum(numbers) / len(numbers)`.
- Format a float to 2 decimal places with `"{:.2f}".format(average)`.
- Unpack a list into `*args` at the call site.

---

## 2. Prerequisites

- Comfort with `*args` (see `15_varargs_demo.py`).
- Familiarity with `sum()` and `len()`.
- Awareness of float formatting.

---

## 3. Key Concepts

- **`*numbers`**: Collects all positional arguments into a tuple of numbers.
- **Empty guard**: With no arguments, `len(numbers)` is `0`; dividing by it would raise `ZeroDivisionError`, so we return a message first.
- **`sum(numbers) / len(numbers)`**: The classic mean formula.
- **`"{:.2f}".format(x)`**: Renders the number with exactly two digits after the decimal point.
- **List unpacking**: To average a list `my_ints`, call `get_average(*my_ints)` — the `*` spreads the list into separate arguments.

---

## 4. Lecture Outline

### 0:00–0:08 — Declaring `*numbers`
- `def get_average(*numbers):`

### 0:08–0:16 — The Empty Guard
- `if not numbers:` returns `"No numbers provided"`.

### 0:16–0:24 — Computing & Formatting
- `average = sum(numbers) / len(numbers)` then `"{:.2f}".format(average)`.

### 0:24–0:32 — Passing a List
- `get_average(*my_ints)` unpacks the list.

---

## 5. Code Demos

```python
def get_average(*numbers):
    if not numbers:
        return "No numbers provided"
    else:
        average = sum(numbers) / len(numbers)
        return "{:.2f}".format(average)

def main():
    print(get_average(10, 20, 15))          # 15.00

    my_ints = [10, 20, 30]
    print(get_average(*my_ints))            # 20.00  (note the * unpacking)

if __name__ == "__main__":
    main()
```

**Expected output:**

```
15.00
20.00
```

> ⚠️ **Honest note on the original `main()`.** The uploaded file created `my_ints = [10, 20, 30]` but then called a bare `print()` (printing an empty line) instead of using the list. If you write `get_average(my_ints)` **without** the `*`, you pass the *whole list as one argument*, and `sum()` will fail with a `TypeError` because it can't add a list. The fix is `get_average(*my_ints)`, which unpacks the list into three separate numbers.

> 💡 **Return type consistency.** This function returns a *string* (`"15.00"`) on success and a *string* (`"No numbers provided"`) on failure — so callers always get a string. An alternative design returns a `float` and lets the caller format it; both are valid, just be consistent and document which one you chose.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `get_average()` return when called with no arguments?
- a) `0`
- b) `None`
- c) `"No numbers provided"`
- d) Raises `ZeroDivisionError`

<details>
<summary>Solution</summary>

**Answer:** c) `"No numbers provided"`. The empty guard runs before any division.
</details>

---

### 2. (Level 1, Short Answer)
Why is the `if not numbers:` check important here?

<details>
<summary>Solution</summary>

Without it, `len(numbers)` would be `0` and `sum(numbers) / len(numbers)` would raise a `ZeroDivisionError`. The guard returns a friendly message instead of crashing.
</details>

---

### 3. (Level 2, Coding)
Call `get_average` to average the numbers in `scores = [88, 92, 79, 95]`.

<details>
<summary>Solution</summary>

```python
scores = [88, 92, 79, 95]
print(get_average(*scores))   # 88.50
```
</details>

---

### 4. (Level 2, Coding)
Write `get_max(*numbers)` that returns the largest value, or `None` if no numbers are given.

<details>
<summary>Solution</summary>

```python
def get_max(*numbers):
    if not numbers:
        return None
    return max(numbers)

print(get_max(3, 9, 5))   # 9
print(get_max())          # None
```
</details>

---

### 5. (Level 3, Coding)
Modify `get_average` to return a `float` (not a string) and round it to 2 decimals using `round()`. Keep the empty guard returning `None`.

<details>
<summary>Solution</summary>

```python
def get_average(*numbers):
    if not numbers:
        return None
    return round(sum(numbers) / len(numbers), 2)

print(get_average(10, 20, 15))   # 15.0
print(get_average())             # None
```
Note: `round(15.0, 2)` is the float `15.0`, displayed without trailing zeros — that's why string formatting is preferred when you need a fixed `15.00` look.
</details>

---

## 7. Further Reading

- [Python Docs: `sum`](https://docs.python.org/3/library/functions.html#sum)
- [Python Docs: `len`](https://docs.python.org/3/library/functions.html#len)
- [Python Tutorial: Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)
- [Python Docs: Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)

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
