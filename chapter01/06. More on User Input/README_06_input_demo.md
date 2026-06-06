# ✅ Turning Input into a Boolean Decision

This lesson builds a small decision based on user input. We read a `yes`/`no` answer, normalize it with `.lower()`, compare it to `"yes"` to get a boolean, and then branch with an `if`/`else` statement to print a different message in each case.

---

## 1. Learning Objectives

- Read a yes/no answer from the user with `input()`.
- Normalize text with the string method `.lower()` so input is case-insensitive.
- Turn a comparison (`== "yes"`) into a boolean value.
- Use an `if`/`else` statement to choose between two outcomes.
- Understand how chaining `.lower()` and `==` works on one line.

---

## 2. Prerequisites

- Familiarity with `input()` returning a string.
- Knowing what a boolean (`True`/`False`) is.
- Basic indentation rules in Python.

---

## 3. Key Concepts

- **`.lower()`**: A string method that returns a lowercase copy, so `"YES"`, `"Yes"`, and `"yes"` all match.
- **Comparison (`==`)**: Tests equality and produces a boolean (`True` or `False`).
- **Method chaining**: `input(...).lower() == "yes"` runs left to right: read, lowercase, then compare.
- **`if`/`else`**: Runs one block when the condition is `True`, otherwise the other block.
- **Indentation**: The indented lines belong to their `if` or `else` branch.

---

## 4. Lecture Outline

### 0:00–0:07 — Reading the Answer
- `input("Are you a student? (yes/no): ")`.

### 0:07–0:14 — Making It Case-Insensitive
- Adding `.lower()` so capitalization does not matter.

### 0:14–0:20 — From Text to Boolean
- `... == "yes"` evaluates to `True` or `False`, stored in `is_student`.

### 0:20–0:28 — Branching with `if`/`else`
- Printing "You are a student" vs. "You are a teacher".

---

## 5. Code Demos

```python
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

if (is_student):
    print("You are a student")
else:
    print("You are a teacher")
```

**Example runs:**

```
Are you a student? (yes/no): YES
You are a student
```

```
Are you a student? (yes/no): no
You are a teacher
```

> 💡 Anything other than `yes`/`Yes`/`YES` (including an empty answer or `y`) evaluates to `False` here, so the `else` branch runs. Keep that in mind when designing prompts.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `"Yes".lower()` return?
- a) `"Yes"`
- b) `"yes"`
- c) `"YES"`
- d) `True`

<details>
<summary>Solution</summary>

**Answer:** b) `"yes"`.
</details>

---

### 2. (Level 1, Short Answer)
What is the type and value of `"yes" == "yes"`?

<details>
<summary>Solution</summary>

It is a boolean with the value `True`.
</details>

---

### 3. (Level 2, Coding)
Ask the user "Do you like Python? (yes/no)" and print `Great!` if they say yes (any capitalization), otherwise `That's okay.`

<details>
<summary>Solution</summary>

```python
likes = input("Do you like Python? (yes/no): ").lower() == "yes"
if likes:
    print("Great!")
else:
    print("That's okay.")
```
</details>

---

### 4. (Level 2, Coding)
Rewrite the lesson so that both `yes` and `y` count as a student answer.

<details>
<summary>Solution</summary>

```python
answer = input("Are you a student? (yes/no): ").lower()
is_student = answer == "yes" or answer == "y"
print("You are a student" if is_student else "You are a teacher")
```
</details>

---

### 5. (Level 3, Coding)
Ask whether it is currently raining (yes/no). If yes, print `Take an umbrella ☔`, otherwise print `Enjoy the sun ☀`.

<details>
<summary>Solution</summary>

```python
raining = input("Is it raining? (yes/no): ").lower() == "yes"
if raining:
    print("Take an umbrella ☔")
else:
    print("Enjoy the sun ☀")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `str.lower()`](https://docs.python.org/3/library/stdtypes.html#str.lower)
- [Python Tutorial: `if` Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Official Documentation: Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

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
