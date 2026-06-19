# 🔐 Simple Message Decryption by Removing Digits

This lesson demonstrates a simple “decryption” technique: given a mixed string containing letters, spaces, and numbers, the program removes all numeric characters and returns the readable message.

---

## 1. Learning Objectives

- Iterate over a string character by character.
- Use `.isnumeric()` to identify numeric characters.
- Build a new string using an accumulator variable.
- Return a value from a function.
- Understand the difference between printing a result and returning a result.
- Recognize unreachable code after `return`.

---

## 2. Prerequisites

- Basic understanding of functions.
- Basic string operations.
- Comfort with `for` loops.
- Basic familiarity with `if` conditions.

---

## 3. Key Concepts

- **String iteration**: A `for` loop can process each character in a string.
- **`.isnumeric()`**: Returns `True` when a character is numeric.
- **Accumulator pattern**: Start with an empty string and add valid characters one by one.
- **Function return**: `return decrypted_message` sends the final result back to the caller.
- **Unreachable code**: Any statement after `return` inside the same block will never execute.

---

## 4. Lecture Outline

### 0:00–0:08 — Define the Function
- Create `decrypt_message(message: str) -> str`.

### 0:08–0:18 — Loop Through the Message
- Visit every character in the encrypted text.

### 0:18–0:28 — Filter Out Numbers
- Keep only characters where `not char.isnumeric()` is `True`.

### 0:28–0:35 — Return and Print the Result
- Return the cleaned message and print it from `main()`.

---

## 5. Code Demo

```python
def decrypt_message(message: str) -> str:
    decrypted_message = ""

    for char in message:
        if not char.isnumeric():
            decrypted_message += char

    return decrypted_message


def main():
    strange_message = "432H3525el523l52o5 523C532F52"
    print(decrypt_message(strange_message))


if __name__ == "__main__":
    main()
```

**Expected output**:

```text
Hello CF
```

> 💡 **Why use `not char.isnumeric()`?:** Because we want to keep letters and spaces, while ignoring digits like `4`, `3`, `2`, and `5`.

> ⚠️ **Small improvement:** Start with `decrypted_message = ""`, not `" "`, otherwise the result begins with an extra leading space.

> ⚠️ **Unreachable code:** A `pass` statement after `return` is unnecessary, because Python exits the function as soon as it reaches `return`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `char.isnumeric()` return for `'A'`?

<details>
<summary>Solution</summary>

`False`, because `A` is not numeric.
</details>

---

### 2. (Level 1, Short Answer)
What does the function remove from the message?

<details>
<summary>Solution</summary>

It removes numeric characters and keeps non-numeric characters such as letters and spaces.
</details>

---

### 3. (Level 2, Coding)
Modify the function so it also converts the final message to uppercase.

<details>
<summary>Solution</summary>

Return `decrypted_message.upper()`.
</details>

---

### 4. (Level 2, Short Answer)
Why is `return` better than printing inside the function?

<details>
<summary>Solution</summary>

Returning makes the function reusable. The caller can print, store, or further process the result.
</details>

---

### 5. (Level 3, Coding)
Rewrite the function using a list and `join()`.

<details>
<summary>Solution</summary>

Append valid characters to a list and return `"".join(chars)`.
</details>

---

## 7. Further Reading

- [Python Docs: `str.isnumeric`](https://docs.python.org/3/library/stdtypes.html#str.isnumeric)
- [Python Docs: `return` statement](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement)
- [Python Docs: `for` statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)

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
