# 🔧 Combining `*args` with a Keyword-Only Parameter

This lesson extends the previous `print_cities` example by adding a parameter **after** `*args`. Anything that follows `*cities` becomes a **keyword-only** parameter, which is exactly how the built-in `print()` handles its `sep=` argument.

---

## 1. Learning Objectives

- Add a parameter after `*args` and understand it becomes **keyword-only**.
- Give that keyword-only parameter a default value (`separator=", "`).
- Mimic the behaviour of `print()`'s built-in `sep=` argument.
- See why you *must* pass the separator by name, never by position.

---

## 2. Prerequisites

- This lesson builds directly on `15_varargs_demo.py` (`*args`).
- Comfort with default parameter values.
- Familiarity with `str.join()`.

---

## 3. Key Concepts

- **Keyword-only parameter**: Any parameter listed **after** `*args` can only be supplied by name. `print_cities("Athens", separator="\t")` is valid; passing it positionally is not.
- **`*cities: str`**: Type hint saying each collected argument should be a string.
- **`-> None`**: Return-type hint stating the function returns nothing (it only prints).
- **Built-in `print(..., sep=...)`**: Python's own `print` uses the same pattern — `sep` is keyword-only.

---

## 4. Lecture Outline

### 0:00–0:08 — A Parameter After `*args`
- `def print_cities(*cities: str, separator: str = ", ") -> None:`

### 0:08–0:16 — Why It's Keyword-Only
- All positional arguments are swallowed by `*cities`, so `separator` can only arrive by name.

### 0:16–0:24 — Custom Separators
- `print_cities("Athens", "Paris", separator="\t")` joins with tabs.

### 0:24–0:30 — Comparing to Built-in `print`
- `print("Athens", "Paris", sep="\t")` does the same thing natively.

---

## 5. Code Demos

> 📝 The original docstring just said `"Homework"` and the parameter was spelled `seperator`. Below it is corrected to the standard English spelling **`separator`** (the common real-world spelling). The behaviour is identical either way — just keep the spelling consistent between the definition and the call.

```python
def print_cities(*cities: str, separator: str = ", ") -> None:
    """Print all the given cities joined by `separator` (keyword-only)."""
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", separator.join(cities))

def main():
    print_cities("Athens", "Paris", "London", separator="\t")
    print("Athens", "Paris", "London", sep="\t")   # built-in print's own sep
    print_cities()

if __name__ == "__main__":
    main()
```

**Expected output:**

```
Cities: Athens	Paris	London
Athens	Paris	London
No cities provided
```

> 💡 **Why keyword-only is a *feature*.** Because `*cities` greedily grabs every positional argument, there is no ambiguity about what `separator` means — it can never be mistaken for "one more city". This is why `print()` was designed the same way: you can pass unlimited values plus a clearly-named `sep`.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Given `def f(*args, key="x")`, which call is **valid**?
- a) `f(1, 2, "y")`
- b) `f(1, 2, key="y")`
- c) Both
- d) Neither

<details>
<summary>Solution</summary>

**Answer:** b) `f(1, 2, key="y")`. In option (a), `"y"` would be swallowed by `*args` as a third positional value, so `key` would still be `"x"` — not what you intended.
</details>

---

### 2. (Level 1, Short Answer)
What is the difference between `print_cities`'s `separator` and the built-in `print`'s `sep`?

<details>
<summary>Solution</summary>

Functionally they do the same job — choose the string placed between items. They are just two separate implementations: `separator` is our custom parameter, `sep` is `print`'s built-in keyword-only parameter.
</details>

---

### 3. (Level 2, Coding)
Call `print_cities` so it prints the three cities separated by ` | ` (space-pipe-space).

<details>
<summary>Solution</summary>

```python
print_cities("Athens", "Paris", "London", separator=" | ")
# Cities: Athens | Paris | London
```
</details>

---

### 4. (Level 2, Coding)
Write a function `make_path(*parts, sep="/")` that joins path parts, e.g. `make_path("home", "user", "file")` → `home/user/file`.

<details>
<summary>Solution</summary>

```python
def make_path(*parts, sep="/"):
    return sep.join(parts)

print(make_path("home", "user", "file"))   # home/user/file
```
</details>

---

### 5. (Level 3, Coding)
Add a second keyword-only parameter `prefix=""` to `print_cities` so the output becomes `Cities: >Athens >Paris` when `prefix=">"`.

<details>
<summary>Solution</summary>

```python
def print_cities(*cities: str, separator: str = ", ", prefix: str = "") -> None:
    if not cities:
        print("No cities provided")
    else:
        decorated = [prefix + c for c in cities]
        print("Cities:", separator.join(decorated))

print_cities("Athens", "Paris", separator=" ", prefix=">")
# Cities: >Athens >Paris
```
</details>

---

## 7. Further Reading

- [Python Docs: Keyword-Only Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-only-arguments)
- [PEP 3102 — Keyword-Only Arguments](https://peps.python.org/pep-3102/)
- [Python Docs: `print`](https://docs.python.org/3/library/functions.html#print)

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
