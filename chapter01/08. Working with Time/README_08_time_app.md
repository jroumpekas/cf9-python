# ⏱️ Working with Time: Converting Seconds

This lesson builds a small program that converts a total number of seconds into days, hours, minutes, and seconds. It is a great practical use of integer (floor) division `//` and the modulo operator `%`, organized cleanly with named constants and f-strings.

---

## 1. Learning Objectives

- Define and use named constants to make code readable.
- Read an integer from the user with `int(input(...))`.
- Use floor division `//` to get whole units (days, hours, minutes).
- Use the modulo operator `%` to get the remaining seconds at each step.
- Format the final result clearly with f-strings.

---

## 2. Prerequisites

- Familiarity with `input()` and converting input to `int`.
- Understanding of the arithmetic operators `//` and `%`.
- Basic f-string usage: `f"{value}"`.

---

## 3. Key Concepts

- **Named constant**: A variable in `UPPER_CASE` whose value does not change, e.g. `SECONDS_IN_A_DAY = 86400`. It documents intent and avoids "magic numbers".
- **Floor division (`//`)**: Divides and discards the remainder, giving a whole number of units.
- **Modulo (`%`)**: Returns the remainder after division — the leftover seconds to process next.
- **Augmented assignment (`%=`)**: `x %= y` is shorthand for `x = x % y`.
- **f-string**: A string prefixed with `f` where `{...}` is replaced by the value inside.

---

## 4. Lecture Outline

### 0:00–0:06 — Defining Constants
- `SECONDS_IN_A_MINUTE`, `SECONDS_IN_AN_HOUR`, `SECONDS_IN_A_DAY`.

### 0:06–0:12 — Reading the Total
- `total_seconds = int(input(...))`.

### 0:12–0:20 — Extracting Days, Then Hours
- `days = total_seconds // SECONDS_IN_A_DAY`.
- Keep the remainder with `% SECONDS_IN_A_DAY`, then repeat for hours.

### 0:20–0:26 — Minutes and Leftover Seconds
- Using `//` and `%=` to peel off minutes, leaving the final seconds.

### 0:26–0:30 — Formatting the Output
- Printing the breakdown with f-strings.

---

## 5. Code Demos

```python
# Constants
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_DAY = 86400

total_seconds = int(input("Please enter the total number of seconds: "))

days = total_seconds // SECONDS_IN_A_DAY
seconds_remaining = total_seconds % SECONDS_IN_A_DAY

hours = seconds_remaining // SECONDS_IN_AN_HOUR
seconds_remaining %= SECONDS_IN_AN_HOUR

minutes = seconds_remaining // SECONDS_IN_A_MINUTE
seconds_remaining %= SECONDS_IN_A_MINUTE

seconds = seconds_remaining

print(f"{total_seconds} seconds equal to:")
print(f"{days} days, {hours} hours, {minutes} mins and {seconds} seconds")
```

**Example run** (input `90061`):

```
Please enter the total number of seconds: 90061
90061 seconds equal to:
1 days, 1 hours, 1 mins and 1 seconds
```

> 💡 The pattern is always the same: `//` tells you how many whole units fit, and `%` tells you what is left over for the next, smaller unit.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `100 // 7` evaluate to?
- a) `14.28`
- b) `14`
- c) `2`
- d) `15`

<details>
<summary>Solution</summary>

**Answer:** b) `14`. Floor division keeps only the whole part.
</details>

---

### 2. (Level 1, Short Answer)
What is the result of `100 % 7`, and what does it represent here?

<details>
<summary>Solution</summary>

`100 % 7` is `2` — the remainder left after taking out fourteen 7s.
</details>

---

### 3. (Level 2, Coding)
Read a number of minutes from the user and print how many whole hours and leftover minutes that is.

<details>
<summary>Solution</summary>

```python
total_minutes = int(input("Minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{hours} hours and {minutes} minutes")
```
</details>

---

### 4. (Level 2, Coding)
Rewrite the seconds line so it uses `divmod()` for hours and minutes. (Hint: `divmod(a, b)` returns `(a // b, a % b)`.)

<details>
<summary>Solution</summary>

```python
seconds_remaining = 5000
minutes, seconds = divmod(seconds_remaining, 60)
print(minutes, "minutes and", seconds, "seconds")
```
</details>

---

### 5. (Level 3, Coding)
Extend the program to also handle weeks (1 week = 604800 seconds). Print weeks, days, hours, minutes, and seconds.

<details>
<summary>Solution</summary>

```python
SECONDS_IN_A_WEEK = 604800
SECONDS_IN_A_DAY = 86400
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_MINUTE = 60

total = int(input("Seconds: "))

weeks, rem = divmod(total, SECONDS_IN_A_WEEK)
days, rem = divmod(rem, SECONDS_IN_A_DAY)
hours, rem = divmod(rem, SECONDS_IN_AN_HOUR)
minutes, seconds = divmod(rem, SECONDS_IN_A_MINUTE)

print(f"{weeks} weeks, {days} days, {hours} hours, {minutes} mins, {seconds} secs")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Binary arithmetic operations (`//`, `%`)](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)
- [Python Official Documentation: `divmod()`](https://docs.python.org/3/library/functions.html#divmod)
- [Python Tutorial: Formatted String Literals (f-strings)](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

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
