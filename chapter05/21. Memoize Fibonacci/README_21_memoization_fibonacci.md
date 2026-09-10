# 🧠 Fibonacci Memoization Decorator

This lesson group demonstrates how memoization improves recursive Fibonacci calculations by caching results that were already computed.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `21_memoize_fibonacci.py` | Basic memoization decorator for recursive Fibonacci. |
| `21_memo_improvement.py` | Improved memoization decorator with hit/miss cache statistics. |

---

## 1. Learning Objectives

- Create a custom memoization decorator.
- Use a dictionary as a cache.
- Apply a decorator to recursive Fibonacci.
- Track cache hits and misses.
- Attach helper functions to a wrapper function.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Memoization**: Stores previous function results and reuses them.
- **Decorator**: Wraps another function with extra behaviour.
- **Cache**: A dictionary that stores Fibonacci values by input number.
- **Cache statistics**: Counts how many calls were served from cache and how many were calculated.

---

## 4. Code Demo

```python
def memoize(func):
    cache = {}
    cache_stats = {"hits": 0, "misses": 0}

    def wrapper(n):
        if n in cache:
            cache_stats["hits"] += 1
            print(f"Cache hit for Fibonacci({n})")
        else:
            cache_stats["misses"] += 1
            print(f"Calculating Fibonacci({n})")
            cache[n] = func(n)
        return cache[n]

    def get_cache_stats():
        return cache_stats

    wrapper.get_cache_stats = get_cache_stats
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## 5. Expected Output / Behaviour

```text
Calculating Fibonacci(0)
Calculating Fibonacci(1)
Cache hit for Fibonacci(...)
Cache Statistics: Hits - ..., Misses - ...
```

The exact cache statistics depend on how many Fibonacci values are requested.

---

## 6. Exercises

### 1. Level 1 — MCQ
What does memoization store?

- a) Previously calculated results
- b) Only user input
- c) Python files
- d) Error messages

<details><summary>Solution</summary>

**Answer:** a) Previously calculated results.
</details>

---

## 7. Further Reading

- [Python Docs: Tutorial](https://docs.python.org/3/tutorial/)
- [Python Docs: Standard Library](https://docs.python.org/3/library/)

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
