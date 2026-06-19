# 🎯 Number Guessing Game (`random`, Loops & Validation)

This lesson builds a complete little game: the computer picks a secret number, and the user has a limited number of tries to guess it, getting "Hot"/"Cold" hints along the way. It's a great showcase of clean function decomposition, robust input handling, and loop control.

---

## 1. Learning Objectives

- Generate a random number with `random.randint(a, b)`.
- Loop input until it's valid using `try`/`except` inside a `while True`.
- Decompose a program into focused functions (`get_user_guess`, `check_guess`, `main`).
- Use a counter and a constant (`MAX_TRIES`) to limit attempts.
- Return a boolean from a function to drive control flow.

---

## 2. Prerequisites

- Comfort with functions, `while` loops, and `break`.
- Familiarity with `try`/`except` and `int(input(...))`.

---

## 3. Key Concepts

- **`random.randint(1, 10)`**: Returns a random integer between 1 and 10, **inclusive** on both ends.
- **Input loop**: `get_user_guess` keeps asking until `int()` succeeds — invalid input never crashes the game.
- **`abs(guess - secret) <= 5`**: Distance check for the "Hot" hint regardless of direction.
- **Boolean return**: `check_guess` returns `True` on a win so `main` can `break`.
- **Constant naming**: `MAX_TRIES` in all-caps signals "this is a fixed configuration value".

---

## 4. Lecture Outline

### 0:00–0:10 — Robust Input
- `get_user_guess` loops on `ValueError`.

### 0:10–0:20 — The Hint Logic
- `check_guess`: exact match → win; within 5 → "Hot"; else "Cold".

### 0:20–0:30 — The Game Loop
- `main` runs up to `MAX_TRIES`, breaks on a win, reports if tries run out.

---

## 5. Code Demos

```python
import random

def get_user_guess():
    """Prompt until the user enters a valid integer, then return it."""
    while True:
        try:
            return int(input("Please insert an int: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_guess(secret, guess):
    """Return True if guess is correct; otherwise print a Hot/Cold hint."""
    if guess == secret:
        print("Bingo! Secret number:", secret)
        return True
    elif abs(guess - secret) <= 5:
        print("Hot")
    else:
        print("Cold")
    return False

def main():
    secret_number = random.randint(1, 10)
    MAX_TRIES = 5
    tries = 0

    while tries < MAX_TRIES:
        guess = get_user_guess()
        if check_guess(secret_number, guess):
            break
        tries += 1

    if tries == MAX_TRIES:
        print("You reached the max number of tries:", MAX_TRIES)

if __name__ == "__main__":
    main()
```

**Example run:**

```
Please insert an int: 8
Cold
Please insert an int: 4
Hot
Please insert an int: 6
Bingo! Secret number: 6
```

> 💡 **Why the win-on-last-try works correctly.** `tries` is incremented **only on a wrong guess**. If the player guesses right on their fifth attempt, the code `break`s with `tries` still at `4`, so the "max tries" message is correctly *not* shown. The message appears only after five genuinely wrong guesses.

> 🧱 **Clean separation of concerns.** Input lives in `get_user_guess`, game rules in `check_guess`, and orchestration in `main`. Each function does one job, which makes the game easy to test and extend.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is the range of possible values from `random.randint(1, 10)`?
- a) 1 to 9
- b) 0 to 10
- c) 1 to 10 inclusive
- d) 0 to 9

<details>
<summary>Solution</summary>

**Answer:** c) 1 to 10 inclusive — both endpoints are possible.
</details>

---

### 2. (Level 1, Short Answer)
Why does `get_user_guess` use `while True` with `try`/`except`?

<details>
<summary>Solution</summary>

So that invalid input (non-integers) doesn't crash the program. The loop keeps re-prompting until `int()` succeeds, at which point it returns the value.
</details>

---

### 3. (Level 2, Coding)
Change the hint so it tells the player whether to guess **higher** or **lower**.

<details>
<summary>Solution</summary>

```python
def check_guess(secret, guess):
    if guess == secret:
        print("Bingo!", secret)
        return True
    print("Too low" if guess < secret else "Too high")
    return False
```
</details>

---

### 4. (Level 2, Short Answer)
What would change if `tries += 1` were placed *before* the `if check_guess(...)` instead of after?

<details>
<summary>Solution</summary>

A correct final-attempt guess would still leave `tries == MAX_TRIES`, so the "max tries reached" message would print *even after a win*. Counting only wrong guesses (current code) avoids that.
</details>

---

### 5. (Level 3, Coding)
Make the secret range and number of tries configurable via constants at the top, and widen the range to 1–100.

<details>
<summary>Solution</summary>

```python
LOW, HIGH, MAX_TRIES = 1, 100, 7
secret_number = random.randint(LOW, HIGH)
# ...use MAX_TRIES in the loop as before
```
Centralising configuration in named constants makes the game easy to tune.
</details>

---

## 7. Further Reading

- [Python Docs: `random.randint`](https://docs.python.org/3/library/random.html#random.randint)
- [Python Docs: `abs`](https://docs.python.org/3/library/functions.html#abs)
- [Python Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

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
