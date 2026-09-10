# ⚡ Fibonacci with `functools.lru_cache`

This lesson shows how Python’s built-in `@lru_cache` can replace a custom memoization decorator for recursive Fibonacci.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `22_lru_func_demo.py` | Uses Python’s built-in `lru_cache` decorator to cache Fibonacci results. |

---

## 1. Learning Objectives

- Import `lru_cache` from `functools`.
- Cache recursive function calls automatically.
- Use `cache_clear()` to reset cache data.
- Understand `maxsize=None`.
- Compare custom memoization with built-in caching.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **`lru_cache`**: A built-in caching decorator.
- **`maxsize=None`**: Allows the cache to grow without a fixed limit.
- **`cache_clear()`**: Removes stored cached values.
- **Recursive optimization**: Avoids repeating Fibonacci subproblems.

---

## 4. Code Demo

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

fibonacci_cached.cache_clear()
print([fibonacci_cached(n) for n in range(10)])
```

---

## 5. Expected Output / Behaviour

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```


---

## 6. Exercises

### 1. Level 2 — Coding
Print cache information after the calculation.

<details><summary>Solution</summary>

```python
print(fibonacci_cached.cache_info())
```
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
