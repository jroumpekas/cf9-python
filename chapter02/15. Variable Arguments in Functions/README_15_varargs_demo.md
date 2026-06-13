# 📦 Variable-Length Arguments with `*args`

This lesson introduces `*args`, the syntax that lets a function accept **any number** of positional arguments. We build a `print_cities()` function that works whether you pass three cities, one city, or none at all.

---

## 1. Learning Objectives

- Define a function that accepts a variable number of positional arguments with `*args`.
- Understand that inside the function, `*cities` becomes a **tuple**.
- Use the **falsy-empty-tuple** check `if not cities:` to detect "no arguments".
- Join a collection of strings into one string with `", ".join(cities)`.

---

## 2. Prerequisites

- Comfort defining and calling functions.
- Familiarity with truthy/falsy values (an empty tuple is falsy).
- Awareness of strings and the `.join()` method.

---

## 3. Key Concepts

- **`*args`**: The asterisk collects all extra positional arguments into a single **tuple**. The name `args` is a convention; here it's `cities`.
- **Empty check**: When called with no arguments, `cities` is an empty tuple `()`, which is falsy, so `if not cities:` is `True`.
- **`str.join()`**: `", ".join(cities)` glues the tuple's strings together separated by `, `.
- **`pass`**: A no-op statement. The trailing `pass` in this function does nothing — it's harmless but unnecessary.

---

## 4. Lecture Outline

### 0:00–0:08 — Declaring `*cities`
- `def print_cities(*cities):` — any number of city names allowed.

### 0:08–0:16 — Detecting "No Cities"
- `if not cities:` → prints `No cities provided`.

### 0:16–0:24 — Joining the Cities
- `", ".join(cities)` builds the comma-separated list.

### 0:24–0:30 — Three Calls
- Three cities, one city, and zero cities.

---

## 5. Code Demos

```python
def print_cities(*cities):
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", ", ".join(cities))

def main():
    print_cities("Athens", "Paris", "London")
    print_cities("Athens")
    print_cities()

if __name__ == "__main__":
    main()
```

**Expected output:**

```
Cities: Athens, Paris, London
Cities: Athens
No cities provided
```

> 💡 **`cities` is a tuple.** Even when you pass a single argument, `cities` is the one-element tuple `("Athens",)`. You can loop over it, index it, or measure it with `len(cities)` just like any other tuple.

> 🧹 **Minor cleanup:** the original file ended the function with a `pass` statement. `pass` is only needed where Python requires a statement but you have nothing to run (e.g. an empty function body). After the `if/else` it does nothing and can be removed.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Inside `def f(*args):`, what type is `args`?
- a) list
- b) tuple
- c) set
- d) dict

<details>
<summary>Solution</summary>

**Answer:** b) tuple.
</details>

---

### 2. (Level 1, Short Answer)
What does `print_cities()` (called with no arguments) print, and why?

<details>
<summary>Solution</summary>

It prints `No cities provided`. With no arguments, `cities` is the empty tuple `()`, which is falsy, so `if not cities:` is `True`.
</details>

---

### 3. (Level 2, Coding)
Write a function `count_items(*items)` that returns how many items were passed.

<details>
<summary>Solution</summary>

```python
def count_items(*items):
    return len(items)

print(count_items("a", "b", "c"))   # 3
print(count_items())                # 0
```
</details>

---

### 4. (Level 2, Coding)
Modify `print_cities` so it numbers each city, e.g. `1. Athens`, `2. Paris`.

<details>
<summary>Solution</summary>

```python
def print_cities(*cities):
    if not cities:
        print("No cities provided")
    else:
        for i, city in enumerate(cities, start=1):
            print(f"{i}. {city}")
```
</details>

---

### 5. (Level 3, Coding)
You have a list `my_cities = ["Rome", "Madrid"]`. Call `print_cities` so the two cities are passed as **separate** arguments, not as one list.

<details>
<summary>Solution</summary>

```python
my_cities = ["Rome", "Madrid"]
print_cities(*my_cities)   # the * "unpacks" the list into separate arguments
# Output: Cities: Rome, Madrid
```
The unpacking `*` at the **call site** is the mirror image of `*args` in the definition.
</details>

---

## 7. Further Reading

- [Python Tutorial: Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
- [Python Tutorial: Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)
- [Python Docs: `str.join`](https://docs.python.org/3/library/stdtypes.html#str.join)

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
