# 🔡 There Is No `char` Type: Characters Are Just Strings

This short lesson clears up a common point of confusion for people coming from languages like C or Java: Python has **no separate character type**. A single character such as `'A'` is simply a string of length 1, with type `str`.

---

## 1. Learning Objectives

- Store a single character in a variable.
- Use `type()` to confirm that a single character is of type `str`.
- Understand that Python does not have a distinct `char` type.
- Embed both a value and its type inside an f-string.
- Connect this idea to the fact that strings are sequences of characters.

---

## 2. Prerequisites

- Knowing what a string is.
- Familiarity with `type()` and f-strings.
- (Optional) Experience with a language that has a `char` type, for contrast.

---

## 3. Key Concepts

- **No `char` type**: In Python, `'A'` is a `str`, not a special character type.
- **Length-1 string**: A single character is just a string containing one element.
- **`type('A')`**: Returns `<class 'str'>`.
- **f-string with two placeholders**: `f"{character} is type of: {type(character)}"` inserts both the value and its type.

---

## 4. Lecture Outline

### 0:00–0:06 — Storing One Character
- `character = 'A'`.

### 0:06–0:14 — Checking the Type
- `type(character)` returns `<class 'str'>`, not a `char`.

### 0:14–0:20 — Why It Matters
- Strings are sequences of one-character strings, so indexing a string also yields `str`.

---

## 5. Code Demos

```python
character = 'A'

print(f"{character} is type of: {type(character)}")
```

**Expected output:**

```
A is type of: <class 'str'>
```

> 💡 Because a single character is just a `str`, indexing into a longer string (e.g. `"Hello"[0]`) also gives you a one-character `str`, never a separate character type.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is the type of `'Z'` in Python?
- a) `char`
- b) `str`
- c) `int`
- d) `byte`

<details>
<summary>Solution</summary>

**Answer:** b) `str`.
</details>

---

### 2. (Level 1, Short Answer)
What is `len('A')`?

<details>
<summary>Solution</summary>

`1` — it is a string with a single character.
</details>

---

### 3. (Level 2, Coding)
Print the type of the first character of the string `"Python"`.

<details>
<summary>Solution</summary>

```python
word = "Python"
print(type(word[0]))  # <class 'str'>
```
</details>

---

### 4. (Level 2, Short Answer)
How would you get the numeric Unicode code point of `'A'`? (Hint: there is a built-in function.)

<details>
<summary>Solution</summary>

Use `ord('A')`, which returns `65`. The reverse is `chr(65)`, which returns `'A'`.
</details>

---

### 5. (Level 3, Coding)
Print each character of `"Hi!"` along with its type, one per line.

<details>
<summary>Solution</summary>

```python
for ch in "Hi!":
    print(f"{ch} -> {type(ch)}")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `type()`](https://docs.python.org/3/library/functions.html#type)
- [Python Official Documentation: `ord()` and `chr()`](https://docs.python.org/3/library/functions.html#ord)
- [Python Official Documentation: Text Sequence Type — `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

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
