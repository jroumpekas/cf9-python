# 🖨️ The `print()` Function: `sep` and `end`

This lesson takes a closer look at Python's `print()` function. Beyond simply showing values, `print()` accepts the keyword arguments `sep` and `end`, which control how multiple values are separated and what is written after the line. We use them to format console output exactly the way we want.

---

## 1. Learning Objectives

- Print several values in one `print()` call and understand the default spacing.
- Use the `sep` argument to change the separator placed between values.
- Use the `end` argument to change what is printed at the end of a line (instead of a newline).
- Combine `sep` and `end` to join the output of consecutive `print()` calls.
- Read tab-separated (`\t`) output correctly.

---

## 2. Prerequisites

- Knowing how to declare variables of basic types.
- Having printed values to the console before.
- Understanding what an escape sequence like `\t` (tab) is.

---

## 3. Key Concepts

- **`print()` multiple values**: Passing several arguments prints them on one line.
- **`sep`**: The string placed *between* values. Its default is a single space `' '`.
- **`end`**: The string printed *after* all values. Its default is a newline `'\n'`.
- **`\t` (tab)**: An escape sequence that inserts a horizontal tab, useful for aligning columns.
- **Joining lines**: Setting `end` to something other than `'\n'` keeps the next `print()` on the same line.

---

## 4. Lecture Outline

### 0:00–0:06 — Default Behaviour
- `print(my_int, my_float, my_str)` separates values with spaces and ends with a newline.

### 0:06–0:13 — Changing the Separator with `sep`
- `print(..., sep='\t')` places a tab between each value.
- When to prefer tabs over spaces for alignment.

### 0:13–0:20 — Changing the Line Ending with `end`
- `end="*"` replaces the automatic newline.
- The following `print()` continues on the same line right after the `*`.

### 0:20–0:26 — Combining `sep` and `end`
- Using both arguments together in a single call.
- Predicting the exact output before running the code.

---

## 5. Code Demos

```python
my_int = 10
my_float = 5.7
my_str = "Hello CF9"

print("Hello comma separated values: ")

print(my_int, my_float, my_str)

print("----------------------------")

print(my_int, my_float, my_str, sep='\t')

print("----------------------------")

print(my_int, my_float, my_str, sep='\t', end="*")
print("Hello friends")
```

**Expected output:**

```
Hello comma separated values: 
10 5.7 Hello CF9
----------------------------
10	5.7	Hello CF9
----------------------------
10	5.7	Hello CF9*Hello friends
```

> 💡 Notice the last two lines: because `end="*"` replaced the newline, `Hello friends` printed right after the `*` on the **same** line.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is the default value of the `end` argument in `print()`?
- a) A space `' '`
- b) An empty string `''`
- c) A newline `'\n'`
- d) A tab `'\t'`

<details>
<summary>Solution</summary>

**Answer:** c) A newline `'\n'`. That is why each `print()` normally starts on a new line.
</details>

---

### 2. (Level 1, Short Answer)
What does `print("a", "b", "c", sep="-")` output?

<details>
<summary>Solution</summary>

**Output:** `a-b-c` — the dash replaces the default space between the values.
</details>

---

### 3. (Level 2, Coding)
Print the numbers `1`, `2`, and `3` separated by commas, producing exactly:
`1, 2, 3`

<details>
<summary>Solution</summary>

```python
print(1, 2, 3, sep=", ")
```
</details>

---

### 4. (Level 2, Coding)
Use two `print()` calls so that the final output is a single line:
`Loading...done`

<details>
<summary>Solution</summary>

```python
print("Loading...", end="")
print("done")
```
</details>

---

### 5. (Level 3, Coding)
Print three product names separated by tabs, and on the same line append the text ` | END`. Aim for output similar to:
`Pen	Book	Lamp | END`

<details>
<summary>Solution</summary>

```python
print("Pen", "Book", "Lamp", sep="\t", end="")
print(" | END")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `print()` function](https://docs.python.org/3/library/functions.html#print)
- [Python Reference: String and Bytes literals (escape sequences)](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)
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
