# 🌐 HTTP Status Messages with `match...case`

This lesson demonstrates how to use Python's structural pattern matching syntax, `match...case`, to map HTTP status codes to human-readable messages.

---

## 1. Learning Objectives

- Define a function that receives an HTTP status code.
- Use `match...case` to handle specific values.
- Return a default value for unknown cases.
- Understand how `case _` works as a fallback.
- Practice clean function documentation with a docstring.

---

## 2. Prerequisites

- Python 3.10 or newer.
- Basic understanding of functions.
- Basic familiarity with `return`.
- Awareness of common HTTP status codes such as `200`, `400`, and `404`.

---

## 3. Key Concepts

- **HTTP status code**: A number that describes the result of an HTTP request.
- **`match` statement**: Compares a value against several possible patterns.
- **`case` block**: Defines what should happen for a specific matched value.
- **`case _`**: Works like a default branch when no other case matches.
- **Docstring**: A string at the top of a function that explains what it does.

---

## 4. Lecture Outline

### 0:00–0:08 — Define the Function
- Create `get_http_error(error_code)`.

### 0:08–0:18 — Match Known Codes
- Match `200`, `400`, and `404` to their messages.

### 0:18–0:26 — Handle Unknown Codes
- Use `case _` to return `Unknown error`.

### 0:26–0:34 — Call the Function from `main()`
- Test the function with `error_code = 404`.

---

## 5. Code Demo

```python
def get_http_error(error_code):
    """
    Returns the HTTP error message corresponding to the given error code.
    
    Args:
    error_code (int): The HTTP error code.
    
    Returns:
    str: The corresponding error message.
    """
    result = ''
    match error_code:
        case 200:
            result = "OK"
        case 400:
            result = "Bad request"
        case 404:
            result = "Not found"
        case _:
            result = "Unknown error"
    return result

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()
```

**Expected output**:

```text
Not found
```

> 💡 **Why use `case _`?:** It catches every value that did not match any previous case. This prevents the function from returning an empty result for unknown codes.

> ⚠️ **Python version note:** `match...case` was introduced in Python 3.10. If you run this script with Python 3.9 or older, it will not work.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which case handles unknown HTTP codes?

<details>
<summary>Solution</summary>

`case _`.
</details>

---

### 2. (Level 1, Short Answer)
What does the function return for `404`?

<details>
<summary>Solution</summary>

It returns `"Not found"`.
</details>

---

### 3. (Level 2, Coding)
Add support for HTTP code `500` with the message `Internal server error`.

<details>
<summary>Solution</summary>

Add `case 500: result = "Internal server error"`.
</details>

---

### 4. (Level 2, Short Answer)
Why is it useful to have a fallback case?

<details>
<summary>Solution</summary>

Because the program can handle unexpected input safely instead of returning an empty string or crashing.
</details>

---

### 5. (Level 3, Coding)
Rewrite the function so it returns directly from each `case`.

<details>
<summary>Solution</summary>

Use `return "OK"`, `return "Bad request"`, etc. inside each case.
</details>

---

## 7. Further Reading

- [Python Docs: `match` statements](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
- [Python Docs: Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [MDN: HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

---

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a> (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
