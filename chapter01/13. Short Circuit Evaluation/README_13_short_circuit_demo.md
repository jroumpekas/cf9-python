# ⚡ Short-Circuit Evaluation with `or` and `and`

This lesson explores a powerful Python feature: `or` and `and` do not just return `True`/`False` — they return one of their actual operands, and they stop evaluating as soon as the result is known. This "short-circuiting" is commonly used to supply default values and to guard conditions.

---

## 1. Learning Objectives

- Understand that `or` returns the first truthy operand (or the last one).
- Understand that `and` returns the first falsy operand (or the last one).
- Use `or` to provide a default value when a variable is empty or `None`.
- Use `and` to build a guarded condition.
- Combine short-circuit results with an `if`/`else` statement.

---

## 2. Prerequisites

- Familiarity with booleans and the `or`/`and` operators.
- Knowing what `None` is and the idea of "truthy" and "falsy" values.
- Comfort with f-strings and `if`/`else`.

---

## 3. Key Concepts

- **Truthy / falsy**: Non-empty strings and non-zero numbers are truthy; `None`, `""`, `0`, and empty containers are falsy.
- **`or` short-circuit**: `x or y` returns `x` if `x` is truthy, otherwise `y`. Evaluation stops at the first truthy value.
- **`and` short-circuit**: `x and y` returns `x` if `x` is falsy, otherwise `y`. Evaluation stops at the first falsy value.
- **Default-value idiom**: `value = something or "default"` fills in a fallback when `something` is empty/`None`.
- **Returned operand, not just a bool**: The operators yield an actual operand, which may or may not be a boolean.

---

## 4. Lecture Outline

### 0:00–0:07 — `or` with a Falsy Left Side
- `None or "User"` returns `"User"`.

### 0:07–0:13 — `or` with a Truthy Left Side
- `name or "User"` returns `"Bob"`, because `name` is already truthy.

### 0:13–0:20 — `and` for a Guarded Check
- `email and email != ""` returns the result of the second part when `email` is truthy.

### 0:20–0:28 — Using the Result in `if`/`else`
- Branching on `valid_email` to print the right message.

---

## 5. Code Demos

```python
name = "Bob"

print("======== or =======")
valid_user = None or "User"
print(f"Hello {valid_user}")

name = "Bob"

print("========= or =========")
valid_user = name or "User"
print(f"Hello {valid_user}")

print("========= and =========")
email = "bob@example.com"

valid_email = email and email != ""  # email and True
print(f"Valid email: {valid_email}")

if valid_email:
    print(f"Hello {valid_user}, your email is {email}")
else:
    print(f"Hello {valid_user}, please enter your email.")
```

**Expected output:**

```
======== or =======
Hello User
========= or =========
Hello Bob
========= and =========
Valid email: True
Hello Bob, your email is bob@example.com
```

> 💡 In `None or "User"`, the left side is falsy, so `or` moves on and returns `"User"`. In `name or "User"`, `name` ("Bob") is truthy, so `or` returns it immediately and never even looks at `"User"`. That is the short circuit in action.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `"" or "fallback"` return?
- a) `""`
- b) `"fallback"`
- c) `True`
- d) `False`

<details>
<summary>Solution</summary>

**Answer:** b) `"fallback"`. The empty string is falsy, so `or` returns the second operand.
</details>

---

### 2. (Level 1, Short Answer)
What does `"hi" and "there"` return, and why?

<details>
<summary>Solution</summary>

`"there"`. With `and`, if the first operand is truthy, the result is the second operand.
</details>

---

### 3. (Level 2, Coding)
Given `username = ""`, use the `or` idiom to print `Hello Guest`.

<details>
<summary>Solution</summary>

```python
username = ""
display = username or "Guest"
print(f"Hello {display}")
```
</details>

---

### 4. (Level 2, Short Answer)
What does `0 and 100` return? What about `5 and 100`?

<details>
<summary>Solution</summary>

`0 and 100` returns `0` (first falsy operand). `5 and 100` returns `100` (first operand is truthy, so the second is returned).
</details>

---

### 5. (Level 3, Coding)
Ask the user for a nickname. If they leave it blank, greet them as `friend`; otherwise greet them by their nickname.

<details>
<summary>Solution</summary>

```python
nickname = input("Nickname: ") or "friend"
print(f"Welcome, {nickname}!")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Boolean Operations (short-circuit behaviour)](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python Official Documentation: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Python Tutorial: More on Conditions](https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions)

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
