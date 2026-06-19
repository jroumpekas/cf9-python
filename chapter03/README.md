# 🐍 Chapter 03 — Python Fundamentals Practice Collection

This repository contains a collection of small Python exercises and demo scripts from **Chapter 03**.  
Each example focuses on one specific programming concept, so the chapter can be studied step by step.

The goal of this chapter is to build confidence with **variables, object identity, mutable and immutable objects, conditions, loops, functions, lists, dictionaries, string operations, input validation, and basic problem solving**.

---

## 📚 Chapter Overview

Chapter 03 is organized as a set of mini-lessons.  
Each folder contains a small Python demo or exercise that can be studied independently.

| # | Lesson | Main Topic |
|---|--------|------------|
| 01 | Immutable ID Demo | Object identity, `id()`, immutability |
| 02 | Modifiable Objects Demo | Mutable objects and object references |
| 03 | Rectangle and Square Check | Conditional logic and geometric checks |
| 04 | List Comparison | Comparing list values and references |
| 05 | Ternary Operator Demo | One-line conditional expressions |
| 06 | Character to ASCII Conversion | `ord()`, characters, ASCII codes |
| 07 | Number Guessing Game | Loops, random numbers, user input |
| 08 | Armstrong Number Checker | Digits, loops, number logic |
| 09 | Sum and Product Calculator | Arithmetic operations and functions |
| 10 | Factorial Calculator | Repetition and factorial logic |
| 11 | Fibonacci Calculator | Fibonacci sequence calculation |
| 12 | Fibonacci Improvement | Cleaner / improved Fibonacci implementation |
| 13 | Name Spacing Demo | String joining, input cleanup, validation |
| 14 | Decrypt Message | String filtering and digit removal |
| 15 | Break Scheduler App | Searching with `break` and `for...else` |
| 16 | HTTP Error Handler | `match...case` pattern matching |
| 17 | HTTP Error Handler with Dictionary | Dictionary lookup with default values |
| 18 | Password Generator | Random password generation and input validation |

---

## 🎯 Learning Objectives

By completing this chapter, you will be able to:

- Understand the difference between **value** and **identity**.
- Explain the difference between **mutable** and **immutable** objects.
- Use `if`, `elif`, `else`, and ternary expressions.
- Work with strings, characters, lists, and dictionaries.
- Read and validate user input with `input()`.
- Use loops such as `for` and `while`.
- Stop loops early with `break`.
- Understand Python's `for...else` structure.
- Write small reusable functions.
- Use built-in functions such as `id()`, `ord()`, `len()`, `int()`, and `range()`.
- Use standard library modules such as `random` and `string`.
- Structure Python scripts with `main()` and the `if __name__ == "__main__"` guard.

---

## 🧠 Key Concepts Covered

### Object Identity and Mutability

The first lessons introduce the idea that variables in Python are names that point to objects.

Important concepts:

- `id(obj)`
- immutable objects
- mutable objects
- object references
- rebinding variables
- comparing identity with `is`
- comparing values with `==`

---

### Conditions and Comparisons

Several examples practice decision-making with conditional logic.

Important concepts:

- `if`
- `elif`
- `else`
- ternary operator
- Boolean expressions
- comparison operators
- case-insensitive comparison with `.casefold()`

---

### Loops and Repetition

Many exercises use loops to repeat logic, search values, or calculate results.

Important concepts:

- `for` loops
- `while` loops
- `break`
- `for...else`
- accumulator variables
- counters
- repeated input prompts

---

### Strings and Characters

The chapter includes several small string-processing exercises.

Important concepts:

- `.strip()`
- `.join()`
- `.isnumeric()`
- string iteration
- `ord()`
- removing unwanted characters
- building a new string step by step

---

### Functions and Program Structure

Most scripts are organized using functions.

Important concepts:

- defining functions
- parameters
- return values
- helper functions
- `main()`
- `if __name__ == "__main__"`

---

## 🗂️ Suggested Folder Structure

