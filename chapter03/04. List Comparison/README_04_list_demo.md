# ⚖️ `is` vs `==`: Identity Versus Equality

This short, focused lesson nails one of Python's most-misunderstood distinctions. Two lists can hold exactly the same values yet be two separate objects. `==` asks "do they hold the same content?"; `is` asks "are they literally the same object?".

---

## 1. Learning Objectives

- Distinguish **identity** (`is`) from **equality** (`==`).
- Predict that two equal-but-separate lists are `==` `True` but `is` `False`.
- Understand when each operator is the right tool.

---

## 2. Prerequisites

- Familiarity with `id()` and object identity (lessons `01`–`02`).
- Comfort with lists and f-strings.

---

## 3. Key Concepts

- **`==` (equality)**: Compares **values/content**. For lists, it's `True` when they have the same elements in the same order.
- **`is` (identity)**: Compares **objects**. It's `True` only when both names point to the *same* object (same `id`).
- **Two literals → two objects**: `[10, 20, 30]` written twice creates two distinct lists, so `is` is `False`.
- **Idiom**: Use `is` mainly for singletons like `None` (`if x is None:`), and `==` for everything value-based.

---

## 4. Lecture Outline

### 0:00–0:08 — The Comparison Helper
- `compare_lists` prints both `is` and `==` results.

### 0:08–0:18 — Two Equal Lists
- `my_ints` and `your_ints` hold the same numbers.

### 0:18–0:26 — The Result
- `is` → `False` (different objects), `==` → `True` (same content).

---

## 5. Code Demos

```python
def compare_lists(list1, list2):
    print(f"{list1} is {list2}: {list1 is list2}")   # identity
    print(f"{list1} == {list2}: {list1 == list2}")   # content

def main():
    my_ints = [10, 20, 30]
    your_ints = [10, 20, 30]

    compare_lists(my_ints, your_ints)

if __name__ == "__main__":
    main()
```

**Expected output:**

```
[10, 20, 30] is [10, 20, 30]: False
[10, 20, 30] == [10, 20, 30]: True
```

> 💡 **Why `False` then `True`?** `my_ints` and `your_ints` were built from two separate list literals, so Python created two distinct objects in memory — `is` reports `False`. But their *contents* are identical, so `==` reports `True`. Content can be equal even when identity differs.

> ⚠️ **A classic bug.** Never write `if name is "Dimitris":` to compare strings, or `if x is 10:` to compare numbers. It may *appear* to work thanks to interning/caching, then fail unpredictably with other values. Use `==` for value comparisons; reserve `is` for `None` and other singletons.

---

## 6. Exercises

### 1. (Level 1, MCQ)
For `a = [1]; b = [1]`, what are `a == b` and `a is b`?
- a) `True`, `True`
- b) `True`, `False`
- c) `False`, `True`
- d) `False`, `False`

<details>
<summary>Solution</summary>

**Answer:** b) `a == b` is `True` (same content); `a is b` is `False` (different objects).
</details>

---

### 2. (Level 1, Short Answer)
In one sentence each, what do `is` and `==` test?

<details>
<summary>Solution</summary>

`is` tests whether two names refer to the *same object* (identity). `==` tests whether two objects have *equal value/content*.
</details>

---

### 3. (Level 2, Coding)
Create an alias `c = a` and show that `c is a` is `True`, then explain the difference from exercise 1.

<details>
<summary>Solution</summary>

```python
a = [1, 2, 3]
c = a            # alias — same object
print(c is a)    # True
print(c == a)    # True
```
Unlike two separate literals, `c = a` doesn't build a new list; it's a second name for the same object, so identity holds.
</details>

---

### 4. (Level 2, Short Answer)
Which operator should you use to check whether a variable `result` is `None`, and why?

<details>
<summary>Solution</summary>

Use `result is None`. `None` is a unique singleton object, so identity is the correct and recommended test (`==` could be overridden by a class's `__eq__`, `is` cannot be fooled).
</details>

---

### 5. (Level 3, Coding)
Demonstrate that `[1, 2] == [2, 1]` is `False` and explain why order matters for list equality.

<details>
<summary>Solution</summary>

```python
print([1, 2] == [2, 1])   # False
```
List equality compares elements **position by position**. The first elements (`1` vs `2`) already differ, so the lists are not equal — lists are ordered sequences, unlike sets.
</details>

---

## 7. Further Reading

- [Python Docs: Comparisons (`is`, `==`)](https://docs.python.org/3/reference/expressions.html#comparisons)
- [Python Docs: `object.__eq__`](https://docs.python.org/3/reference/datamodel.html#object.__eq__)
- [Python Docs: Identity comparisons](https://docs.python.org/3/reference/expressions.html#is)

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
