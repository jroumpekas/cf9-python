# 🧩 List Comprehension, `map()`, and `filter()` Demo

This lesson compares list comprehensions with functional tools such as `map()` and `filter()`. The script squares numbers in different ways and then squares only the even numbers.

---

## 1. Learning Objectives

- Use list comprehension to transform values.
- Use `map()` with lambda and named functions.
- Use `filter()` to keep only selected values.
- Compare readable and functional-style approaches.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, loops, and simple terminal execution.

---

## 3. Key Concepts

- **List comprehension**: Creates a new list in a compact syntax.
- **`map()`**: Applies a function to every item.
- **`filter()`**: Keeps items that match a condition.
- **Lambda**: A short anonymous function.

---

## 4. Lecture Outline

### 0:00–0:08 — Introduce the Example
- Read the input data and identify the goal of the script.

### 0:08–0:20 — Main Logic
- Walk through the important Python concepts used in the code.

### 0:20–0:32 — Output and Behaviour
- Run the script and explain the result.

### 0:32–0:40 — Improvements
- Discuss small fixes, cleaner structure, or extra validation.

---

## 5. Code Demo

```python
list_of_ints = [1, 2, 3, 4, 5, 6, 7]

squared_list_compr = [number ** 2 for number in list_of_ints]
print(f"Squared Numbers: {squared_list_compr}")

def square_function(num):
    return num ** 2

squared_nums_lambda = list(map(lambda number: number ** 2, list_of_ints))
print(f"Squared numbers with map(): {squared_nums_lambda}")

squared_nums_func = list(map(square_function, list_of_ints))
print(f"Squared number from square_function: {squared_nums_func}")

squared_filtered_nums = [number ** 2 for number in list_of_ints if number % 2 == 0]
print(f"Squared using list compr and if: {squared_filtered_nums}")

filtered_mapped_squared = list(map(square_function, filter(lambda x: x % 2 == 0, list_of_ints)))
print(f"Squared nums using filter and map functions: {filtered_mapped_squared}")
```

---

## 6. Expected Output

```text
Squared Numbers: [1, 4, 9, 16, 25, 36, 49]
Squared numbers with map(): [1, 4, 9, 16, 25, 36, 49]
Squared number from square_function: [1, 4, 9, 16, 25, 36, 49]
Squared using list compr and if: [4, 16, 36]
Squared nums using filter and map functions: [4, 16, 36]
```


---

## 7. Exercises

### 1. Level 1 — MCQ
Which expression keeps only even numbers?

- a) `number % 2 == 0`
- b) `number % 2 == 1`
- c) `number ** 2`
- d) `number + 2`

<details>
<summary>Solution</summary>

**Answer:** a) `number % 2 == 0`
</details>

---

### 2. Level 2 — Coding
Create a list with the cubes of only odd numbers.

<details>
<summary>Solution</summary>

```python
odd_cubes = [number ** 3 for number in list_of_ints if number % 2 != 0]
print(odd_cubes)
```
</details>

---

## 8. Further Reading

- [Python Docs: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python Docs: map](https://docs.python.org/3/library/functions.html#map)
- [Python Docs: filter](https://docs.python.org/3/library/functions.html#filter)

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
