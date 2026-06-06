# 🔤 Using Literals in Python

This lesson explores how to write **literals** — the fixed values you type directly into your code. We look at integer literals in different number bases (decimal, binary, hexadecimal), several ways to write string literals (single quotes, double quotes, line continuation, and triple quotes), and the boolean literal `True`.

---

## 1. Learning Objectives

- Write integer literals in decimal, binary (`0b`), and hexadecimal (`0x`) form and understand they can represent the same value.
- Create string literals using single quotes, double quotes, and triple quotes.
- Use the backslash (`\`) for line continuation inside a string and understand how surrounding whitespace is kept.
- Build multi-line strings with triple quotes (`'''...'''`).
- Recognize the boolean literal `True` and how all literals print together.

---

## 2. Prerequisites

- Comfort declaring variables and assigning values.
- Knowing the four primitive types (`int`, `float`, `bool`, `str`).
- Ability to run a script and read its console output.

---

## 3. Key Concepts

- **Literal**: A value written directly in source code, such as `10`, `"CF"`, or `True`.
- **Decimal literal**: A normal base-10 number, e.g. `10`.
- **Binary literal**: A base-2 number prefixed with `0b`, e.g. `0b1010` (which equals `10`).
- **Hexadecimal literal**: A base-16 number prefixed with `0x`, e.g. `0x000A` (which also equals `10`).
- **String quoting**: Single (`'...'`) and double (`"..."`) quotes are equivalent in Python.
- **Line continuation (`\`)**: A backslash at the end of a line joins it with the next, with no newline inserted.
- **Triple-quoted string**: Text wrapped in `'''...'''` (or `"""..."""`) that may span several lines, preserving the line breaks.

---

## 4. Lecture Outline

### 0:00–0:06 — Integer Literals in Different Bases
- `num1 = 10` (decimal), `num2 = 0b1010` (binary), `num3 = 0x000A` (hex).
- All three store the same integer value: `10`.

### 0:06–0:12 — Single vs. Double Quotes
- `str1 = 'CF'` and `str2 = "CF"` are identical.
- Choosing one style consistently for readability.

### 0:12–0:18 — Line Continuation Inside Strings
- `str3 = 'Cod\` + new line + `    ing'`.
- The `\` removes the newline, but the leading spaces on the next line stay in the string.

### 0:18–0:24 — Multi-line Strings with Triple Quotes
- `str4` and `str5` span several lines.
- The line breaks you type are kept exactly in the value.

### 0:24–0:28 — Boolean Literal and Combined Output
- `my_bool = True`.
- Printing every literal together to compare results.

---

## 5. Code Demos

```python
num1 = 10
num2 = 0b1010
num3 = 0x000A

str1 = 'CF'
str2 = "CF"
str3 = 'Cod\
    ing'

str4 = '''Hello 
Coding 
Factory'''

str5 = '''Hello
Again
!'''

my_bool = True

print(num1, num2, num3, str1, str2, str3, str4, str5, my_bool)
```

**What to notice in the output:**

- `num1`, `num2`, and `num3` all print as `10` — different literal forms, same value.
- `str3` becomes `Cod    ing`: the `\` joined the lines, but the four leading spaces before `ing` remained part of the string.
- `str4` and `str5` print across multiple lines because the newlines are stored inside the triple-quoted strings.
- `my_bool` prints as `True`.

> 💡 Tip: To verify the integer literals are equal, try `print(num1 == num2 == num3)`, which prints `True`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What value does `0b1010` represent?
- a) `1010`
- b) `10`
- c) `2`
- d) `16`

<details>
<summary>Solution</summary>

**Answer:** b) `10`. The `0b` prefix means binary, and `1010` in base 2 equals 10 in base 10.
</details>

---

### 2. (Level 1, Short Answer)
Are `'CF'` and `"CF"` the same value in Python? Why or why not?

<details>
<summary>Solution</summary>

Yes. Single and double quotes are interchangeable for string literals in Python; both create the identical string `CF`.
</details>

---

### 3. (Level 2, Coding)
Write a hexadecimal literal for the value `255` and print it. The output should be `255`.

<details>
<summary>Solution</summary>

```python
value = 0xFF
print(value)
```
</details>

---

### 4. (Level 2, Coding)
Create a triple-quoted string variable `address` that prints across three lines:

```
123 Main Street
Athens
Greece
```

<details>
<summary>Solution</summary>

```python
address = '''123 Main Street
Athens
Greece'''

print(address)
```
</details>

---

### 5. (Level 3, Coding)
Using a single backslash for line continuation, create a string `word` whose value is exactly `Coding` (no extra spaces), split across two lines of source code. Print it.

<details>
<summary>Solution</summary>

```python
word = 'Cod\
ing'

print(word)  # -> Coding
```

Note: keep the second line flush to the left margin. Any indentation before `ing` would be included in the string (that is exactly why `str3` in the demo became `Cod    ing`).
</details>

---

## 7. Further Reading

- [Python Language Reference: Lexical Analysis — Literals](https://docs.python.org/3/reference/lexical_analysis.html#literals)
- [Python Official Documentation: Integer literals](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals)
- [Python Tutorial: Strings](https://docs.python.org/3/tutorial/introduction.html#text)

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
