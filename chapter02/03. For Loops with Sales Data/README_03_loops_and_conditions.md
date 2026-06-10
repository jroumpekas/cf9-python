# 🍊 Loops, Conditions, and the `in` Operator

This lesson checks whether a value exists in a list. It contrasts a manual `for` loop with conditions against Python's clean `in` operator and a one-line conditional expression. It also contains an instructive bug that quietly produces the wrong result.

---

## 1. Learning Objectives

- Loop through a list and compare each element with a target value.
- Use `break` to stop a loop once a match is found.
- Use the `in` operator to check membership directly.
- Write a one-line conditional expression (`'in' if ... else 'not in'`).
- Diagnose a subtle bug: comparing the whole list instead of the current element.

---

## 2. Prerequisites

- Familiarity with lists and `for` loops.
- Understanding of `if`/`else` and comparison with `==`.
- Basic f-string usage.

---

## 3. Key Concepts

- **Element vs. collection**: `fruit` is one item; `fruits` is the whole list. Comparing the list to a string is never equal.
- **`==`**: Tests equality; `fruits == "Orange"` is always `False` (list vs. string).
- **`break`**: Exits the loop immediately once a match is found.
- **`in` operator**: `value in list` returns `True`/`False` for membership in one step.
- **Conditional expression**: `A if condition else B` chooses a value inline.

---

## 4. Lecture Outline

### 0:00–0:07 — Setting Up the List and Target
- `fruits = [...]`, `fruit_to_check = "Orange"`.

### 0:07–0:16 — The Manual Loop (with a Bug)
- The intent: compare each `fruit` to `fruit_to_check`.
- The bug: the code compares `fruits` (the list) instead of `fruit` (the element), so the `if` is never `True`.

### 0:16–0:24 — The Clean One-Liner
- `fruit_to_check in fruits` plus a conditional expression gives the correct answer in one line.

---

## 5. Code Demos

```python
# List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# Fruit we want to check
fruit_to_check = "Orange"

for fruit in fruits:
    if fruits == fruit_to_check:        # bug: 'fruits' (list) instead of 'fruit'
        print(f"{fruit_to_check} is in your list. ")
        break
    else:
        print(f"{fruit_to_check} is NOT in your list. ")

# One-liner condition check
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} your list")
```

**Actual output:**

```
Orange is NOT in your list. 
Orange is NOT in your list. 
Orange is NOT in your list. 
Orange is NOT in your list. 
Orange is in your list
```

> ⚠️ **The two parts disagree — and the loop is wrong.** The condition `fruits == fruit_to_check` compares the **whole list** to the string `"Orange"`, which is always `False`, so the `else` branch runs for every element and prints "NOT in your list" four times. The one-liner uses `in` correctly and reports the truth: Orange *is* in the list.
>
> **Corrected loop:**
>
> ```python
> for fruit in fruits:
>     if fruit == fruit_to_check:     # compare the element, not the list
>         print(f"{fruit_to_check} is in your list.")
>         break
> else:
>     print(f"{fruit_to_check} is NOT in your list.")
> ```
>
> Note the `else` here is attached to the **`for`** loop: it runs only if the loop finished without hitting `break` (i.e. no match was found).

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `"Mango" in ["Banana", "Mango"]` return?
- a) `0`
- b) `True`
- c) `"Mango"`
- d) An error

<details>
<summary>Solution</summary>

**Answer:** b) `True`.
</details>

---

### 2. (Level 1, Short Answer)
Why is `["a", "b"] == "a"` always `False`?

<details>
<summary>Solution</summary>

Because a list and a string are different types and can never be equal; the list is a collection, not a single string.
</details>

---

### 3. (Level 2, Coding)
Rewrite the membership check using only the `in` operator and an `if`/`else`.

<details>
<summary>Solution</summary>

```python
if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in your list.")
else:
    print(f"{fruit_to_check} is NOT in your list.")
```
</details>

---

### 4. (Level 2, Coding)
Use a `for`/`else` loop to report whether the number `7` is in `[2, 4, 6, 8]`.

<details>
<summary>Solution</summary>

```python
numbers = [2, 4, 6, 8]
for n in numbers:
    if n == 7:
        print("Found 7")
        break
else:
    print("7 is not in the list")
```
</details>

---

### 5. (Level 3, Coding)
Write a one-liner that prints `Orange: available` or `Orange: out of stock` depending on whether it is in `fruits`.

<details>
<summary>Solution</summary>

```python
print(f"Orange: {'available' if 'Orange' in fruits else 'out of stock'}")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Membership test operations (`in`)](https://docs.python.org/3/reference/expressions.html#membership-test-operations)
- [Python Tutorial: `break` and `else` on loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- [Python Reference: Conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

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
