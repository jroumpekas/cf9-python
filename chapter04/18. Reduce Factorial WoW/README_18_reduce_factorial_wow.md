# 🚀 Reduce Factorial Step-by-Step

This lesson expands the factorial example with `reduce()` by showing intermediate multiplication steps.

It demonstrates three versions:

1. A simple `reduce()` factorial.
2. A helper function that prints each multiplication.
3. A lambda expression that prints and returns the multiplication result.

---

## 1. Learning Objectives

- Use `reduce()` for rolling multiplication.
- Calculate factorial from `1` to `n`.
- Print intermediate results.
- Understand how a helper function improves readability.
- Understand how `print(...) or x * y` works inside a lambda.

---

## 2. Prerequisites

- Factorial logic.
- Lambda functions.
- Functions.
- `range()`.
- `functools.reduce`.

---

## 3. Key Concepts

- **Rolling result**: Each step receives the previous result.
- **Helper function**: A named function used by `reduce()`.
- **Side effect**: Printing inside a calculation.
- **`or` trick**: `print()` returns `None`, so `print(...) or x * y` returns `x * y`.
- **Final result**: The last accumulated value from reduce.

---

## 4. Lecture Outline

### 0:00–0:08 — Input
- Ask the user for an integer.

### 0:08–0:18 — Simple Reduce Factorial
- Calculate the factorial using `lambda x, y: x * y`.

### 0:18–0:30 — Helper Function Version
- Print every multiplication step.

### 0:30–0:42 — Lambda with Print
- Use a compact lambda that prints and returns the result.

---

## 5. Code Demo

```python
from functools import reduce

n = int(input("Give an int to calc facto: "))

result = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"{n}! = {result}")

def print_and_multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

result = reduce(print_and_multiply, range(1, n + 1))
print(f"Final result: {result}")

result = reduce(
    lambda x, y: print(f"{x} * {y} = {x * y}") or x * y,
    range(1, n + 1)
)
print(f"Final result: {result}")
```

---

## 6. Example Output

Input:

```text
Give an int to calc facto: 5
```

Output:

```text
5! = 120
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
24 * 5 = 120
Final result: 120
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
24 * 5 = 120
Final result: 120
```

---

## 7. Explanation of the Lambda Print Trick

```python
lambda x, y: print(f"{x} * {y} = {x * y}") or x * y
```

This works because `print()` returns `None`.

So Python evaluates:

```python
None or x * y
```

and returns `x * y`.

---

## 8. Exercises

### 1. Level 1 — MCQ
What does `print()` return?

- a) `True`
- b) `False`
- c) `None`
- d) The printed string

<details>
<summary>Solution</summary>

**Answer:** c) `None`.
</details>

---

### 2. Level 1 — Short Answer
What is the final result of factorial 5?

<details>
<summary>Solution</summary>

`5! = 120`.
</details>

---

### 3. Level 2 — Coding
Create a helper function for addition instead of multiplication.

<details>
<summary>Solution</summary>

```python
from functools import reduce

def print_and_add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")
    return result

result = reduce(print_and_add, range(1, 6))
print(result)
```
</details>

---

### 4. Level 2 — Short Answer
Why is the helper function version more readable?

<details>
<summary>Solution</summary>

Because it separates the printing and multiplication logic into clear steps with a descriptive function name.
</details>

---

## 9. Further Reading

- [Python Docs: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)
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
