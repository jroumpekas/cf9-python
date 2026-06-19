# 🔤 Name Spacing with `join()`

This lesson demonstrates how to take a user's name and print it with a fixed number of spaces between every character. It is a compact example for practicing **input validation**, **string cleanup**, and the powerful string method **`join()`**.

---

## 1. Learning Objectives

- Validate that a function argument is an integer.
- Reject invalid values such as negative spacing.
- Read user input with `input()`.
- Clean user input with `.strip()`.
- Use `join()` to insert a separator between characters.
- Structure a script with `main()` and the `if __name__ == "__main__"` guard.

---

## 2. Prerequisites

- Basic understanding of functions.
- Basic familiarity with `if` statements.
- Comfort with strings and user input.
- Awareness of simple type checking with `isinstance()`.

---

## 3. Key Concepts

- **Function parameter**: `num` controls how many spaces are placed between letters.
- **Type validation**: `isinstance(num, int)` checks whether `num` is an integer.
- **Early return**: The function stops immediately when the input is invalid.
- **`.strip()`**: Removes leading and trailing spaces from the user's name.
- **`join()`**: Places a separator between every character of an iterable string.
- **Main guard**: Ensures the script runs only when executed directly.

---

## 4. Lecture Outline

### 0:00–0:08 — Function Definition
- Create `name_spacing(num: int)` and define the spacing parameter.

### 0:08–0:18 — Validate the Number of Spaces
- Check that `num` is an integer and is not negative.

### 0:18–0:28 — Read and Clean the Name
- Ask the user for a name and remove unnecessary spaces with `.strip()`.

### 0:28–0:38 — Create the Spaced Name
- Use `(' ' * num).join(name)` to add spaces between characters.

---

## 5. Code Demo

```python
def name_spacing(num: int):
  if not isinstance(num, int):
     print("The number of spaces must be an integer. ")
     return
  
  if num < 0:
     print("The number of spaces has to be positive")
     return
  
  name = input("Please give a name: ").strip()

  if not name:
     print("No name provided")
     return
  
  spaced_name = (' ' * num).join(name)
  print(spaced_name)

def main():
    name_spacing(4)

if __name__ == "__main__":
    main()
```

**Expected output**:

```text
Please give a name: Dimitris
D    i    m    i    t    r    i    s
```

> 💡 **Why does `join()` work here?:** A string is iterable, so Python can loop over each character of `name`. The expression `' ' * num` creates the separator, and `.join(name)` places that separator between each character.

> ⚠️ **Small detail:** The check `num < 0` allows `0`. If `num` is `0`, the name prints normally without spaces between letters.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `.strip()` do?

<details>
<summary>Solution</summary>

b) Removes leading and trailing whitespace.
</details>

---

### 2. (Level 1, Short Answer)
What happens if the user presses Enter without typing a name?

<details>
<summary>Solution</summary>

After `.strip()`, the input becomes an empty string. The condition `if not name:` becomes `True`, so the program prints `No name provided` and stops.
</details>

---

### 3. (Level 2, Coding)
Change the program so it uses two dashes between every character instead of spaces.

<details>
<summary>Solution</summary>

`"--".join("CF9")` produces `C--F--9`.
</details>

---

### 4. (Level 2, Short Answer)
Why do we use `return` after printing an error message?

<details>
<summary>Solution</summary>

`return` exits the function early and prevents the rest of the code from running with invalid data.
</details>

---

### 5. (Level 3, Coding)
Rewrite `main()` so the user also gives the number of spaces from the keyboard.

<details>
<summary>Solution</summary>

Use `spaces = int(input("Give number of spaces: "))` inside a `try` block and then call `name_spacing(spaces)`.
</details>

---

## 7. Further Reading

- [Python Docs: `str.join`](https://docs.python.org/3/library/stdtypes.html#str.join)
- [Python Docs: `str.strip`](https://docs.python.org/3/library/stdtypes.html#str.strip)
- [Python Docs: `isinstance`](https://docs.python.org/3/library/functions.html#isinstance)

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
