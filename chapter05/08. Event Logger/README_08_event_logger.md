# 📝 Event Logger with `datetime` and `**kwargs`

This lesson demonstrates a simple event logger in Python.

The script logs different event types, automatically adds a timestamp, and accepts flexible event details using `**kwargs`.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `08_event_logger.py` | Logs events with event type, timestamp, and extra keyword-based metadata. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Import and use `datetime`.
- Generate timestamps with `datetime.now().isoformat()`.
- Use `**kwargs` to accept flexible event data.
- Loop through dictionary key-value pairs.
- Build a reusable logging-style function.
- Understand how structured event output works.

---

## 2. Prerequisites

- Functions.
- Dictionaries.
- `**kwargs`.
- Loops.
- Basic imports.

---

## 3. Key Concepts

### `datetime.now()`

The `datetime.now()` method returns the current local date and time.

```python
timestamp = datetime.now()
```

---

### `.isoformat()`

The `.isoformat()` method converts a datetime object into a clean string format.

Example:

```text
2026-06-30T14:25:18.123456
```

---

### `**kwargs`

The `**kwargs` parameter collects extra keyword arguments into a dictionary.

```python
def log_event(event_type: str, **kwargs) -> None:
    ...
```

This allows the function to accept different event details each time.

---

## 4. Lecture Outline

### 0:00–0:08 — Importing `datetime`
- Import `datetime` from the standard library.

### 0:08–0:18 — Logger Function
- Define `log_event(event_type, **kwargs)`.

### 0:18–0:30 — Event Metadata
- Print each key-value pair from `kwargs`.

### 0:30–0:40 — Multiple Events
- Log different event types with different extra fields.

---

## 5. Code Demo

```python
from datetime import datetime

def log_event(event_type: str, **kwargs) -> None:
    timestamp = datetime.now().isoformat()
    print(f"Event type: {event_type}")
    print(f"Timestamp: {timestamp}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print("-" * 41)

def main():
    log_event("UserLogin", user="JohnDoe", status="Success", ip="192.168.1.1")
    log_event(
        "FileUploaded",
        user="JaneDoe",
        status="Failure",
        filename="report.pdf",
        reason="File too large"
    )

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output

The timestamp will be different each time the script runs.

```text
Event type: UserLogin
Timestamp: 2026-06-30T14:25:18.123456
user: JohnDoe
status: Success
ip: 192.168.1.1
-----------------------------------------
Event type: FileUploaded
Timestamp: 2026-06-30T14:25:18.123789
user: JaneDoe
status: Failure
filename: report.pdf
reason: File too large
-----------------------------------------
```

---

## 7. Why `**kwargs` Is Useful Here

Different event types can have different extra information.

For example:

```python
log_event("UserLogin", user="JohnDoe", ip="192.168.1.1")
```

and:

```python
log_event("FileUploaded", filename="report.pdf", reason="File too large")
```

The same function can handle both cases.

---

## 8. Exercises

### 1. Level 1 — MCQ

What does `**kwargs` collect?

- a) Positional arguments
- b) Keyword arguments
- c) Only strings
- d) Only timestamps

<details>
<summary>Solution</summary>

**Answer:** b) Keyword arguments.
</details>

---

### 2. Level 1 — Short Answer

Why does the timestamp change every time?

<details>
<summary>Solution</summary>

Because `datetime.now()` gets the current date and time at the moment the function is called.
</details>

---

### 3. Level 2 — Coding

Add a third event called `"PasswordChanged"`.

<details>
<summary>Solution</summary>

```python
log_event("PasswordChanged", user="JohnDoe", status="Success")
```
</details>

---

### 4. Level 3 — Challenge

Modify `log_event()` so it also writes the event to a text file.

<details>
<summary>Solution</summary>

```python
def log_event(event_type: str, **kwargs) -> None:
    timestamp = datetime.now().isoformat()

    with open("events.log", "a", encoding="utf-8") as file:
        file.write(f"Event type: {event_type}\n")
        file.write(f"Timestamp: {timestamp}\n")

        for key, value in kwargs.items():
            file.write(f"{key}: {value}\n")

        file.write("-" * 41 + "\n")
```
</details>

---

## 9. Further Reading

- [Python Docs: datetime](https://docs.python.org/3/library/datetime.html)
- [Python Docs: Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)

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
