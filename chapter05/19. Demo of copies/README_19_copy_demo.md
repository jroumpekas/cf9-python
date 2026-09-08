# 📋 Shallow Copy vs Deep Copy Demo

This lesson demonstrates the difference between shallow copies and deep copies in Python.

The script creates several copies of a nested list and then modifies both a top-level item and a nested item.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `19_demo_of_copies.py` | Demonstrates slicing, `.copy()`, `list()`, and `copy.deepcopy()` with a nested list. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Create shallow copies using slicing.
- Create shallow copies using `.copy()`.
- Create shallow copies using `list()`.
- Create deep copies using `copy.deepcopy()`.
- Understand why nested mutable objects are shared in shallow copies.
- Understand why deep copies are independent.

---

## 2. Prerequisites

- Lists.
- Nested lists.
- Mutability.
- Object references.
- Basic imports.

---

## 3. Key Concepts

### Shallow Copy

A shallow copy creates a new outer list, but nested objects are still shared.

```python
ages_slice = ages[:]
ages_cp = ages.copy()
ages_list = list(ages)
```

---

### Deep Copy

A deep copy creates a new outer list and also copies nested mutable objects.

```python
ages_deep_copy = copy.deepcopy(ages)
```

---

### Nested Mutation

This modifies a nested list:

```python
ages[1][0] = 200
```

Shallow copies see this change because they share the same nested list.

---

## 4. Code Demo

```python
import copy

def main():
    ages = [1, [2, 3, 4], 5]

    ages_slice = ages[:]
    ages_cp = ages.copy()
    ages_list = list(ages)
    ages_deep_copy = copy.deepcopy(ages)

    print(f"Original list: {ages}")
    print(f"Shallow copy with slicing: {ages_slice}")
    print(f"Shallow copy with list copy method: {ages_cp}")
    print(f"Deep copy: {ages_deep_copy}")

    ages[0] = 100
    ages[1][0] = 200

    print(f"Original list: {ages}")
    print(f"Shallow copy with slicing: {ages_slice}")
    print(f"Shallow copy with list copy method: {ages_cp}")
    print(f"Deep copy: {ages_deep_copy}")

if __name__ == "__main__":
    main()
```

---

## 5. Expected Output

```text
Original list: [1, [2, 3, 4], 5]
Shallow copy with slicing: [1, [2, 3, 4], 5]
Shallow copy with list copy method: [1, [2, 3, 4], 5]
Deep copy: [1, [2, 3, 4], 5]
Original list: [100, [200, 3, 4], 5]
Shallow copy with slicing: [1, [200, 3, 4], 5]
Shallow copy with list copy method: [1, [200, 3, 4], 5]
Deep copy: [1, [2, 3, 4], 5]
```

---

## 6. Important Note

The script also creates:

```python
ages_list = list(ages)
```

This is another shallow copy.  
It is not printed in the original script, but you can add it to compare all methods.

---

## 7. Exercises

### 1. Level 1 — MCQ

Which copy type also copies nested mutable objects?

- a) Shallow copy
- b) Deep copy
- c) List slicing only
- d) `.copy()` only

<details>
<summary>Solution</summary>

**Answer:** b) Deep copy.
</details>

---

### 2. Level 2 — Coding

Print `ages_list` before and after the mutation.

<details>
<summary>Solution</summary>

```python
print(f"Shallow copy with list constructor: {ages_list}")
```
</details>

---

### 3. Level 3 — Challenge

Use `id()` to prove that shallow copies share the nested list.

<details>
<summary>Solution</summary>

```python
print(id(ages[1]))
print(id(ages_slice[1]))
print(id(ages_deep_copy[1]))
```
</details>

---

## 8. Further Reading

- [Python Docs: copy](https://docs.python.org/3/library/copy.html)
- [Python Docs: Lists](https://docs.python.org/3/tutorial/datastructures.html)

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
