# ✂️ String Slicing Techniques

This lesson explores string slicing — extracting parts of a string using the `[start:stop:step]` syntax. We cover single-character indexing, full and partial slices, negative indices, stepping, reversing a string, and empty slices.

---

## 1. Learning Objectives

- Access a single character by index (`s[7]`).
- Extract a substring with `s[start:stop]`.
- Use the full slice `s[:]` and understand what it returns.
- Use negative indices to count from the end (`s[-2]`).
- Use a step to skip characters (`s[::2]`) and reverse a string (`s[::-1]`).
- Recognize that an empty slice like `s[7:7]` returns `""`.

---

## 2. Prerequisites

- Familiarity with strings and indexing.
- Knowing that indices start at `0`.
- Understanding `len()`.

---

## 3. Key Concepts

- **`s[i]`**: A single character at index `i`.
- **`s[start:stop]`**: Characters from `start` up to (but not including) `stop`.
- **`s[:]`**: A full copy of the **entire** string — not a part of it.
- **Negative index**: `s[-1]` is the last character, `s[-2]` the one before it.
- **Step**: `s[::2]` takes every second character; `s[::-1]` reverses the string.
- **Empty slice**: `s[7:7]` (start equals stop) returns an empty string `""`.

---

## 4. Lecture Outline

### 0:00–0:06 — Length and Single Index
- `len(s)` and `s[7]`.

### 0:06–0:13 — Full and Partial Slices
- `s[:]` returns the whole string; `s[7:len(s)]` returns the tail.

### 0:13–0:19 — Negative Indices
- `s[-2]` counts from the end.

### 0:19–0:26 — Stepping, Reversing, and Empty Slices
- `s[::2]`, `s[::-1]`, and `s[7:7]`.

---

## 5. Code Demos

```python
s = "Coding Factory"
print(f"len(s) = {len(s)}")

s1 = s[7]            # 'F'
print(s1)

s2 = s[:]            # the WHOLE string, not just "Coding"
print(s2)

s3 = s[7:len(s)]     # 'Factory'
print(s3)

s4 = s[-2]           # 'r'
print(s4)

s5 = s[0::2]         # every 2nd character
print(s5)

s6 = s[::-1]         # reversed
print(s6)

s7 = s[7:7]          # empty string
print(s7)
```

**Expected output:**

```
len(s) = 14
F
Coding Factory
Factory
r
Cdn atr
yrotcaF gnidoC

```

> ⚠️ **Watch the comment on `s[:]`.** In the original file it says `# Coding`, but that is misleading: `s[:]` returns the **entire** string `"Coding Factory"`, not just `"Coding"`. To get only `"Coding"` you would write `s[:6]`.
>
> 💡 A couple of the trickier results:
> - `s[0::2]` → `Cdn atr` (indices 0, 2, 4, 6, 8, 10, 12 — note index 6 is the space).
> - `s[::-1]` → `yrotcaF gnidoC` (the whole string reversed).
> - `s[7:7]` → `""` (an empty line), because start and stop are equal.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `"Python"[::-1]` return?
- a) `"Python"`
- b) `"nohtyP"`
- c) `"P"`
- d) `""`

<details>
<summary>Solution</summary>

**Answer:** b) `"nohtyP"` — the string reversed.
</details>

---

### 2. (Level 1, Short Answer)
What does `s[:]` return for `s = "Coding Factory"`?

<details>
<summary>Solution</summary>

The entire string, `"Coding Factory"` — a full copy, not a part of it.
</details>

---

### 3. (Level 2, Coding)
From `s = "Coding Factory"`, extract and print just the word `Coding`.

<details>
<summary>Solution</summary>

```python
s = "Coding Factory"
print(s[:6])  # 'Coding'
```
</details>

---

### 4. (Level 2, Coding)
Print the last three characters of `s = "Coding Factory"` using a negative slice.

<details>
<summary>Solution</summary>

```python
s = "Coding Factory"
print(s[-3:])  # 'ory'
```
</details>

---

### 5. (Level 3, Coding)
Write a function `is_palindrome(word)` that returns `True` if a word reads the same forwards and backwards, using slicing.

<details>
<summary>Solution</summary>

```python
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("level"))  # True
print(is_palindrome("python")) # False
```
</details>

---

## 7. Further Reading

- [Python Tutorial: Strings (slicing)](https://docs.python.org/3/tutorial/introduction.html#text)
- [Python Official Documentation: Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Reference: Slicings](https://docs.python.org/3/reference/expressions.html#slicings)

---

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Dimitris Roumpekas - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a> (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
