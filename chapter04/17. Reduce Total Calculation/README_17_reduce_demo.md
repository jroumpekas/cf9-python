# 🧱 Factorial with `reduce()`

This lesson demonstrates how to use `functools.reduce()` to calculate factorials.

The `reduce()` function applies a rolling calculation to pairs of values until one final result remains.

---

## 1. Learning Objectives

- Import and use `reduce()` from `functools`.
- Calculate a factorial using multiplication.
- Understand how reduce combines values step by step.
- Use a helper function with reduce.
- Print intermediate multiplication steps.

---

## 2. Prerequisites

- Functions.
- Lambda functions.
- Ranges.
- Factorial logic.
- Basic imports.

---

## 3. Key Concepts

- **`reduce(function, iterable)`**: Combines values into one final result.
- **Rolling calculation**: The result of one step becomes the input to the next step.
- **Lambda function**: Used for short multiplication logic.
- **Helper function**: A named function can make reduce easier to understand.
- **Factorial**: Product of all integers from `1` to `n`.

---

## 4. Lecture Outline

### 0:00–0:08 — Import Reduce
- Import `reduce` from `functools`.

### 0:08–0:18 — Factorial with Lambda
- Multiply numbers from `1` to `num`.

### 0:18–0:30 — Step-by-Step Helper
- Use `print_and_multiply()` to show intermediate results.

### 0:30–0:40 — Reduce with Inline Print
- Use `print(...) or x * y` inside a lambda.

---

## 5. Code Demo

```python
from functools import reduce

num = int(input("Give me an int to calculate the factorial: "))

result = reduce(lambda x, y: x * y, range(1, num + 1))
print(f"{num}! = {result}")

def print_and_multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

new_result = reduce(print_and_multiply, range(1, 6))
print(f"Final result: {new_result}")
```

---

## 6. Example Output

Input:

```text
Give me an int to calculate the factorial: 5
```

Output:

```text
5! = 120
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
24 * 5 = 120
Final result: 120
```

---

## 7. Important Note

For readability, a normal loop is often easier for beginners than `reduce()`.

Example:

```python
result = 1
for number in range(1, num + 1):
    result *= number
```

---

## 8. Exercises

### 1. Level 1 — MCQ
Where does `reduce()` come from?

- a) `math`
- b) `random`
- c) `functools`
- d) `string`

<details>
<summary>Solution</summary>

**Answer:** c) `functools`.
</details>

---

### 2. Level 1 — Short Answer
What does `reduce(lambda x, y: x * y, range(1, 6))` calculate?

<details>
<summary>Solution</summary>

It calculates `1 * 2 * 3 * 4 * 5`, which is `120`.
</details>

---

### 3. Level 2 — Coding
Use `reduce()` to calculate the sum of numbers from 1 to 5.

<details>
<summary>Solution</summary>

```python
from functools import reduce

result = reduce(lambda x, y: x + y, range(1, 6))
print(result)
```
</details>

---

### 4. Level 2 — Short Answer
Why is `print_and_multiply()` easier to understand than a long lambda?

<details>
<summary>Solution</summary>

Because it gives names to the logic and allows multiple statements, such as printing and returning a value.
</details>

---

## 9. Further Reading

- [Python Docs: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)
- [Python Docs: range](https://docs.python.org/3/library/stdtypes.html#range)
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
