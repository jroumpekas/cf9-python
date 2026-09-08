# ⏲️ Timing Functions with Decorators

This lesson demonstrates how to create and use a Python decorator that measures function execution time.

The script shows both manual decoration and the cleaner `@decorator` syntax.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `17_time_decorator.py` | Timer decorator applied to sum, average, and string-reversal functions. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Understand what a decorator is.
- Write a decorator function.
- Use an inner wrapper function.
- Pass `*args` and `**kwargs` through a wrapper.
- Measure function execution time.
- Decorate functions manually.
- Decorate functions with `@timer_decorator`.

---

## 2. Prerequisites

- Functions.
- Inner functions.
- `*args` and `**kwargs`.
- `time` module.
- Functions as objects.

---

## 3. Key Concepts

### Decorator

A decorator is a function that receives another function and returns a modified version of it.

```python
def timer_decorator(func):
    def inner_function(*args, **kwargs):
        ...
    return inner_function
```

---

### Wrapper Function

The wrapper function runs extra logic before and after the original function.

```python
start_time = time.time()
result = func(*args, **kwargs)
end_time = time.time()
```

---

### Manual Decoration

```python
sum_function = timer_decorator(sum_function)
```

---

### Decorator Syntax

```python
@timer_decorator
def average_function(n):
    ...
```

This is cleaner and more common.

---

## 4. Lecture Outline

### 0:00–0:10 — What is a Decorator?
- Explain that decorators wrap another function.

### 0:10–0:22 — Timer Decorator
- Build `timer_decorator()` and `inner_function()`.

### 0:22–0:34 — Manual Decoration
- Apply the decorator by reassignment.

### 0:34–0:48 — `@decorator` Syntax
- Apply the decorator to different functions.

---

## 5. Code Demo

```python
import time

def timer_decorator(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to run.")
        return result

    return inner_function

def sum_function(n):
    return sum(range(n))

sum_function = timer_decorator(sum_function)

@timer_decorator
def average_function(n):
    if n == 0:
        return 0

    total_sum = sum(range(n))
    return total_sum / n

@timer_decorator
def reverse_string(s):
    return "".join(reversed(s))
```

---

## 6. Example Output

The times will differ by machine.

```text
sum_function took 0.01234 seconds to run.
499999500000
average_function took 0.01256 seconds to run.
499999.5
reverse_string took 0.00001 seconds to run.
yrotcaF gnidoC
```

---

## 7. Important Note

The script contains function calls at the top level and also inside `main()`.

That means some output may appear before `main()` is called and then again when `main()` runs.

For cleaner structure, place demonstration calls inside `main()` only.

---

## 8. Suggested Cleaner Structure

```python
def main():
    print(sum_function(1_000_000))
    print(average_function(1_000_000))
    print(reverse_string("Coding Factory"))

if __name__ == "__main__":
    main()
```

---

## 9. Exercises

### 1. Level 1 — MCQ

What does a decorator do?

- a) Deletes a function
- b) Wraps or extends a function's behavior
- c) Converts a function to a string
- d) Imports a module

<details>
<summary>Solution</summary>

**Answer:** b) Wraps or extends a function's behavior.
</details>

---

### 2. Level 1 — Short Answer

Why do we use `*args` and `**kwargs` inside the wrapper?

<details>
<summary>Solution</summary>

So the decorator can work with functions that accept different kinds of arguments.
</details>

---

### 3. Level 2 — Coding

Create a decorator that prints `"Function started"` before running the function.

<details>
<summary>Solution</summary>

```python
def start_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)
    return wrapper
```
</details>

---

### 4. Level 3 — Challenge

Improve the decorator using `functools.wraps`.

<details>
<summary>Solution</summary>

```python
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time:.5f} seconds")
        return result

    return inner_function
```
</details>

---

## 10. Further Reading

- [Python Docs: Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Python Docs: functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)
- [Python Docs: time](https://docs.python.org/3/library/time.html)

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