```text
chapter03/
├── 01. Immutable ID Demo/
├── 02. Modifiable Objects Demo/
├── 03. Rectangle and Square Check/
├── 04. List Comparison/
├── 05. Ternary Operator Demo/
├── 06. Character to ASCII Conversion/
├── 07. Number Guessing Game/
├── 08. Armstrong Number Checker/
├── 09. Sum and Product Calculator/
├── 10. Factorial Calculator/
├── 11. Fibonacci Calculator/
├── 12. Fibonacci Improvement/
├── 13. Name Spacing Demo/
├── 14. Decrypt Message/
├── 15. Break Scheduler App/
├── 16. HTTP Error Handler/
├── 17. HTTP Error Handler with Dictionary/
└── 18. Password Generator/
```

---

## ⚙️ Requirements

To run the examples, you need:

- Python 3.10 or newer
- A code editor such as VS Code or PyCharm
- Basic terminal usage

Most examples use only Python's built-in features.  
The password generator uses Python's standard library modules:

```python
import random
import string
```

No external packages are required.

---

## ▶️ How to Run the Scripts

Open a terminal inside the lesson folder and run the Python file.

Example:

```bash
python 13_name_spacing.py
```

or, depending on your system:

```bash
python3 13_name_spacing.py
```

For Windows with the Python launcher:

```bash
py 13_name_spacing.py
```

---

## 🧪 Example Usage

### Name Spacing Demo

```bash
python 13_name_spacing.py
```

Example input:

```text
Please give a name: Dimitris
```

Example output:

```text
D    i    m    i    t    r    i    s
```

---

### Decrypt Message

```bash
python 14_decrypt_demo.py
```

Expected output:

```text
Hello CF
```

---

### HTTP Error Handler

```bash
python 16_http_error_demo.py
```

Expected output:

```text
Not found
```

---

### Password Generator

```bash
python 18_password_gen.py
```

Example flow:

```text
Do you want to create a password? ('y' or 'q' for quit) y
Please give the password length: 12

Generated password: A8k@pL2m#Qx9
```

---

## 🧭 Recommended Study Path

A good way to study this chapter is:

1. Start with lessons **01–02** to understand object identity and mutability.
2. Continue with lessons **03–06** to practice conditions, comparisons, and basic built-ins.
3. Move to lessons **07–12** for loops and number-based exercises.
4. Finish with lessons **13–18** for strings, dictionaries, pattern matching, and small practical scripts.

---

## ✅ Practice Checklist

Use this checklist while studying:

- [ ] I can explain what `id()` returns.
- [ ] I understand the difference between mutable and immutable objects.
- [ ] I can compare values with `==`.
- [ ] I know when `is` should be used.
- [ ] I can write `if / elif / else` statements.
- [ ] I can use a ternary operator.
- [ ] I can loop through strings and lists.
- [ ] I can stop a loop with `break`.
- [ ] I understand how `for...else` works.
- [ ] I can write a simple function with parameters.
- [ ] I can return a result from a function.
- [ ] I can validate user input.
- [ ] I can use a dictionary for lookup logic.
- [ ] I can use `random.choice()` to generate random values.

---

## 📝 Notes for Beginners

Do not try to memorize everything at once.  
The purpose of these examples is to understand the logic behind each small program.

For each script, try to answer:

- What is the input?
- What processing happens?
- What is the output?
- Which Python concept is being practiced?
- What would happen if the user gives invalid input?

---

## 🚀 Possible Improvements

Some useful improvements you can add later:

- Add more input validation.
- Add more examples for each script.
- Convert repeated logic into helper functions.
- Add unit tests with `pytest`.
- Add screenshots or terminal output examples.
- Group similar scripts into subfolders.
- Add a separate README file inside each lesson folder.

---

## 📖 Further Reading

- [Python Docs: Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python Docs: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Docs: Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Docs: String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Docs: random](https://docs.python.org/3/library/random.html)
- [Python Docs: string](https://docs.python.org/3/library/string.html)

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

---

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

---

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: These are Python scripts and require a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
