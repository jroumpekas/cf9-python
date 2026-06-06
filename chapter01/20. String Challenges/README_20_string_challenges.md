# 🧩 String Challenges: Building Patterns with Loops

This lesson uses loops, string repetition, and the `end` argument to draw text patterns from the word "Factory". It also contains a recurring bug worth studying: multiplying a string by a **list** instead of an integer, which raises a `TypeError`.

---

## 1. Learning Objectives

- Loop over a string's indices with `range(len(message))`.
- Repeat a character with `*` to build incremental patterns.
- Combine repetition with `end` to add trailing characters on the same line.
- Diagnose the `TypeError` caused by `str * [list]` instead of `str * int`.
- Read and reproduce a target pattern from its description.

---

## 2. Prerequisites

- Familiarity with strings, indexing, and `len()`.
- Understanding of string repetition (`"a" * 3`).
- Knowing the `end` argument of `print()`.

---

## 3. Key Concepts

- **`range(len(message))`**: Produces valid indices `0 .. len-1` for the string.
- **`message[i]`**: The character at position `i`.
- **String repetition needs an int**: `"a" * 3` works; `"a" * [3]` does **not** — you cannot multiply a string by a list.
- **`(i + 1)` vs `[i + 1]`**: Parentheses group an expression; square brackets create a **list**. Only the integer works with `*`.
- **`end="*" * k`**: Sets the line ending to `k` asterisks instead of a newline.

---

## 4. Lecture Outline

### 0:00–0:08 — Challenge 1: Incremental Repetition
- Print each character repeated `i + 1` times to form a growing staircase.

### 0:08–0:16 — The Bug: `* [i + 1]`
- The code multiplies by `[i + 1]` (a list), which raises `TypeError`.
- The fix is `(i + 1)` (an integer).

### 0:16–0:24 — Challenge 2: Right-Aligned Triangle
- Add a decreasing number of trailing `*` using `end`.

---

## 5. Code Demos

```python
# Challenge 1
# Print each character of "Factory" repeated incrementally on each line:
# F
# aa
# ccc
# tttt
# ooooo
# rrrrrr
# yyyyyyy
print("Challenge 1")
message = "Factory"

for i in range(len(message)):
    print(message[i] * [i + 1])   # bug: [i + 1] is a list, not an int

print()


# Challenge 2
# Same staircase, plus a decreasing number of asterisks (right-aligned triangle):
# F******
# aa*****
# ccc****
# tttt***
# ooooo**
# rrrrrr*
# yyyyyyy
for i in range(len(message)):
    print(message[i] * [i + 1], end="*" * (len(message) - i - 1))
    print()
```

> ⚠️ **As written, both loops crash.** `message[i] * [i + 1]` tries to multiply a string by a **list**, which raises:
>
> ```
> TypeError: can't multiply sequence by non-int of type 'list'
> ```
>
> The intended code uses parentheses, not square brackets: `message[i] * (i + 1)`.

**Corrected version:**

```python
message = "Factory"

# Challenge 1
print("Challenge 1")
for i in range(len(message)):
    print(message[i] * (i + 1))
print()

# Challenge 2
for i in range(len(message)):
    print(message[i] * (i + 1), end="*" * (len(message) - i - 1))
    print()
```

**Output of the corrected version:**

```
Challenge 1
F
aa
ccc
tttt
ooooo
rrrrrr
yyyyyyy

F******
aa*****
ccc****
tttt***
ooooo**
rrrrrr*
yyyyyyy
```

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `"x" * [3]` do in Python?
- a) Returns `"xxx"`
- b) Returns `["x", "x", "x"]`
- c) Raises a `TypeError`
- d) Returns `"x3"`

<details>
<summary>Solution</summary>

**Answer:** c) Raises a `TypeError`. You can only multiply a string by an integer.
</details>

---

### 2. (Level 1, Short Answer)
What is the difference between `(i + 1)` and `[i + 1]`?

<details>
<summary>Solution</summary>

`(i + 1)` is just the integer result of the addition; `[i + 1]` is a list containing that single integer.
</details>

---

### 3. (Level 2, Coding)
Print the word "CODE" as a staircase, each letter repeated by its position (C×1, O×2, D×3, E×4).

<details>
<summary>Solution</summary>

```python
word = "CODE"
for i in range(len(word)):
    print(word[i] * (i + 1))
```
</details>

---

### 4. (Level 2, Coding)
Print a left-aligned triangle of `#` characters with heights 1 to 5.

<details>
<summary>Solution</summary>

```python
for i in range(1, 6):
    print("#" * i)
```
</details>

---

### 5. (Level 3, Coding)
Print a centered pyramid of `*` with 5 rows, like:

```
    *
   ***
  *****
 *******
*********
```

<details>
<summary>Solution</summary>

```python
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Common Sequence Operations (repetition)](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Official Documentation: `print()` and the `end` argument](https://docs.python.org/3/library/functions.html#print)
- [Python Tutorial: `range()` and loops](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

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
