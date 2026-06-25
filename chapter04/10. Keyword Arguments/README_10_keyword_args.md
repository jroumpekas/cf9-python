# 🔑 Keyword Arguments & Dictionary Unpacking

This lesson demonstrates how to use **keyword arguments** with `**kwargs` and how to unpack a dictionary into function arguments.

The example filters a list of product tuples based on search criteria such as brand and price.

---

## 1. Learning Objectives

- Understand how `**kwargs` collects keyword arguments.
- Use dictionary unpacking with `**criteria`.
- Filter a list using a list comprehension.
- Work with tuples inside a list.
- Use `.get()` to safely read dictionary values.

---

## 2. Prerequisites

- Lists and tuples.
- Dictionaries.
- Functions.
- Basic type annotations.
- List comprehensions.

---

## 3. Key Concepts

- **`**kwargs`**: Collects keyword arguments into a dictionary.
- **Dictionary unpacking**: `**criteria` passes dictionary keys as keyword argument names.
- **List comprehension**: A compact way to build a new list.
- **Tuple unpacking**: `for brand, price in products` extracts each tuple into two variables.
- **`.get()`**: Reads a dictionary value without raising an error if the key is missing.

---

## 4. Lecture Outline

### 0:00–0:08 — Product Data
- Create a list of product tuples.

### 0:08–0:18 — Search Criteria
- Store filters inside a dictionary.

### 0:18–0:28 — Dictionary Unpacking
- Call the function with `get_results(products, **criteria)`.

### 0:28–0:38 — Filtering with List Comprehension
- Return only products matching both brand and price.

---

## 5. Code Demo

```python
from typing import List, Tuple, Dict, Optional

def get_results(
    products: List[Tuple[str, int]],
    **kwargs: Optional[Dict[str, str | int]]
) -> List[Tuple[str, int]]:
    results = [
        (brand, price)
        for brand, price in products
        if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    return results

def main():
    products = [("lenovo", 100), ("lenovo", 40), ("ibm", 100)]
    criteria = {"brand": "lenovo", "price": 100}

    print(get_results(products, **criteria))

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output

```text
[('lenovo', 100)]
```

---

## 7. Exercises

### 1. Level 1 — MCQ
What does `**criteria` do?

- a) Converts a list to a tuple
- b) Unpacks a dictionary into keyword arguments
- c) Multiplies numbers
- d) Deletes dictionary keys

<details>
<summary>Solution</summary>

**Answer:** b) Unpacks a dictionary into keyword arguments.
</details>

---

### 2. Level 1 — Short Answer
Why does the function return only `[('lenovo', 100)]`?

<details>
<summary>Solution</summary>

Because it filters products where both `brand` equals `"lenovo"` and `price` equals `100`.
</details>

---

### 3. Level 2 — Coding
Modify the function so that it can filter only by brand if price is not provided.

<details>
<summary>Solution</summary>

```python
def get_results(products, **kwargs):
    return [
        (brand, price)
        for brand, price in products
        if kwargs.get("brand", brand) == brand
        and kwargs.get("price", price) == price
    ]
```
</details>

---

### 4. Level 2 — Short Answer
What is the benefit of using `.get()` instead of direct indexing?

<details>
<summary>Solution</summary>

`.get()` returns `None` or a default value if the key does not exist, while direct indexing raises `KeyError`.
</details>

---

## 8. Further Reading

- [Python Docs: Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
- [Python Docs: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
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
