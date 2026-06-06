# 🧩 Applying Short-Circuit Logic to Build Messages

This lesson puts short-circuit evaluation to practical use. We read a username and an email, fall back to a default user with `or`, and then combine `and` + `or` in a single expression to print either a confirmation of the email or a request to provide one.

---

## 1. Learning Objectives

- Read two inputs and use `or` to supply a default value.
- Combine `and` and `or` to choose between two messages in one expression.
- Understand how `(email and message) or fallback` works step by step.
- Build a final output by concatenating a greeting with the chosen message.
- Recognize and explain a redundant line of code.

---

## 2. Prerequisites

- Understanding of short-circuit evaluation with `or` and `and` (previous lesson).
- Familiarity with `input()` and f-strings.
- Knowing that empty strings are falsy.

---

## 3. Key Concepts

- **`username or "User"`**: Returns `username` if non-empty, otherwise the default `"User"`.
- **`email and f"your email is {email}"`**: If `email` is truthy, this yields the formatted message; if empty, it yields `""` (falsy).
- **`(A and B) or C`**: A common idiom meaning "use B if A is truthy, otherwise use C".
- **String concatenation (`+`)**: Joins the greeting with the chosen message.
- **Redundancy**: Repeating the same assignment has no effect — useful to spot when reviewing code.

---

## 4. Lecture Outline

### 0:00–0:07 — Reading Username and Email
- Two `input()` calls.

### 0:07–0:13 — Default Value with `or`
- `valid_user = username or "User"`.
- Noting the duplicated (redundant) line.

### 0:13–0:22 — The `and`/`or` Message Selector
- `email and f"your email is {email}"` produces a message only when email exists.
- The trailing `or "please provide..."` supplies the fallback.

### 0:22–0:28 — Assembling the Final Output
- Concatenating `f"Hello {valid_user}, "` with the selected message.

---

## 5. Code Demos

```python
# Prompt the user to enter a username and store it in a variable
username = input(f"Enter your username: ")

# Prompt the user to enter an email address and store it in a variable
email = input("Enter your email: ")

# Using the 'or' logical operator to assign a fallback value
# If 'username' is truthy (non-empty), use it; otherwise, use the fallback value "User"
valid_user = username or "User"

# Repeat the operation to reinforce the example (this line could be omitted as it's redundant)
valid_user = username or "User"

# Use a combination of 'and' and 'or' to construct an output message
# 'email and f"your email is {email}"' evaluates to the email message if 'email' is non-empty
# If 'email' is empty, the expression after 'or' is used, asking for a valid email address
print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or ("please provide a valid email address.")))
```

**Example runs:**

```
Enter your username: bob
Enter your email: bob@example.com
Hello bob, your email is bob@example.com
```

```
Enter your username:           (left blank)
Enter your email:              (left blank)
Hello User, please provide a valid email address.
```

> 💡 The two assignments to `valid_user` are identical — the second one does nothing new. Spotting redundancy like this is part of reading code critically.

---

## 6. Exercises

### 1. (Level 1, MCQ)
If `email = ""`, what does `email and "has email"` return?
- a) `"has email"`
- b) `""`
- c) `True`
- d) `None`

<details>
<summary>Solution</summary>

**Answer:** b) `""`. With `and`, a falsy left operand is returned immediately.
</details>

---

### 2. (Level 1, Short Answer)
In `(A and B) or C`, when is `C` used?

<details>
<summary>Solution</summary>

When the whole `A and B` part is falsy — i.e. when `A` is falsy, or when `A` is truthy but `B` is falsy.
</details>

---

### 3. (Level 2, Coding)
Read a name; greet the user by name, or by `"stranger"` if they leave it blank.

<details>
<summary>Solution</summary>

```python
name = input("Name: ")
print(f"Hello {name or 'stranger'}")
```
</details>

---

### 4. (Level 2, Coding)
Read an email and print `Email set: <email>` if provided, otherwise `No email on file.` using the `(A and B) or C` idiom.

<details>
<summary>Solution</summary>

```python
email = input("Email: ")
print((email and f"Email set: {email}") or "No email on file.")
```
</details>

---

### 5. (Level 3, Short Answer)
Rewrite the demo's final `print` using a normal `if`/`else` instead of the `and`/`or` trick, and say which version you find clearer.

<details>
<summary>Solution</summary>

```python
if email:
    message = f"your email is {email}"
else:
    message = "please provide a valid email address."
print(f"Hello {valid_user}, " + message)
```

Most beginners find the `if`/`else` version clearer; the `and`/`or` trick is compact but harder to read.
</details>

---

## 7. Further Reading

- [Python Official Documentation: Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python Official Documentation: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Python Tutorial: Conditional Expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

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
