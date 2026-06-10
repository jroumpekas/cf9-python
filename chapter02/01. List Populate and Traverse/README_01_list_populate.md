# 📋 Lists, Iteration, and `enumerate()`

This lesson works with a list of values and shows two ways to loop over it: a simple `for` loop over the elements, and `enumerate()`, which gives you both the index and the value at the same time. It also contains a small typo worth studying, because it changes what gets printed.

---

## 1. Learning Objectives

- Create a list and print it.
- Iterate over a list's elements with a `for` loop.
- Use `enumerate()` to get `(index, value)` pairs while looping.
- Unpack a tuple into multiple variables (`a, b = (10, 20)`).
- Spot a common loop bug: printing the whole list instead of the current element.

---

## 2. Prerequisites

- Knowing what a list is and how to create one.
- Familiarity with `for` loops and `print()`.
- Basic f-string usage.

---

## 3. Key Concepts

- **List**: An ordered, changeable collection, e.g. `[19, 23, 34, 45]`.
- **Iterating elements**: `for age in ages` gives you each value in turn.
- **`enumerate(seq)`**: Yields pairs of `(index, value)`, so you can track position while looping.
- **Tuple unpacking**: `a, b = (10, 20)` assigns `a = 10` and `b = 20` in one line.
- **`end=" "`**: Keeps `print()` output on the same line with a space instead of a newline.

---

## 4. Lecture Outline

### 0:00–0:06 — Creating and Printing a List
- `ages = [19, 23, 34, 45]` and `print("Initial list of ages:", ages)`.

### 0:06–0:13 — Looping Over Elements (and a Typo)
- `for age in ages: print(ages, end=" ")` accidentally prints the whole list each time.
- The intended line was `print(age, end=" ")`.

### 0:13–0:18 — Tuple Unpacking
- `a, b = (10, 20)` as a quick aside on unpacking.

### 0:18–0:26 — Looping with `enumerate()`
- `for index, value in enumerate(ages)` to print both position and value.

---

## 5. Code Demos

```python
ages = [19, 23, 34, 45]

print("Initial list of ages:", ages)

# Read: Iterating over a list with an enhanced for loop
for age in ages:
    print(ages, end=" ")
print()

# enumerate()
# Read: Iterate over a list using enumerate -> (index, value)
a, b = (10, 20)
for index, value in enumerate(ages):
    print(f"Index: {index}, Value: {value}")
```

**Actual output:**

```
Initial list of ages: [19, 23, 34, 45]
[19, 23, 34, 45] [19, 23, 34, 45] [19, 23, 34, 45] [19, 23, 34, 45] 
Index: 0, Value: 19
Index: 1, Value: 23
Index: 2, Value: 34
Index: 3, Value: 45
```

> ⚠️ **Look at the second line.** The loop prints the **entire list** four times, because it says `print(ages, ...)` (the whole list) instead of `print(age, ...)` (the current element). The intended version:
>
> ```python
> for age in ages:
>     print(age, end=" ")
> # -> 19 23 34 45
> ```
>
> The `a, b = (10, 20)` line is unrelated to the loop — it just demonstrates tuple unpacking and is not used afterward.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `enumerate(["a", "b"])` yield on each iteration?
- a) Just the values
- b) Just the indexes
- c) `(index, value)` pairs
- d) `(value, index)` pairs

<details>
<summary>Solution</summary>

**Answer:** c) `(index, value)` pairs, with indexes starting at `0`.
</details>

---

### 2. (Level 1, Short Answer)
After `x, y = (1, 2)`, what are the values of `x` and `y`?

<details>
<summary>Solution</summary>

`x` is `1` and `y` is `2`.
</details>

---

### 3. (Level 2, Coding)
Fix the buggy loop so it prints each age on the same line separated by spaces: `19 23 34 45`.

<details>
<summary>Solution</summary>

```python
ages = [19, 23, 34, 45]
for age in ages:
    print(age, end=" ")
print()
```
</details>

---

### 4. (Level 2, Coding)
Use `enumerate()` to print a numbered list (starting at 1) of the fruits `["Apple", "Pear", "Plum"]`, like `1. Apple`.

<details>
<summary>Solution</summary>

```python
fruits = ["Apple", "Pear", "Plum"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```
</details>

---

### 5. (Level 3, Coding)
Given `ages = [19, 23, 34, 45]`, print only the ages that are 30 or older, along with their index.

<details>
<summary>Solution</summary>

```python
ages = [19, 23, 34, 45]
for index, age in enumerate(ages):
    if age >= 30:
        print(f"Index {index}: {age}")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: `enumerate()`](https://docs.python.org/3/library/functions.html#enumerate)
- [Python Tutorial: Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python Tutorial: Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)

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
