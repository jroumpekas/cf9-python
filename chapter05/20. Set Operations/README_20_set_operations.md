# 🧮 Set Operations Demo

This lesson demonstrates the most common set operations in Python using a realistic store-products example.

The script compares the products available in Store A and Store B.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `20_set_operations.py` | Demonstrates intersection, union, difference, and symmetric difference. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Create Python sets.
- Find common items with intersection.
- Combine unique items with union.
- Find items that exist only in one set with difference.
- Find items that exist in either set but not both with symmetric difference.
- Use both operators and method syntax.

---

## 2. Prerequisites

- Sets.
- Basic collection operations.
- `print()`.
- Functions.

---

## 3. Key Concepts

### Intersection

Products that exist in both stores.

```python
common_products = store_a_products & store_b_products
```

or:

```python
common_products = store_a_products.intersection(store_b_products)
```

---

### Union

All unique products from both stores.

```python
all_products = store_a_products | store_b_products
```

or:

```python
all_products = store_a_products.union(store_b_products)
```

---

### Difference

Products that exist in one store but not the other.

```python
store_a_exclusive = store_a_products - store_b_products
```

or:

```python
store_a_exclusive = store_a_products.difference(store_b_products)
```

---

### Symmetric Difference

Products that exist in either store, but not in both.

```python
unique_to_either_store = store_a_products ^ store_b_products
```

or:

```python
unique_to_either_store = store_a_products.symmetric_difference(store_b_products)
```

---

## 4. Code Demo

```python
def main():
    store_a_products = {"Apples", "Bananas", "Cherries", "Dates", "Watermelons"}
    store_b_products = {"Bananas", "Cherries", "Figs", "Grapes", "Melons"}

    common_products = store_a_products & store_b_products
    print("Products available in both Store A and Store B:", common_products)

    all_products = store_a_products | store_b_products
    print("All unique products across Store A and Store B:", all_products)

    store_a_exclusive = store_a_products - store_b_products
    print("Products available only in Store A:", store_a_exclusive)

    store_b_exclusive = store_b_products - store_a_products
    print("Products available only in Store B:", store_b_exclusive)

    unique_to_either_store = store_a_products ^ store_b_products
    print("Products available in either Store A or Store B but not both:", unique_to_either_store)

if __name__ == "__main__":
    main()
```

---

## 5. Expected Output

Set order is not guaranteed, so the order of products may differ.

```text
Products available in both Store A and Store B: {'Bananas', 'Cherries'}
All unique products across Store A and Store B: {'Apples', 'Bananas', 'Cherries', 'Dates', 'Watermelons', 'Figs', 'Grapes', 'Melons'}
Products available only in Store A: {'Apples', 'Dates', 'Watermelons'}
Products available only in Store B: {'Figs', 'Grapes', 'Melons'}
Products available in either Store A or Store B but not both: {'Apples', 'Dates', 'Watermelons', 'Figs', 'Grapes', 'Melons'}
```

---

## 6. Operators vs Methods

| Operation | Operator | Method |
|----------|----------|--------|
| Intersection | `&` | `.intersection()` |
| Union | `|` | `.union()` |
| Difference | `-` | `.difference()` |
| Symmetric Difference | `^` | `.symmetric_difference()` |

Both styles are valid.

---

## 7. Exercises

### 1. Level 1 — MCQ

Which operator gives common items?

- a) `|`
- b) `&`
- c) `-`
- d) `^`

<details>
<summary>Solution</summary>

**Answer:** b) `&`.
</details>

---

### 2. Level 1 — Short Answer

Why can the printed order of a set change?

<details>
<summary>Solution</summary>

Because sets are unordered collections.
</details>

---

### 3. Level 2 — Coding

Find products that are not common between the two stores.

<details>
<summary>Solution</summary>

```python
not_common = store_a_products ^ store_b_products
print(not_common)
```
</details>

---

### 4. Level 3 — Challenge

Check whether all Store A products exist in Store B.

<details>
<summary>Solution</summary>

```python
all_a_in_b = store_a_products.issubset(store_b_products)
print(all_a_in_b)
```
</details>

---

## 8. Further Reading

- [Python Docs: Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Python Docs: Sets Tutorial](https://docs.python.org/3/tutorial/datastructures.html#sets)

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
