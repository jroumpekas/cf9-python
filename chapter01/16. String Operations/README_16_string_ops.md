# 🔗 String Operations: Concatenation and Repetition

This lesson covers two fundamental string operations: joining strings together with `+` (concatenation) and repeating a string with `*` (repetition). We also see that repetition works in either order — `str * n` and `n * str` give the same result.

---

## 1. Learning Objectives

- Join two strings with the `+` operator.
- Repeat a string a number of times with the `*` operator.
- Understand that string repetition is commutative (`s * 3` equals `3 * s`).
- Predict the exact output of concatenation and repetition.
- Recognize that `+` and `*` mean different things for strings than for numbers.

---

## 2. Prerequisites

- Knowing how to declare string variables.
- Familiarity with `print()`.
- Awareness that operators can behave differently per type.

---

## 3. Key Concepts

- **Concatenation (`+`)**: `"a" + "b"` produces `"ab"`. Both operands must be strings.
- **Repetition (`*`)**: `"ab" * 3` produces `"ababab"`. One operand is a string, the other an integer.
- **Commutative repetition**: `"x" * 3` and `3 * "x"` give the same string.
- **Spaces matter**: A trailing space in a string is repeated/joined like any other character.

---

## 4. Lecture Outline

### 0:00–0:07 — Concatenation
- `str3 = str1 + str2` joins `"Hello "` and `"Coding Factory"`.

### 0:07–0:14 — Repetition
- `str4 = str1 * 7` repeats `"Hello "` seven times.

### 0:14–0:20 — Order Does Not Matter
- `str5 = 3 * str1` works exactly like `str1 * 3`.

---

## 5. Code Demos

```python
str1 = "Hello "
str2 = "Coding Factory"

str3 = str1 + str2
print(str3)

# ...
str4 = str1 * 7
print(str4)

str5 = 3 * str1
print(str5)
```

**Expected output:**

```
Hello Coding Factory
Hello Hello Hello Hello Hello Hello Hello 
Hello Hello Hello 
```

> 💡 Notice the trailing space in `"Hello "`. It is part of the string, so it appears between each repetition and at the very end of the repeated lines.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is the result of `"ab" * 3`?
- a) `"ab3"`
- b) `"ababab"`
- c) `"6"`
- d) An error

<details>
<summary>Solution</summary>

**Answer:** b) `"ababab"`.
</details>

---

### 2. (Level 1, Short Answer)
Does `"hi" + 3` work? Why or why not?

<details>
<summary>Solution</summary>

No. You cannot concatenate a string with an integer; it raises a `TypeError`. You would need `"hi" + str(3)`.
</details>

---

### 3. (Level 2, Coding)
Print a line of 20 dashes using string repetition.

<details>
<summary>Solution</summary>

```python
print("-" * 20)
```
</details>

---

### 4. (Level 2, Coding)
Given `first = "Jane"` and `last = "Doe"`, print `Jane Doe` using concatenation (mind the space).

<details>
<summary>Solution</summary>

```python
first = "Jane"
last = "Doe"
print(first + " " + last)
```
</details>

---

### 5. (Level 3, Coding)
Build a simple progress bar string of 10 filled blocks followed by 5 empty ones, like `██████████-----`.

<details>
<summary>Solution</summary>

```python
bar = "█" * 10 + "-" * 5
print(bar)
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Official Documentation: Text Sequence Type — `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
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
