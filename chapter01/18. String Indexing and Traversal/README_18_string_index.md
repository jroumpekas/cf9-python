# 🔎 String Indexing and Traversal

This lesson shows how to access individual characters of a string by index, measure a string's length with `len()`, and walk through every character with a `for` loop. It also includes a separate `for` loop over a numeric range to compare the two kinds of iteration.

---

## 1. Learning Objectives

- Access characters by position using square-bracket indexing (`message[0]`).
- Understand that indexing starts at `0`.
- Measure the length of a string with `len()`.
- Iterate over a string character by character with a `for` loop.
- Iterate over a numeric range with `range()` and control output with `end`.

---

## 2. Prerequisites

- Knowing that strings are sequences of characters.
- Familiarity with `print()`, f-strings, and the `end` argument.
- Basic understanding of `for` loops.

---

## 3. Key Concepts

- **Indexing**: `message[i]` returns the character at position `i`, counting from `0`.
- **Zero-based**: The first character is at index `0`, the second at `1`, and so on.
- **`len(s)`**: Returns the number of characters in `s`, including spaces.
- **Iterating a string**: `for char in message` visits each character in order.
- **`range(1, 11)`**: Produces the numbers `1` through `10` (the end value is excluded).
- **`end=" "`**: Prints values on the same line separated by spaces instead of newlines.

---

## 4. Lecture Outline

### 0:00–0:08 — Accessing Characters by Index
- `message[0]` through `message[5]` print `C`, `o`, `d`, `i`, `n`, `g`.

### 0:08–0:14 — Measuring Length
- `len(message)` counts every character, including the space.

### 0:14–0:21 — Looping Over the String
- `for char in message: print(char, end=" ")` lays all characters on one line.

### 0:21–0:28 — Looping Over a Range
- `for i in range(1, 10 + 1)` prints `1` to `10`.
- A final empty `print()` ends the line.

---

## 5. Code Demos

```python
message = "Coding Factory"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

print(f"Number of letters inside the {message}: {len(message)}")


# Iterate over each character in the string using an enhanced for loop
for char in message:
    print(char, end=" ")

for i in range(1, 10 + 1):
    print(i, end=" ")
print()
```

**Expected output:**

```
C
o
d
i
n
g
Number of letters inside the Coding Factory: 14
C o d i n g   F a c t o r y 1 2 3 4 5 6 7 8 9 10 
```

> 💡 `len(message)` is `14`, not `13`, because the space between "Coding" and "Factory" counts as a character. Also note the two `for` loops print on the same line: the first has no trailing newline, so the numbers continue right after the characters.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `"Python"[0]` return?
- a) `"y"`
- b) `"P"`
- c) `"Python"`
- d) `1`

<details>
<summary>Solution</summary>

**Answer:** b) `"P"`. Indexing starts at `0`.
</details>

---

### 2. (Level 1, Short Answer)
What is `len("Hi there")`?

<details>
<summary>Solution</summary>

`8` — six letters plus the space plus... let's count: H, i, space, t, h, e, r, e = 8 characters.
</details>

---

### 3. (Level 2, Coding)
Print the first and last character of `message = "Coding Factory"`. (Hint: the last index is `len(message) - 1`, or use `-1`.)

<details>
<summary>Solution</summary>

```python
message = "Coding Factory"
print(message[0])
print(message[-1])  # 'y'
```
</details>

---

### 4. (Level 2, Coding)
Use a `for` loop to print each character of `"CF9"` on its own line.

<details>
<summary>Solution</summary>

```python
for ch in "CF9":
    print(ch)
```
</details>

---

### 5. (Level 3, Coding)
Count and print how many times the letter `o` appears in `"Coding Factory"` using a loop.

<details>
<summary>Solution</summary>

```python
message = "Coding Factory"
count = 0
for ch in message:
    if ch == "o":
        count += 1
print("o appears", count, "times")  # 2
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `len()`](https://docs.python.org/3/library/functions.html#len)
- [Python Tutorial: Strings (indexing and slicing)](https://docs.python.org/3/tutorial/introduction.html#text)
- [Python Official Documentation: `range()`](https://docs.python.org/3/library/stdtypes.html#range)

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
