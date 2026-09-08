# ⏱️ Measuring Function Execution Time with `time.perf_counter()`

This lesson demonstrates how to measure how long a calculation takes in Python.

The script calculates the sum of the first `n` natural numbers and prints the execution time.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `16_timing_func.py` | Measures the execution time of `sum(range(n))` using `time.perf_counter()`. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Import and use Python's `time` module.
- Use `time.perf_counter()` for high-resolution timing.
- Measure the execution time of a calculation.
- Return a function result after timing it.
- Understand the difference between measuring and calculating.

---

## 2. Prerequisites

- Functions.
- Imports.
- `sum()`.
- `range()`.
- Basic f-string formatting.

---

## 3. Key Concepts

### `time.perf_counter()`

`time.perf_counter()` gives a high-resolution timer.

It is useful for measuring short durations:

```python
start_time = time.perf_counter()
...
end_time = time.perf_counter()
```

---

### Execution Time

Execution time is calculated by subtracting the start time from the end time:

```python
end_time - start_time
```

---

### Timed Calculation

The script measures this calculation:

```python
result = sum(range(n))
```

This calculates:

```text
0 + 1 + 2 + ... + (n - 1)
```

---

## 4. Lecture Outline

### 0:00–0:08 — Importing `time`
- Import the time module.

### 0:08–0:18 — Start Timer
- Record `start_time`.

### 0:18–0:28 — Run Calculation
- Calculate the sum of a range.

### 0:28–0:38 — End Timer and Print Duration
- Record `end_time` and print the difference.

---

## 5. Code Demo

```python
import time

def get_time(n):
    start_time = time.perf_counter()

    result = sum(range(n))

    end_time = time.perf_counter()

    print(f"My function took {end_time - start_time:.5f} seconds to run")

    return result

def main():
    print(get_time(10000000))

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output

The execution time depends on your computer.

```text
My function took 0.12345 seconds to run
49999995000000
```

---

## 7. Why `perf_counter()` Is Used

`perf_counter()` is preferred for timing code because it provides a precise clock for measuring elapsed time.

It is better for benchmarking than using normal date/time values.

---

## 8. Exercises

### 1. Level 1 — MCQ

What does `time.perf_counter()` help us measure?

- a) The current date
- b) The elapsed time of code execution
- c) The size of a list
- d) The Python version

<details>
<summary>Solution</summary>

**Answer:** b) The elapsed time of code execution.
</details>

---

### 2. Level 2 — Coding

Measure the time needed to create a list of one million numbers.

<details>
<summary>Solution</summary>

```python
start = time.perf_counter()
numbers = list(range(1_000_000))
end = time.perf_counter()

print(f"List creation took {end - start:.5f} seconds")
```
</details>

---

### 3. Level 3 — Challenge

Create a reusable timing function that accepts another function as an argument.

<details>
<summary>Solution</summary>

```python
def time_function(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    print(f"{func.__name__} took {end - start:.5f} seconds")
    return result
```
</details>

---

## 9. Further Reading

- [Python Docs: time](https://docs.python.org/3/library/time.html)
- [Python Docs: time.perf_counter](https://docs.python.org/3/library/time.html#time.perf_counter)

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
