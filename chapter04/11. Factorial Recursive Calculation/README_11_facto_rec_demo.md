# 🔁 Recursive Factorial Demo

This lesson demonstrates how to calculate a factorial using **recursion**.

A recursive function is a function that calls itself until it reaches a stopping condition.

---

## 1. Learning Objectives

- Understand the idea of recursion.
- Identify a base case.
- Identify a recursive case.
- Calculate factorial values.
- Read integer input from the user.
- Understand why negative factorials need special handling.

---

## 2. Prerequisites

- Functions.
- Integer arithmetic.
- `if` statements.
- User input with `input()`.

---

## 3. Key Concepts

- **Recursion**: A function calling itself.
- **Base case**: The condition that stops recursion.
- **Recursive case**: The part of the function that calls itself again.
- **Factorial**: `n! = n × (n - 1) × ... × 1`.
- **Stack calls**: Each recursive call waits for the next one to finish.

---

## 4. Lecture Outline

### 0:00–0:08 — What is Factorial?
- Explain `5! = 5 × 4 × 3 × 2 × 1`.

### 0:08–0:18 — Base Cases
- Return `1` for `0` and `1`.

### 0:18–0:28 — Recursive Case
- Return `n * factorial(n - 1)`.

### 0:28–0:36 — User Input
- Ask the user for an integer and print the result.

---

## 5. Code Demo

```python
def factorial(n: int) -> int:
    if n < 0:
        return 0
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

def main():
    n = int(input("Please insert an integer: "))
    print(f"{n}! = {factorial(n)}")

if __name__ == "__main__":
    main()
```

---

## 6. Example Output

Input:

```text
Please insert an integer: 5
```

Output:

```text
5! = 120
```

---

## 7. Important Note

Mathematically, factorial is not defined for negative integers.  
In this demo, the function returns `0` when `n < 0` as a simple way to handle invalid input.

A stricter version would be:

```python
if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
```

---

## 8. Exercises

### 1. Level 1 — MCQ
What is the base case in this factorial function?

- a) `n < 0`
- b) `n in (0, 1)`
- c) `n * factorial(n - 1)`
- d) `input()`

<details>
<summary>Solution</summary>

**Answer:** b) `n in (0, 1)`.
</details>

---

### 2. Level 1 — Short Answer
Why does recursion need a base case?

<details>
<summary>Solution</summary>

Without a base case, the function would keep calling itself forever until Python raises a recursion error.
</details>

---

### 3. Level 2 — Coding
Rewrite factorial using a `for` loop.

<details>
<summary>Solution</summary>

```python
def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers are not allowed")

    result = 1
    for number in range(1, n + 1):
        result *= number

    return result
```
</details>

---

### 4. Level 2 — Short Answer
What does `factorial(5)` return?

<details>
<summary>Solution</summary>

It returns `120`.
</details>

---

## 9. Further Reading

- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Docs: Recursion Limit](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit)
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
