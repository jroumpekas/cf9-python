# 🔗 Combining `map()`, `filter()`, and `lambda`

This lesson demonstrates how to combine `filter()`, `map()`, and lambda functions.

The goal is to keep only city names longer than 5 characters and then capitalize them.

---

## 1. Learning Objectives

- Combine `filter()` and `map()`.
- Use lambda expressions for short transformations.
- Filter strings based on length.
- Capitalize filtered strings.
- Understand how chained iterators work.

---

## 2. Prerequisites

- Lists.
- Strings.
- Lambda functions.
- `map()` and `filter()`.

---

## 3. Key Concepts

- **`filter()`**: Keeps only values that satisfy a condition.
- **`map()`**: Transforms each value.
- **Chaining**: Passing the result of one function into another.
- **`len(city) > 5`**: Condition for long city names.
- **`.title()`**: Converts text to title case.

---

## 4. Lecture Outline

### 0:00–0:08 — City List
- Create a list of city names.

### 0:08–0:18 — Filter Long Names
- Keep cities with length greater than 5.

### 0:18–0:28 — Capitalize Results
- Use `map()` to apply `.title()`.

### 0:28–0:38 — All in One Expression
- Combine `map()` and `filter()` in one line.

---

## 5. Code Demo

Corrected version:

```python
cities = ["london", "paris", "barcelona", "athens", "Casablanka"]

long_cities = filter(lambda city: len(city) > 5, cities)

cap_length_cities = map(lambda city: city.title(), long_cities)

cap_long_cities = list(
    map(
        lambda city: city.title(),
        filter(lambda city: len(city) > 5, cities)
    )
)

print(*cap_long_cities)
```

---

## 6. Expected Output

```text
Barcelona Athens Casablanka
```

---

## 7. Known Issue in the Original Script

The original script uses:

```python
city.tittle()
```

This causes an error because the correct string method is:

```python
city.title()
```

The README uses the corrected version.

---

## 8. Exercises

### 1. Level 1 — MCQ
Which method correctly capitalizes a city name?

- a) `.tittle()`
- b) `.title()`
- c) `.upperCase()`
- d) `.capitalizeAll()`

<details>
<summary>Solution</summary>

**Answer:** b) `.title()`.
</details>

---

### 2. Level 1 — Short Answer
What does `filter(lambda city: len(city) > 5, cities)` do?

<details>
<summary>Solution</summary>

It keeps only the city names that have more than 5 characters.
</details>

---

### 3. Level 2 — Coding
Keep only cities with length less than or equal to 5 and capitalize them.

<details>
<summary>Solution</summary>

```python
short_cities = list(
    map(lambda city: city.title(), filter(lambda city: len(city) <= 5, cities))
)
print(short_cities)
```
</details>

---

### 4. Level 2 — Short Answer
Why does `print(*cap_long_cities)` print values separated by spaces?

<details>
<summary>Solution</summary>

Because `*` unpacks the list into separate arguments for `print()`.
</details>

---

## 9. Further Reading

- [Python Docs: map](https://docs.python.org/3/library/functions.html#map)
- [Python Docs: filter](https://docs.python.org/3/library/functions.html#filter)
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
