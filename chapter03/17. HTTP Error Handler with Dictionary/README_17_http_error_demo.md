# 🧾 HTTP Error Lookup with a Dictionary

This lesson demonstrates a clean and compact way to map HTTP status codes to messages using a Python dictionary. Instead of using many conditional branches, the script stores known codes as dictionary keys and reads their messages with `.get()`.

---

## 1. Learning Objectives

- Create a dictionary with integer keys and string values.
- Use `.get()` to safely read values from a dictionary.
- Provide a default message when a key does not exist.
- Compare dictionary lookup with conditional branching.
- Keep code short and readable for simple mappings.

---

## 2. Prerequisites

- Basic understanding of dictionaries.
- Basic understanding of functions.
- Comfort with `return`.
- Awareness of common HTTP status codes.

---

## 3. Key Concepts

- **Dictionary**: Stores data as key-value pairs.
- **Key**: The HTTP status code, such as `200` or `404`.
- **Value**: The message associated with the code, such as `"OK"`.
- **`.get(key, default)`**: Returns the value for `key`, or the default value if the key is missing.
- **Mapping**: A clean way to connect one set of values to another set of values.

---

## 4. Lecture Outline

### 0:00–0:08 — Create the Dictionary
- Store status codes and messages in `error_messages`.

### 0:08–0:18 — Use `.get()`
- Retrieve the message for the requested status code.

### 0:18–0:26 — Add a Default Message
- Return `Unknown Error` if the code is not in the dictionary.

### 0:26–0:34 — Test from `main()`
- Call the function with `404` and print the result.

---

## 5. Code Demo

```python
def get_http_error(error_code):
    error_messages = {
        200: "OK",
        400: "Bad Request",
        404: "Not Found"
    }
    return error_messages.get(error_code, "Unknown Error")

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()
```

**Expected output**:

```text
Not Found
```

> 💡 **Why is this approach nice?:** When the goal is only to map known values to messages, a dictionary is often shorter and easier to expand than many `if`, `elif`, or `case` blocks.

> ⚠️ **Default value:** Without the second argument in `.get(error_code, "Unknown Error")`, Python would return `None` for unknown codes.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `.get(404, "Unknown Error")` return if `404` exists in the dictionary?

<details>
<summary>Solution</summary>

The value connected to key `404`.
</details>

---

### 2. (Level 1, Short Answer)
What does the function return for `500` in the current version?

<details>
<summary>Solution</summary>

It returns `"Unknown Error"`, because `500` is not currently a key in the dictionary.
</details>

---

### 3. (Level 2, Coding)
Add support for HTTP code `500`.

<details>
<summary>Solution</summary>

Add `500: "Internal Server Error"` to the dictionary.
</details>

---

### 4. (Level 2, Short Answer)
What is the main difference between `dict[key]` and `dict.get(key)`?

<details>
<summary>Solution</summary>

`dict[key]` raises `KeyError` if the key does not exist. `dict.get(key)` returns `None` or a custom default value.
</details>

---

### 5. (Level 3, Coding)
Make the dictionary global so it is not recreated every time the function is called.

<details>
<summary>Solution</summary>

Create `ERROR_MESSAGES = {...}` outside the function and return `ERROR_MESSAGES.get(error_code, "Unknown Error")`.
</details>

---

## 7. Further Reading

- [Python Docs: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Docs: `dict.get`](https://docs.python.org/3/library/stdtypes.html#dict.get)
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
