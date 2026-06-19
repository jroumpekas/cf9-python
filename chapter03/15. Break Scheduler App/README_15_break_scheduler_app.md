# 📅 Searching a Month with `break` and `for...else`

This lesson demonstrates two common ways to search for a value inside a list. The example asks the user for a three-letter month abbreviation and checks whether it exists in a predefined list.

---

## 1. Learning Objectives

- Store multiple values in a list.
- Read user input with `input()`.
- Compare strings without case sensitivity using `.casefold()`.
- Use a boolean flag to remember whether a value was found.
- Stop a loop early with `break`.
- Understand Python's `for...else` pattern.

---

## 2. Prerequisites

- Basic understanding of lists.
- Comfort with `for` loops.
- Basic familiarity with `if` statements.
- Basic experience with f-strings.

---

## 3. Key Concepts

- **List search**: Loop over each item and compare it with the target value.
- **Case-insensitive comparison**: `.casefold()` is stronger and safer than `.lower()` for text comparison.
- **Boolean flag**: A variable like `found = False` can track whether a match was found.
- **`break`**: Stops the loop as soon as the target is found.
- **`for...else`**: The `else` block runs only if the loop finishes without hitting `break`.

---

## 4. Lecture Outline

### 0:00–0:08 — Create the Month List
- Define `months = ["Jan", "Feb", "Mar"]`.

### 0:08–0:18 — First Way: Boolean Flag
- Start with `found = False`, search the list, and change it to `True` when a match appears.

### 0:18–0:28 — Second Way: `for...else`
- Use `break` when the month is found; otherwise let the `else` block handle the failure case.

### 0:28–0:35 — Compare the Two Approaches
- Both approaches work, but `for...else` avoids the extra `found` variable.

---

## 5. Code Demo

```python

def main():
    months = ["Jan", "Feb", "Mar"]
    input_month = input("Please insert 3 letters for a month: ")
    
    # 1st way
    found = False
    for month in months:
        if month.casefold() == input_month.casefold():
            found = True
            break
    
    print(f"Input month found {input_month}"
          if found else f"Month: {input_month} not found") 
    
    # 2nd way
    for month in months:
        if month.casefold() == input_month.casefold():
            print(f"Input month found: {input_month}")
            break
    else:
        print(f"Month: {input_month} not found")

if __name__ == "__main__":
    main()
```

**Expected output**:

```text
Please insert 3 letters for a month: feb
Input month found feb
Input month found: feb
```

> 💡 **Why does `for...else` work?:** The `else` block belongs to the loop, not to the `if`. It runs only when the loop ends normally, meaning no `break` happened.

> ⚠️ **Naming note:** The filename says `break_scheduler_app`, but the actual script demonstrates searching month abbreviations using `break`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `break` do inside a loop?

<details>
<summary>Solution</summary>

It stops the loop immediately.
</details>

---

### 2. (Level 1, Short Answer)
Why is `.casefold()` used on both strings?

<details>
<summary>Solution</summary>

It makes the comparison case-insensitive, so `Feb`, `feb`, and `FEB` are treated as the same value.
</details>

---

### 3. (Level 2, Coding)
Add the next three months to the list.

<details>
<summary>Solution</summary>

Use `months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]`.
</details>

---

### 4. (Level 2, Short Answer)
When does the `else` block of a `for...else` loop run?

<details>
<summary>Solution</summary>

It runs when the loop finishes without being stopped by `break`.
</details>

---

### 5. (Level 3, Coding)
Rewrite the search using the `in` operator and a normalized list.

<details>
<summary>Solution</summary>

Create `normalized_months = [month.casefold() for month in months]` and check `input_month.casefold() in normalized_months`.
</details>

---

## 7. Further Reading

- [Python Docs: `break`](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- [Python Docs: `str.casefold`](https://docs.python.org/3/library/stdtypes.html#str.casefold)
- [Python Docs: Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

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
