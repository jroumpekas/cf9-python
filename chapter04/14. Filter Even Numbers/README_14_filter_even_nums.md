# 🔎 Filtering Even Numbers with `filter()`

This lesson demonstrates how to use Python's built-in `filter()` function with a lambda expression.

The example filters a list of numbers and keeps only the even numbers.

---

## 1. Learning Objectives

- Use `filter()` to select items from an iterable.
- Write a lambda condition.
- Check whether a number is even using `%`.
- Convert a filter object into a list.
- Understand that filter objects are iterators.

---

## 2. Prerequisites

- Lists.
- Loops.
- Lambda functions.
- Basic arithmetic operators.

---

## 3. Key Concepts

- **`filter(function, iterable)`**: Keeps items for which the function returns `True`.
- **Lambda predicate**: A small function used as a condition.
- **Modulo operator `%`**: Gives the remainder of a division.
- **Even number**: A number where `x % 2 == 0`.
- **Iterator**: An object that produces values one at a time.

---

## 4. Lecture Outline

### 0:00–0:08 — Number List
- Create numbers from 1 to 10.

### 0:08–0:18 — Filter Object
- Use `filter(lambda x: x % 2 == 0, numbers)`.

### 0:18–0:26 — Convert to List
- Use `list(filter(...))`.

### 0:26–0:34 — Print Results
- Loop through the even numbers.

---

## 5. Code Demo

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers_iter = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers_iter)

even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers))

for num in even_numbers_list:
    print(num, end="\t")
print()
```

---

## 6. Expected Output

The first print shows a filter object address, which differs by machine:

```text
<filter object at 0x...>
2    4    6    8    10
```

---

## 7. Important Note

A `filter` object is an iterator.  
Once it has been consumed, it cannot be reused unless you create it again.

---

## 8. Exercises

### 1. Level 1 — MCQ
Which condition keeps even numbers?

- a) `x % 2 == 0`
- b) `x % 2 == 1`
- c) `x > 10`
- d) `x == 0`

<details>
<summary>Solution</summary>

**Answer:** a) `x % 2 == 0`.
</details>

---

### 2. Level 1 — Short Answer
What does `filter()` return?

<details>
<summary>Solution</summary>

It returns a filter object, which is an iterator.
</details>

---

### 3. Level 2 — Coding
Filter only the odd numbers from the list.

<details>
<summary>Solution</summary>

```python
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
```
</details>

---

### 4. Level 2 — Short Answer
Why do we often wrap `filter()` with `list()`?

<details>
<summary>Solution</summary>

Because `filter()` returns an iterator. `list()` lets us see all filtered values at once.
</details>

---

## 9. Further Reading

- [Python Docs: filter](https://docs.python.org/3/library/functions.html#filter)
- [Python Docs: Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

---

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

---

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
