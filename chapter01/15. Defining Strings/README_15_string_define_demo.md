# 📝 Defining Strings: Quotes and Multi-line Text

This lesson shows the different ways to create string values in Python: single quotes, double quotes, and triple quotes for multi-line text. We see that single and double quotes are equivalent, while triple quotes preserve line breaks exactly as written.

---

## 1. Learning Objectives

- Create strings with single quotes (`'...'`) and double quotes (`"..."`).
- Understand that single and double quotes are interchangeable.
- Build multi-line strings with triple single quotes (`'''...'''`).
- Build multi-line strings with triple double quotes (`"""..."""`).
- Predict how multi-line strings print across several lines.

---

## 2. Prerequisites

- Knowing what a string is.
- Familiarity with `print()`.
- Awareness that whitespace and newlines are characters too.

---

## 3. Key Concepts

- **Single vs. double quotes**: `'Hello'` and `"Hello"` create identical strings.
- **Triple-quoted strings**: Wrapped in `'''...'''` or `"""..."""`, they may span multiple lines.
- **Preserved newlines**: Each line break you type inside triple quotes becomes a newline in the string.
- **Choosing a quote style**: Use double quotes when the text contains an apostrophe, and vice versa.

---

## 4. Lecture Outline

### 0:00–0:06 — Single and Double Quotes
- `str1 = 'Hello'` and `str2 = "Coding Factory"`.

### 0:06–0:14 — Triple Single Quotes
- `str3` spans three lines: `I` / `Love` / `Python`.

### 0:14–0:20 — Triple Double Quotes
- `str4` spells `Python` one letter per line.

### 0:20–0:26 — Printing Multi-line Strings
- How the stored newlines appear in the output.

---

## 5. Code Demos

```python
# Define a string using single quotes
str1 = 'Hello'

# Define a string using double quotes
str2 = "Coding Factory"

# Define a multi-line string using triple single quotes
str3 = '''I
Love
Python'''

# Define a multi-line string using triple double quotes
str4 = """P
y
t
h
o
n"""

print(str1)
print(str2)
print(str3)
print(str4)
```

**Expected output:**

```
Hello
Coding Factory
I
Love
Python
P
y
t
h
o
n
```

> 💡 Triple-quoted strings are also commonly used for docstrings (the description at the top of a function or module). The newlines you type are kept exactly.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which of these does **not** create a valid string?
- a) `'cat'`
- b) `"cat"`
- c) `'''cat'''`
- d) `cat`

<details>
<summary>Solution</summary>

**Answer:** d) `cat` — without quotes, Python treats it as a variable name, not a string.
</details>

---

### 2. (Level 1, Short Answer)
Are `'Python'` and `"Python"` the same value?

<details>
<summary>Solution</summary>

Yes. The choice of single or double quotes does not change the string.
</details>

---

### 3. (Level 2, Coding)
Create a triple-quoted string that prints exactly:

```
Roses are red
Violets are blue
```

<details>
<summary>Solution</summary>

```python
poem = '''Roses are red
Violets are blue'''
print(poem)
```
</details>

---

### 4. (Level 2, Short Answer)
Why is it useful to have both single and double quotes available? Give an example.

<details>
<summary>Solution</summary>

So you can include the other quote character inside a string without escaping, e.g. `"It's sunny"` uses double quotes so the apostrophe needs no backslash.
</details>

---

### 5. (Level 3, Coding)
Store your full name and city in a single triple-quoted string, each on its own line, and print it.

<details>
<summary>Solution</summary>

```python
info = '''Dimitris Roumpekas
Athens'''
print(info)
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Text Sequence Type — `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python Reference: String literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)
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
