# 🗓️ Optional Parameters & Default Arguments

This lesson shows how to give function parameters **default values** so the caller can omit them. We build a `get_formatted_date()` function that formats a date as `dd/mm/yyyy`, and we explore the difference between **positional** and **keyword** arguments.

---

## 1. Learning Objectives

- Define a function with **default parameter values** (`day=1`, `month=1`, `year=2000`).
- Call a function while omitting some, all, or none of its arguments.
- Distinguish between **positional arguments** (matched by order) and **keyword arguments** (matched by name).
- Understand that keyword arguments can be passed in **any order**.
- Format integers with leading zeros using `{day:02d}` and `{year:04d}`.

---

## 2. Prerequisites

- Comfort defining a function with `def`.
- Familiarity with f-strings.
- Awareness of type hints (`day: int`) and return-type hints (`-> str`).

---

## 3. Key Concepts

- **Default value**: `def f(x=1)` means `x` becomes `1` if the caller doesn't supply it.
- **Positional argument**: Matched by position, e.g. `get_formatted_date(14, 5)` → `day=14`, `month=5`.
- **Keyword argument**: Matched by name, e.g. `get_formatted_date(year=2026)`.
- **Order independence (keywords)**: `get_formatted_date(year=2005, day=10, month=12)` works because names, not positions, decide the match.
- **Format spec `:02d`**: Pad an integer to at least 2 digits with leading zeros; `:04d` pads to 4 digits.

---

## 4. Lecture Outline

### 0:00–0:07 — Declaring Defaults
- `def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000) -> str:`

### 0:07–0:15 — Calling With No Arguments
- `get_formatted_date()` uses every default → `01/01/2000`.

### 0:15–0:23 — Positional Calls
- `get_formatted_date(14, 5)` fills `day` and `month` by position.

### 0:23–0:32 — Keyword Calls and Reordering
- `get_formatted_date(year=2005, day=10, month=12)` — order doesn't matter.

---

## 5. Code Demos

```python
def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000) -> str:
    """
    Returns a string representing a date in the format "dd/mm/yyyy"

    Args:
        day (int): The day of the month. Defaults to 1.
        month (int): The month of the year. Defaults to 1.
        year (int): The year. Defaults to 2000.

    Returns:
        str: The formatted date string.
    """
    return f"{day:02d}/{month:02d}/{year:04d}"

def main():
    print(get_formatted_date())                  # 01/01/2000
    print(get_formatted_date(2010))              # 2010/01/2000  (2010 fills `day`!)
    print(get_formatted_date(14, 5))             # 14/05/2000
    print(get_formatted_date(12, 7, 2010))       # 12/07/2010
    print(get_formatted_date(year=2026))         # 01/01/2026
    print(get_formatted_date(day=10, month=12, year=2005))   # 10/12/2005
    print(get_formatted_date(year=2005, day=10, month=12))   # 10/12/2005

if __name__ == "__main__":
    main()
```

**Expected output:**

```
01/01/2000
2010/01/2000
14/05/2000
12/07/2010
01/01/2026
10/12/2005
10/12/2005
```

> ⚠️ **Honest note on the comments.** The original file had the comment `# 10/01/2000` next to `get_formatted_date(2010)`. That comment is misleading: `2010` is passed **positionally**, so it fills the *first* parameter, `day`, giving `2010/01/2000` — not `10/01/2000`. This is exactly the trap default parameters set: a single positional value goes to the first slot, not the one you have in mind. If you want only the year, you must use a keyword: `get_formatted_date(year=2010)`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
With `def f(a=1, b=2)`, what does `f(5)` set?
- a) `a=1, b=5`
- b) `a=5, b=2`
- c) `a=5, b=5`
- d) Error

<details>
<summary>Solution</summary>

**Answer:** b) `a=5, b=2`. The single positional value fills the first parameter; `b` keeps its default.
</details>

---

### 2. (Level 1, Short Answer)
Why does `get_formatted_date(year=2026)` produce `01/01/2026` instead of an error?

<details>
<summary>Solution</summary>

Because `day` and `month` have default values (`1` and `1`). Supplying only the `year` keyword leaves the other two at their defaults.
</details>

---

### 3. (Level 2, Coding)
Write a function `greet(name, greeting="Hello")` that returns `"Hello, Bob!"` when called as `greet("Bob")`.

<details>
<summary>Solution</summary>

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))           # Hello, Bob!
print(greet("Bob", "Hi"))     # Hi, Bob!
```
</details>

---

### 4. (Level 2, Coding)
Using `get_formatted_date`, print Greece's Independence Day (25 March 1821) using keyword arguments in the order `year`, `month`, `day`.

<details>
<summary>Solution</summary>

```python
print(get_formatted_date(year=1821, month=3, day=25))   # 25/03/1821
```
</details>

---

### 5. (Level 3, Coding)
Format the number `7` as a 3-digit string with leading zeros (`007`) using an f-string format spec.

<details>
<summary>Solution</summary>

```python
n = 7
print(f"{n:03d}")   # 007
```
</details>

---

## 7. Further Reading

- [Python Tutorial: Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)
- [Python Tutorial: Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
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
