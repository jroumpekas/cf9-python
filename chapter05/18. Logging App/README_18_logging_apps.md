# 🪵 Logging Applications with Python's `logging` Module

This lesson group contains two logging examples.

The first script shows a simple logging setup that writes errors to a log file.  
The second script improves the structure with a reusable logger configuration, file and console handlers, typed functions, and better search logic.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `18_logging_app.py` | Basic logging example using `logging.basicConfig()` and `FileHandler`. |
| `18_logging_extra.py` | Improved logging app with reusable `configure_logger()` and `search_item()` functions. |

---

## 1. Learning Objectives

By studying these examples, you will be able to:

- Import and use Python's `logging` module.
- Configure logging to a file.
- Create a logger with `logging.getLogger()`.
- Use `FileHandler` and `StreamHandler`.
- Format log messages.
- Log errors with `exc_info=True`.
- Search for an item in a list and log the result.
- Raise and re-raise exceptions after logging.
- Understand common logging levels.

---

## 2. Prerequisites

- Functions.
- Lists.
- Exceptions.
- `try / except`.
- Basic file handling concepts.
- Type annotations.

---

## 3. Key Concepts

### Logger

A logger is an object used to record messages from an application.

```python
logger = logging.getLogger("search-app")
```

---

### Logging Levels

Common logging levels are:

| Level | Meaning |
|-------|---------|
| `DEBUG` | Detailed diagnostic information |
| `INFO` | Normal application information |
| `WARNING` | Something unexpected but not fatal |
| `ERROR` | Something failed |
| `CRITICAL` | Serious failure |

---

### File Handler

A file handler writes logs to a file.

```python
file_handler = logging.FileHandler(log_file, mode="a")
```

The mode `"a"` means append.

---

### Console Handler

A console handler prints log messages to the terminal.

```python
console_handler = logging.StreamHandler()
```

---

### `exc_info=True`

This includes the traceback in the log entry.

```python
logger.error("Error occurred", exc_info=True)
```

This is very useful for debugging.

---

## 4. Code Demo 1 — Basic Logging App

```python
import logging

def main():
    log_file = "cf9.log"

    file_handler = logging.FileHandler(log_file, mode="a")
    handlers = [file_handler]

    logger = logging.getLogger("search-app")

    logging.basicConfig(
        handlers=handlers,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    )

    nums = [10, 20, 30, 40, 50]
    num_to_find = 120

    try:
        index = nums.index(num_to_find)
        print(f"Found at index: {index}")
    except ValueError as e:
        logger.error(f"Error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
```

---

## 5. Code Demo 2 — Improved Logging App

```python
import logging
from typing import List, Any

def configure_logger(log_file: str, logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def search_item(items: List[Any], item_to_find: Any, logger: logging.Logger) -> int:
    if not items:
        logger.warning("The list is empty.")
        raise ValueError("Cannot search in an empty list.")

    try:
        index = items.index(item_to_find)
        logger.info(f"Item '{item_to_find}' found at index {index}.")
        return index
    except ValueError as e:
        logger.error(f"Item '{item_to_find}' not found in the list. Error: {e}", exc_info=True)
        raise
```

---

## 6. Expected Behaviour

If the item is found:

```text
Employee 'Alice' found at index 0.
```

If the item is not found:

```text
Employee 'Frank' was not found in the list.
```

The log file will also contain an error entry with traceback information.

---

## 7. Basic vs Improved Version

| Feature | Basic Version | Improved Version |
|---------|---------------|------------------|
| File logging | Yes | Yes |
| Console logging | No | Yes |
| Reusable logger config | No | Yes |
| Search logic in function | No | Yes |
| Type annotations | Minimal | Yes |
| Re-raises errors | No | Yes |

---

## 8. Small Notes

### Log File Name

The basic version uses:

```python
cf9.log
```

The improved version uses:

```python
cf6.log
```

You may want to rename it to `cf9.log` for consistency.

---

### Avoid Duplicate Handlers

If `configure_logger()` is called multiple times with the same logger name, handlers can be added repeatedly.

A safer version is:

```python
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
```

---

## 9. Exercises

### 1. Level 1 — MCQ

Which method logs an error?

- a) `logger.info()`
- b) `logger.warning()`
- c) `logger.error()`
- d) `logger.print()`

<details>
<summary>Solution</summary>

**Answer:** c) `logger.error()`.
</details>

---

### 2. Level 1 — Short Answer

What does `exc_info=True` add?

<details>
<summary>Solution</summary>

It adds traceback information to the log, making debugging easier.
</details>

---

### 3. Level 2 — Coding

Change the logger level to `DEBUG`.

<details>
<summary>Solution</summary>

```python
logger.setLevel(logging.DEBUG)
```
</details>

---

### 4. Level 3 — Challenge

Add a function that logs successful searches and failed searches to different files.

<details>
<summary>Solution</summary>

Create two file handlers, one for normal logs and one for errors, and assign different levels to them.
</details>

---

## 10. Further Reading

- [Python Docs: logging](https://docs.python.org/3/library/logging.html)
- [Python Docs: logging handlers](https://docs.python.org/3/library/logging.handlers.html)

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
