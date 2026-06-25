# 🗺️ Mapping City Names with `map()`

This lesson demonstrates how to use Python's built-in `map()` function with a lambda expression.

The example converts city names into title case.

---

## 1. Learning Objectives

- Use `map()` to transform items.
- Apply a lambda function to each list element.
- Use `.title()` to capitalize city names.
- Iterate over a map object.
- Understand the difference between transforming and filtering.

---

## 2. Prerequisites

- Lists.
- Strings.
- Lambda functions.
- Loops.

---

## 3. Key Concepts

- **`map(function, iterable)`**: Applies a function to every item.
- **Transformation**: Creating a changed version of each value.
- **`.title()`**: Converts a string to title case.
- **Map object**: An iterator returned by `map()`.

---

## 4. Lecture Outline

### 0:00–0:08 — City List
- Create a list of lowercase city names.

### 0:08–0:18 — Map with Lambda
- Apply `city.title()` to each city.

### 0:18–0:26 — Iterate Results
- Print each capitalized city.

### 0:26–0:34 — Convert to List
- Optionally use `list(map(...))`.

---

## 5. Code Demo

```python
cities = ["london", "paris", "athens", "barcelona"]

cap_cities = map(lambda city: city.title(), cities)

for cap_city in cap_cities:
    print(cap_city)
```

---

## 6. Expected Output

```text
London
Paris
Athens
Barcelona
```

---

## 7. Exercises

### 1. Level 1 — MCQ
What does `map()` do?

- a) Filters values
- b) Applies a function to every item
- c) Deletes values
- d) Sorts values only

<details>
<summary>Solution</summary>

**Answer:** b) Applies a function to every item.
</details>

---

### 2. Level 1 — Short Answer
What does `.title()` do?

<details>
<summary>Solution</summary>

It converts a string to title case, where the first letter of each word is capitalized.
</details>

---

### 3. Level 2 — Coding
Create a list with the lengths of all city names.

<details>
<summary>Solution</summary>

```python
lengths = list(map(lambda city: len(city), cities))
print(lengths)
```
</details>

---

### 4. Level 2 — Short Answer
What is the difference between `map()` and `filter()`?

<details>
<summary>Solution</summary>

`map()` transforms every item. `filter()` keeps only items that satisfy a condition.
</details>

---

## 8. Further Reading

- [Python Docs: map](https://docs.python.org/3/library/functions.html#map)
- [Python Docs: str.title](https://docs.python.org/3/library/stdtypes.html#str.title)
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
