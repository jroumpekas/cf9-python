# 🌀 Recursive Fibonacci Demo

This lesson demonstrates a basic recursive implementation of the **Fibonacci sequence**.

The Fibonacci sequence starts with `0` and `1`. Each next number is the sum of the two previous numbers.

---

## 1. Learning Objectives

- Understand Fibonacci numbers.
- Write a recursive Fibonacci function.
- Identify base cases.
- Understand the recursive case `fibo(n - 1) + fibo(n - 2)`.
- Recognize that simple recursive Fibonacci can become slow for large values.

---

## 2. Prerequisites

- Functions.
- Recursion basics.
- Integer arithmetic.
- Conditional statements.

---

## 3. Key Concepts

- **Fibonacci sequence**: `0, 1, 1, 2, 3, 5, 8, 13, ...`
- **Base cases**: `fibo(0) = 0` and `fibo(1) = 1`.
- **Recursive case**: `fibo(n) = fibo(n - 1) + fibo(n - 2)`.
- **Exponential growth**: This simple recursive solution repeats many calculations.
- **Main function placeholder**: The demo defines the function, but `main()` currently contains `pass`.

---

## 4. Lecture Outline

### 0:00–0:08 — Fibonacci Sequence
- Explain the sequence pattern.

### 0:08–0:18 — Base Cases
- Return `n` when `n` is `0` or `1`.

### 0:18–0:30 — Recursive Case
- Add the two previous Fibonacci results.

### 0:30–0:38 — Testing the Function
- Add calls inside `main()` to test different values.

---

## 5. Code Demo

```python
def fibo(n: int) -> int:
    if n in (0, 1):
        return n
    return fibo(n - 1) + fibo(n - 2)

def main():
    pass

if __name__ == "__main__":
    main()
```

---

## 6. Suggested Test Version

Since `main()` currently contains only `pass`, you can test the function like this:

```python
def main():
    for i in range(10):
        print(f"fibo({i}) = {fibo(i)}")
```

Expected output:

```text
fibo(0) = 0
fibo(1) = 1
fibo(2) = 1
fibo(3) = 2
fibo(4) = 3
fibo(5) = 5
fibo(6) = 8
fibo(7) = 13
fibo(8) = 21
fibo(9) = 34
```

---

## 7. Important Note

This simple recursive version is good for learning, but it is not efficient for large numbers because it repeats many calculations.

Later improvements can use:

- iteration
- memoization
- dynamic programming
- `functools.lru_cache`

---

## 8. Exercises

### 1. Level 1 — MCQ
What is `fibo(0)`?

- a) 0
- b) 1
- c) 2
- d) undefined

<details>
<summary>Solution</summary>

**Answer:** a) 0.
</details>

---

### 2. Level 1 — Short Answer
What are the two base cases?

<details>
<summary>Solution</summary>

The base cases are `fibo(0) = 0` and `fibo(1) = 1`.
</details>

---

### 3. Level 2 — Coding
Add a `main()` function that prints the first 8 Fibonacci numbers.

<details>
<summary>Solution</summary>

```python
def main():
    for i in range(8):
        print(fibo(i))
```
</details>

---

### 4. Level 2 — Short Answer
Why is recursive Fibonacci slow for large `n`?

<details>
<summary>Solution</summary>

Because it recalculates the same Fibonacci values many times.
</details>

---

## 9. Further Reading

- [Python Docs: functools.cache](https://docs.python.org/3/library/functools.html#functools.cache)
- [Python Docs: Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
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
