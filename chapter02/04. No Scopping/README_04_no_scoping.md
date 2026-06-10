# 🌐 No Block Scope: Loop Variables Leak in Python

This lesson demonstrates an important Python behaviour: `for` loops and `if` blocks do **not** create their own scope. Variables you assign inside a loop body remain accessible after the loop ends. We build a list of random numbers and then read loop-defined variables afterward to prove the point.

---

## 1. Learning Objectives

- Generate random integers with the `random` module.
- Build a list by appending inside a loop.
- Understand that Python has function/module scope, not block scope.
- See that variables assigned inside a `for` or `if` block persist afterward.
- Recognize the risk: a variable may be undefined if the block never ran.

---

## 2. Prerequisites

- Familiarity with `for` loops, `if`, and lists.
- Knowing how to import a module.
- Basic understanding of the modulo operator (`%`).

---

## 3. Key Concepts

- **`random.randint(a, b)`**: Returns a random integer between `a` and `b`, inclusive.
- **`list.append(x)`**: Adds `x` to the end of a list.
- **No block scope**: Unlike C/Java, `for` and `if` blocks do not limit where a variable is visible.
- **Variables leak**: `even`, `name`, and the loop variable `num` are all still usable after the loop.
- **Conditional definition risk**: If the `if` never runs, the variable it would define stays undefined and raises `NameError` when used.

---

## 4. Lecture Outline

### 0:00–0:08 — Building a Random List
- Looping 10 times, appending `random.randint(1, 100)`.

### 0:08–0:16 — Assigning Inside Loops and Ifs
- `even = num` and `name = "Katerina"` are set inside the `if`.

### 0:16–0:24 — Reading Them After the Loop
- `even`, `name`, and `num` all still hold their last values.
- Why this works: no block-level scoping in Python.

### 0:24–0:30 — The Hidden Risk
- If no even number existed, `even` and `name` would be undefined.

---

## 5. Code Demos

```python
import random

random_numbers = []

for i in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)

print(random_numbers)

for num in random_numbers:
    if num % 2 == 0:
        even = num
        name = "Katerina"

print(f"Even: {even}")
print(name)
print(num)
```

**Example output** (your numbers will differ):

```
[42, 7, 88, 13, 90, 5, 64, 21, 6, 77]
Even: 6
Katerina
77
```

> 💡 **What just happened?** `even` and `name` were created *inside* the `if`, yet we read them after the loop with no error — Python does not scope variables to `for`/`if` blocks. `even` holds the **last** even number seen, and `num` holds the **last** element of the list (whether even or odd).
>
> ⚠️ **The catch:** this only works because the list contained at least one even number. If every number were odd, `even` and `name` would never be assigned, and `print(f"Even: {even}")` would raise:
>
> ```
> NameError: name 'even' is not defined
> ```
>
> A safer pattern is to initialise such variables *before* the loop (e.g. `even = None`).

---

## 6. Exercises

### 1. (Level 1, MCQ)
After a `for` loop `for i in range(3): ...`, what is the value of `i`?
- a) Undefined (out of scope)
- b) `0`
- c) `2`
- d) `3`

<details>
<summary>Solution</summary>

**Answer:** c) `2`. The loop variable keeps its last value and is still accessible.
</details>

---

### 2. (Level 1, Short Answer)
Does Python create a new scope for the body of an `if` statement?

<details>
<summary>Solution</summary>

No. Python uses function/module scope, not block scope, so variables defined inside an `if` remain visible afterward.
</details>

---

### 3. (Level 2, Coding)
Rewrite the second loop so `even` is safely initialised before the loop and prints `None` if no even number is found.

<details>
<summary>Solution</summary>

```python
even = None
for num in random_numbers:
    if num % 2 == 0:
        even = num
print(f"Even: {even}")
```
</details>

---

### 4. (Level 2, Coding)
Generate 5 random numbers between 1 and 6 (like dice rolls) and print them as a list.

<details>
<summary>Solution</summary>

```python
import random
rolls = [random.randint(1, 6) for _ in range(5)]
print(rolls)
```
</details>

---

### 5. (Level 3, Coding)
From a list of random numbers, collect **all** even numbers into a new list (not just the last one) and print it.

<details>
<summary>Solution</summary>

```python
import random
numbers = [random.randint(1, 100) for _ in range(10)]
evens = [n for n in numbers if n % 2 == 0]
print("All evens:", evens)
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `random`](https://docs.python.org/3/library/random.html)
- [Python Tutorial: Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Python Tutorial: `list.append()` and list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

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
