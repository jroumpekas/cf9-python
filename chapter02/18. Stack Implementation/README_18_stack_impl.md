# 🥞 A Menu-Driven Stack (LIFO) with Input Validation

This is the biggest example in the chapter: an interactive program that implements a **stack** (Last-In-First-Out) using a Python list, driven by a text menu, and validated with **regular expressions** and a **`match`/`case`** statement.

---

## 1. Learning Objectives

- Implement the two core stack operations: **push** (add to top) and **pop** (remove from top).
- Build a menu loop with `while True:` and `break`.
- Read user input with `input()` and validate it with the `re` module.
- Branch on a value using the `match` / `case` statement (Python 3.10+).
- Recognise and fix an indentation/comment bug that stops the program from running.

---

## 2. Prerequisites

- Comfort with lists and `list.append()` / `list.pop()`.
- Familiarity with `while` loops, `break`, and `continue`.
- Basic awareness of functions and the `if __name__ == "__main__"` idiom.

---

## 3. Key Concepts

- **Stack (LIFO)**: The last item pushed is the first popped. A Python list is a perfect stack: `append()` pushes, `pop()` pops the last element.
- **`re.match(pattern, text)`**: Returns a match object if the pattern matches at the *start* of the text, else `None` (falsy).
- **Pattern `r'^\d$'`**: `^` start, `\d` one digit, `$` end → exactly one digit.
- **Pattern `r'^\d+$'`**: `\d+` = one or more digits → a whole non-negative integer.
- **`match` / `case`**: Structural pattern matching introduced in Python 3.10; `case _:` is the default ("everything else").

---

## 4. Lecture Outline

### 0:00–0:08 — Stack Helpers
- `push`, `pop`, and `print_stack` operate on a list passed in.

### 0:08–0:16 — The Menu Loop
- `print_menu()`, `get_choice()`, and the `while True:` driver.

### 0:16–0:26 — Validating Input with Regex
- `r'^\d$'` for the single-digit menu choice, `r'^\d+$'` for the number to push.

### 0:26–0:36 — Dispatching with `match`
- `case 1` push, `case 2` pop, `case 3` print, `case _` error.

---

## 5. Code Demos (Corrected)

> ⚠️ **Critical bug in the uploaded file — read this first.** The original had the quit check written *inside a comment*:
> ```python
> # If the user wants to quit, check for 'q' or 'Q'.if choice == 'q' or choice == 'Q': # ...
>     break  # Exit the loop and end the program.
> ```
> Everything after `#` is a comment, so the `if` never executes — and the lonely `break` underneath it is indented one level too deep, which makes Python raise **`IndentationError: unexpected indent`**. The program won't even start. The fix is to put the `if` on its **own line** (no `#` in front) and align `break` under it.

Below is the cleaned-up, runnable version:

```python
import re

stack = []

def push(lst, item):
    lst.append(item)               # add to the top

def pop(lst):
    if lst:
        return lst.pop()           # remove & return the top
    else:
        print("Stack is empty")

def print_stack(lst):
    if lst:
        print("Current stack:", lst)
    else:
        print("Stack is empty")

def print_menu():
    print("1. Insert on top")
    print("2. Get from top")
    print("3. Print stack")
    print("4. q/Q for Quit")

def get_choice():
    return input("Please provide a choice\n")

def main():
    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue

        # FIXED: the quit check is now real code, not a comment
        if choice == 'q' or choice == 'Q':
            break

        if not re.match(r'^\d$', choice):     # must be a single digit
            print("Error in choice")
            continue

        choice = int(choice)

        match choice:
            case 1:
                num = input("Please insert a number: ")
                if not re.match(r'^\d+$', num):
                    print("Error")
                    continue
                num = int(num)
                push(stack, num)
                print(str(num) + " inserted")
            case 2:
                out_num = pop(stack)
                if out_num is not None:
                    print("You got:", out_num)
            case 3:
                print_stack(stack)
            case _:
                print("Not valid choice")

if __name__ == "__main__":
    main()
```

**Example session:**

```
1. Insert on top
2. Get from top
3. Print stack
4. q/Q for Quit
Please provide a choice
1
Please insert a number: 42
42 inserted
...
Please provide a choice
2
You got: 42
...
Please provide a choice
q
```

> 💡 **Why LIFO matters.** Because `pop()` always removes the *last* item appended, if you push `1`, then `2`, then `3`, the first thing you pop is `3`. That "last in, first out" order is the defining property of a stack — used for undo history, function call frames, and expression evaluation.

---

## 6. Exercises

### 1. (Level 1, MCQ)
In a stack, which item is removed first?
- a) The oldest (first pushed)
- b) The newest (last pushed)
- c) A random one
- d) The smallest

<details>
<summary>Solution</summary>

**Answer:** b) The newest, last-pushed item — that's the "Last In, First Out" rule.
</details>

---

### 2. (Level 1, Short Answer)
Why did the original file fail with an `IndentationError` before it could ask for any input?

<details>
<summary>Solution</summary>

The intended `if choice == 'q' ...:` line started with `#`, so Python treated it as a comment. The `break` below it was indented as if it belonged to that `if`, but since the `if` didn't exist as code, the indented `break` was "unexpected" — raising `IndentationError`.
</details>

---

### 3. (Level 2, Coding)
Write a `peek(lst)` function that returns the top item **without** removing it, or `None` if the stack is empty.

<details>
<summary>Solution</summary>

```python
def peek(lst):
    if lst:
        return lst[-1]   # last element = top, not removed
    return None
```
</details>

---

### 4. (Level 2, Coding)
What regular expression matches a string of one or more digits, and nothing else? Explain each symbol.

<details>
<summary>Solution</summary>

`r'^\d+$'`:
- `^` — start of string
- `\d` — a digit (0–9)
- `+` — one or more of the preceding
- `$` — end of string

So the whole string must be made up entirely of digits.
</details>

---

### 5. (Level 3, Coding)
Add a `case 4:` to the `match` that prints the current size of the stack (number of items) without removing anything.

<details>
<summary>Solution</summary>

```python
case 4:
    print("Stack size:", len(stack))
```
(Remember to mention option 4 in `print_menu()` too.)
</details>

---

## 7. Further Reading

- [Python Docs: `re` — Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python Tutorial: `match` Statements](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [Python Docs: Using Lists as Stacks](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)

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
