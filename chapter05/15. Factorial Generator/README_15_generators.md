# 🔁 Infinite Generators: Factorial & Fibonacci

This lesson group contains two generator-based examples:

1. An infinite **factorial generator**
2. An infinite **Fibonacci generator**

Both examples use `yield` and `while True` to produce values one at a time.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `15_factorial_generator.py` | Infinite generator that yields factorial values: `0!`, `1!`, `2!`, ... |
| `15_fibo_gen.py` | Infinite generator that yields Fibonacci numbers: `0, 1, 1, 2, 3, 5, ...` |

---

## 1. Learning Objectives

By studying these examples, you will be able to:

- Create infinite generators with `while True`.
- Use `yield` to return values lazily.
- Generate factorial values step by step.
- Generate Fibonacci numbers step by step.
- Use `next()` to consume generator values.
- Understand that a generator remembers its internal state.
- Understand why generators are useful for sequences that can continue indefinitely.

---

## 2. Prerequisites

- Functions.
- Loops.
- `yield`.
- `next()`.
- Basic factorial logic.
- Basic Fibonacci logic.

---

## 3. Key Concepts

### Infinite Generator

An infinite generator can keep producing values forever.

```python
while True:
    yield value
```

It does not create all values at once. It produces the next value only when `next()` is called.

---

### Lazy Evaluation

Generators are lazy. This means they calculate values only when needed.

```python
f = facto()
print(next(f))
```

The next factorial is calculated only at the moment `next(f)` runs.

---

### Generator State

A generator remembers local variables between calls.

In the factorial generator:

```python
n, result = 0, 1
```

The values of `n` and `result` are preserved between `next()` calls.

In the Fibonacci generator:

```python
a, b = 0, 1
```

The pair `(a, b)` is updated after each yielded value.

---

## 4. Code Demo 1 — Factorial Generator

```python
def facto():
    n, result = 0, 1

    while True:
        yield result
        n += 1
        result *= n

def main():
    f = facto()

    for i in range(6):
        print(f"{i}! = {next(f)}")

    for i in range(6, 11):
        print(f"{i}! = {next(f)}")

if __name__ == "__main__":
    main()
```

---

## 5. Expected Output 1

```text
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
```

The second loop continues from where the first loop stopped because the generator keeps its state.

---

## 6. Code Demo 2 — Fibonacci Generator

```python
def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

def main():
    fib = fibonacci()

    for i in range(10):
        print(f"fibo({i}) = {next(fib)}")

if __name__ == "__main__":
    main()
```

---

## 7. Expected Output 2

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

## 8. Small Note

In the original Fibonacci script, the print statement is:

```python
print(f"fibo(i) = {next(fib)}")
```

This prints the literal text `fibo(i)`.  
A clearer version is:

```python
print(f"fibo({i}) = {next(fib)}")
```

---

## 9. Factorial vs Fibonacci

| Generator | State Variables | Output Pattern |
|----------|-----------------|----------------|
| Factorial | `n`, `result` | `1, 1, 2, 6, 24, ...` |
| Fibonacci | `a`, `b` | `0, 1, 1, 2, 3, 5, ...` |

Both generators are infinite, so we use `range()` to decide how many values to print.

---

## 10. Exercises

### 1. Level 1 — MCQ

What does `yield` do?

- a) Ends the program
- b) Returns a value and pauses the function
- c) Deletes a variable
- d) Imports a module

<details>
<summary>Solution</summary>

**Answer:** b) Returns a value and pauses the function.
</details>

---

### 2. Level 1 — Short Answer

Why do we use `range(10)` with an infinite generator?

<details>
<summary>Solution</summary>

Because the generator can produce values forever, so `range(10)` limits how many values we consume.
</details>

---

### 3. Level 2 — Coding

Print the first 15 Fibonacci numbers.

<details>
<summary>Solution</summary>

```python
fib = fibonacci()

for i in range(15):
    print(f"fibo({i}) = {next(fib)}")
```
</details>

---

### 4. Level 2 — Coding

Print factorials from `0!` to `15!`.

<details>
<summary>Solution</summary>

```python
f = facto()

for i in range(16):
    print(f"{i}! = {next(f)}")
```
</details>

---

### 5. Level 3 — Challenge

Create a generator that yields only even Fibonacci numbers.

<details>
<summary>Solution</summary>

```python
def even_fibonacci():
    a, b = 0, 1

    while True:
        if a % 2 == 0:
            yield a
        a, b = b, a + b
```
</details>

---

## 11. Further Reading

- [Python Docs: yield expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions)
- [Python Docs: Generator Types](https://docs.python.org/3/library/stdtypes.html#generator-types)
- [Python Docs: next](https://docs.python.org/3/library/functions.html#next)

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
