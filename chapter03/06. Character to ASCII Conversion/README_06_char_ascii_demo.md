# 🔤 Characters & ASCII Values with `ord()`

This lesson reads characters from the user and prints their ASCII (Unicode) code points using `ord()`. It shows **two ways** to write the same sentinel-controlled loop — a "read first" `while` and a cleaner `while True` with `break`.

---

## 1. Learning Objectives

- Convert a character to its numeric code with `ord()`.
- Write a **sentinel-controlled loop** that stops on a special value (`'#'`).
- Compare the "priming read" pattern with the `while True` + `break` pattern.
- Recognise the edge cases where `ord()` raises an error.

---

## 2. Prerequisites

- Comfort with `input()`, `while` loops, and `break`.
- Familiarity with f-strings.

---

## 3. Key Concepts

- **`ord(ch)`**: Returns the Unicode code point of a **single** character, e.g. `ord('A')` → `65`.
- **Sentinel value**: A special input (`'#'`) that signals "stop". The loop runs until the sentinel is entered.
- **Priming read**: `process_characters()` reads once *before* the loop, then again at the bottom — the input statement is duplicated.
- **`while True` + `break`**: `process_characters2()` reads in one place and breaks on the sentinel — usually the cleaner pattern (no duplicated input line).

---

## 4. Lecture Outline

### 0:00–0:10 — Version 1: Priming Read
- Read once, loop `while ch != '#'`, read again at the end.

### 0:10–0:20 — Version 2: `while True` + `break`
- Read once inside the loop; `break` when `ch == '#'`.

### 0:20–0:28 — Why Version 2 Is Preferred
- A single input statement means one place to change and no risk of the two getting out of sync.

---

## 5. Code Demos

```python
def process_characters():
    """Print ASCII values until the user enters '#'. (priming-read version)"""
    ch = input("Please insert a char: ")
    while ch != '#':
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")
    print("Goodbye")

def process_characters2():
    """Print ASCII values until the user enters '#'. (while True version)"""
    while True:
        ch = input("Please insert a char (or '#' to quit): ")
        if ch == '#':
            break
        print(f"{ch}: {ord(ch)}")
    print("Goodbye")

def main():
    process_characters()
    process_characters2()

if __name__ == "__main__":
    main()
```

**Example run:**

```
Please insert a char: A
A : 65
Please insert a char: z
z : 122
Please insert a char: #
Goodbye
...
```

> 💡 **Two patterns, one behaviour.** The priming-read version duplicates the `input(...)` line — easy to forget to update both. The `while True` + `break` version keeps the read in exactly one place, which is why it's generally preferred for sentinel loops.

> ⚠️ **`ord()` wants exactly one character.** If the user presses Enter with no input (`""`) or types more than one character (`"ab"`), `ord()` raises `TypeError: ord() expected a character, but string of length N found`. A robust version would check `len(ch) == 1` before calling `ord(ch)`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `ord('a')` return?
- a) `65`
- b) `97`
- c) `'a'`
- d) `1`

<details>
<summary>Solution</summary>

**Answer:** b) `97`. (Uppercase `'A'` is `65`; lowercase letters start at `97`.)
</details>

---

### 2. (Level 1, Short Answer)
What is a "sentinel value" in this program?

<details>
<summary>Solution</summary>

It's the special input `'#'` that signals the loop should stop. The loop keeps reading characters until the sentinel is entered.
</details>

---

### 3. (Level 2, Coding)
Add a guard so the program skips empty or multi-character input instead of crashing.

<details>
<summary>Solution</summary>

```python
while True:
    ch = input("Char (# to quit): ")
    if ch == '#':
        break
    if len(ch) != 1:
        print("Please enter exactly one character.")
        continue
    print(f"{ch}: {ord(ch)}")
```
</details>

---

### 4. (Level 2, Coding)
Use `chr()` (the inverse of `ord()`) to print the character for code point `100`.

<details>
<summary>Solution</summary>

```python
print(chr(100))   # d
```
`chr` turns a number back into its character; `ord` and `chr` are inverses.
</details>

---

### 5. (Level 3, Coding)
Print every uppercase letter `A`–`Z` with its ASCII value using a loop over `ord` values.

<details>
<summary>Solution</summary>

```python
for code in range(ord('A'), ord('Z') + 1):
    print(chr(code), code)
```
</details>

---

## 7. Further Reading

- [Python Docs: `ord`](https://docs.python.org/3/library/functions.html#ord)
- [Python Docs: `chr`](https://docs.python.org/3/library/functions.html#chr)
- [Python Tutorial: `break` and `continue`](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

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
