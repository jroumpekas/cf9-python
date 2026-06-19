# 🔑 Random Password Generator

This lesson demonstrates how to build a simple command-line password generator using Python's `random` and `string` modules. The script asks the user for a password length and creates a random password from letters, digits, and selected special characters.

---

## 1. Learning Objectives

- Import and use Python standard library modules.
- Build a character pool using `string.ascii_letters`, `string.digits`, and special characters.
- Read and validate numeric user input.
- Handle invalid input with `try...except`.
- Use `random.choice()` to select random characters.
- Use a `while True` menu loop with a quit option.
- Understand a common list/string conversion mistake.

---

## 2. Prerequisites

- Basic understanding of lists and strings.
- Comfort with functions and loops.
- Basic familiarity with `try...except`.
- Awareness of user input validation.

---

## 3. Key Concepts

- **`string.ascii_letters`**: Contains lowercase and uppercase English letters.
- **`string.digits`**: Contains the characters `0` through `9`.
- **Character pool**: A list of possible characters used to build the password.
- **`random.choice()`**: Selects one random item from a sequence.
- **`random.shuffle()`**: Randomly reorders a list in place.
- **`try...except ValueError`**: Protects the program when the user does not type a valid integer.
- **Menu loop**: Keeps asking the user whether they want to generate another password.

---

## 4. Lecture Outline

### 0:00–0:08 — Build the Character Pool
- Combine letters, digits, and special characters.

### 0:08–0:18 — Ask for Password Length
- Read the length from the user and convert it to `int`.

### 0:18–0:30 — Validate the Input
- Reject non-integers and non-positive lengths.

### 0:30–0:42 — Generate the Password
- Pick random characters and join them into one string.

### 0:42–0:55 — Repeat or Quit
- Let the user generate more passwords or exit with `q`.

---

## 5. Code Demo

```python
import string
import random

characters = list(string.ascii_letters + string.digits + "!@%#^&")


def generate_password():
    """
    Generate a random password based on the user-specified length.
    """

    try:
        password_length = int(input("Please give the password length: "))

        if password_length <= 0:
            print("Password length must be a positive integer.")
            return

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    password = []

    for _ in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)

    print(f"\nGenerated password: {password}")


def main():
    while True:
        option = input("Do you want to create a password? ('y' or 'q' for quit): ")

        if option.lower() == "y":
            generate_password()
        elif option.lower() == "q":
            print("Goodbye")
            break
        else:
            print("Wrong input")


if __name__ == "__main__":
    main()
```

**Expected output**:

```text
Do you want to create a password? ('y' or 'q' for quit): y
Please give the password length: 10

Generated password: D8f#qA2m@z
Do you want to create a password? ('y' or 'q' for quit): q
Goodbye
```

> 💡 **Why use a list first?:** Lists are easy to append to and shuffle. After the password is complete, `"".join(password)` converts the list of characters into one string.

> ⚠️ **Known issue in the draft version:** If `password = "".join(password)` is placed inside the `for` loop, `password` becomes a string too early. On the next iteration, `password.append(...)` will fail because strings do not have `.append()`.

> ⚠️ **Security note:** This script is useful for practice. For real security-sensitive password generation, prefer Python's `secrets` module instead of `random`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which module provides `ascii_letters` and `digits`?

<details>
<summary>Solution</summary>

`string`.
</details>

---

### 2. (Level 1, Short Answer)
Why do we check `password_length <= 0`?

<details>
<summary>Solution</summary>

Because a password length must be positive. A length of `0` or a negative number does not make sense.
</details>

---

### 3. (Level 2, Coding)
Add the characters `?` and `*` to the character pool.

<details>
<summary>Solution</summary>

Use `characters = list(string.ascii_letters + string.digits + "!@%#^&?*")`.
</details>

---

### 4. (Level 2, Short Answer)
What is the difference between `random.choice()` and `random.shuffle()`?

<details>
<summary>Solution</summary>

`random.choice()` selects one random item. `random.shuffle()` reorders the items of a list in place.
</details>

---

### 5. (Level 3, Coding)
Rewrite the generator using the `secrets` module.

<details>
<summary>Solution</summary>

Use `secrets.choice(characters)` inside a generator expression and join the result.
</details>

---

## 7. Further Reading

- [Python Docs: `random`](https://docs.python.org/3/library/random.html)
- [Python Docs: `string`](https://docs.python.org/3/library/string.html)
- [Python Docs: `secrets`](https://docs.python.org/3/library/secrets.html)

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
