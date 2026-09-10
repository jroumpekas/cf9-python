# 🎛️ Multiple Decorators Demo

This lesson demonstrates decorator stacking and shows how one function can be wrapped by multiple decorators.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `23_multiple_decorators.py` | Applies a logging decorator and a timing decorator to the same function. |

---

## 1. Learning Objectives

- Create a call-logging decorator.
- Create a timing decorator.
- Apply multiple decorators to one function.
- Understand bottom-to-top decoration order.
- Use `*args` and `**kwargs` in wrappers.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Decorator stacking**: Multiple decorators can wrap the same function.
- **Call logging**: Prints function name and arguments.
- **Timing**: Measures execution time with `time.perf_counter()`.
- **Execution order**: Decorators are applied bottom-to-top and wrappers execute outside-in.

---

## 4. Code Demo

```python
import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def say_hello(name):
    time.sleep(1)
    return f"Hello, {name}!"
```

---

## 5. Expected Output / Behaviour

```text
Calling function 'say_hello' with arguments ('Alice',) and keyword arguments {}
Hello, Alice!
```

The original file also measures execution time using a second decorator.

---

## 6. Exercises

### 1. Level 2 — Coding
Improve the decorators with `functools.wraps`.

<details><summary>Solution</summary>

```python
from functools import wraps

@wraps(func)
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
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
