# ⌨️ Handling User Input with `input()`

This lesson covers reading text from the user with the `input()` function. A crucial idea here is that `input()` **always returns a string**, even when the user types a number. We see how to convert that string to an `int` when we need to do arithmetic — and what happens when we forget.

---

## 1. Learning Objectives

- Read text from the user with `input()` and use it in `print()`.
- Understand that `input()` always returns a value of type `str`.
- Convert a numeric string to a number using `int()` (and `float()`).
- Diagnose the common `TypeError` that occurs when you do math on a string.
- Combine prompts and computed results in clear output.

---

## 2. Prerequisites

- Knowing how to print values and basic arithmetic operators.
- Understanding the difference between `str` and numeric types.
- Ability to run a script that pauses to wait for keyboard input.

---

## 3. Key Concepts

- **`input(prompt)`**: Shows the prompt, waits for the user, and returns what they typed as a **string**.
- **Type of input**: Even `"2000"` typed by the user is a `str`, not an `int`.
- **`int(x)`**: Converts a numeric string (or float) to an integer.
- **`float(x)`**: Converts a numeric string to a floating-point number.
- **`TypeError`**: Raised when an operation is applied to an incompatible type, e.g. dividing a string by a number.

---

## 4. Lecture Outline

### 0:00–0:06 — Reading a Name
- `name = input("Please enter your name: ")` and greeting the user.

### 0:06–0:14 — Reading a Number and Converting It
- `year_of_birth` comes in as a string.
- Wrapping it in `int()` so the subtraction `2026 - int(year_of_birth)` works.

### 0:14–0:22 — A Common Mistake: Forgetting to Convert
- `height = input(...)` is a string.
- `height / 100` raises a `TypeError` because you cannot divide a string by a number.
- The fix: convert with `float(height)` first.

### 0:22–0:28 — Putting It Together
- Why converting input early avoids confusing errors later.

---

## 5. Code Demos

```python
name = input("Please enter your name: ")

print("Hello", name)

year_of_birth = input("Please enter the year of your birth: ")
# year_of_birth_int = int(year_of_birth)

print("You are", 2026 - int(year_of_birth), "years old.")

height = input("Please enter your height in cm: ")
print("You are", height / 100, "meters tall.")
```

> ⚠️ **Heads-up — the last line crashes as written.** Because `input()` returns a string, `height` is text like `"180"`, and `height / 100` raises:
>
> ```
> TypeError: unsupported operand type(s) for /: 'str' and 'int'
> ```
>
> This is the single most common beginner mistake with `input()`. The earlier `year_of_birth` line avoids it by using `int(year_of_birth)`.

**Corrected version of the last two lines:**

```python
height = float(input("Please enter your height in cm: "))
print("You are", height / 100, "meters tall.")
```

With input `180`, this prints `You are 1.8 meters tall.`

---

## 6. Exercises

### 1. (Level 1, MCQ)
What type does `input()` always return?
- a) `int`
- b) `float`
- c) `str`
- d) It depends on what the user types

<details>
<summary>Solution</summary>

**Answer:** c) `str`. You must convert it yourself if you need a number.
</details>

---

### 2. (Level 1, Short Answer)
Why does `2026 - int(year_of_birth)` work but `2026 - year_of_birth` would not?

<details>
<summary>Solution</summary>

`year_of_birth` is a string. Subtraction between an integer and a string is not allowed, so it must first be converted with `int()`.
</details>

---

### 3. (Level 2, Coding)
Ask the user for two numbers and print their sum. (Remember to convert!)

<details>
<summary>Solution</summary>

```python
a = int(input("First number: "))
b = int(input("Second number: "))
print("Sum:", a + b)
```
</details>

---

### 4. (Level 2, Coding)
Fix the height bug from the demo so the program correctly prints the height in meters.

<details>
<summary>Solution</summary>

```python
height = float(input("Please enter your height in cm: "))
print("You are", height / 100, "meters tall.")
```
</details>

---

### 5. (Level 3, Coding)
Ask for a name and a birth year, then print a sentence such as:
`Hello Maria, in 2030 you will be 35 years old.`
(Use a fixed future year of 2030.)

<details>
<summary>Solution</summary>

```python
name = input("Name: ")
birth = int(input("Birth year: "))
print(f"Hello {name}, in 2030 you will be {2030 - birth} years old.")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `input()`](https://docs.python.org/3/library/functions.html#input)
- [Python Official Documentation: `int()`](https://docs.python.org/3/library/functions.html#int)
- [Python Tutorial: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

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
