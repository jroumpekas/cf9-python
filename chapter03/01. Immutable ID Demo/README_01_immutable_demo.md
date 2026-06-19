# 🆔 Object Identity & Immutability with `id()`

This lesson uses the built-in `id()` function to peek at the memory identity of objects. It reveals two surprising-but-important CPython behaviours: **small integer caching** and **string interning**, and it shows what "immutable" really means — rebinding a name creates a *new* object rather than changing the old one.

---

## 1. Learning Objectives

- Use `id(obj)` to read an object's unique identity.
- Understand that immutable objects (`int`, `str`) cannot be changed in place.
- Observe **small integer caching**: small ints reuse the same object.
- Observe **string interning**: identical string literals can share one object.
- Explain why reassigning `b = 20` gives `b` a brand-new id while `a` is untouched.

---

## 2. Prerequisites

- Comfort with variables, functions, and f-strings.
- Awareness that `int` and `str` are immutable types.

---

## 3. Key Concepts

- **`id(obj)`**: Returns an integer that is unique for the object during its lifetime (in CPython, its memory address).
- **Identity vs value**: Two names can point to the *same* object (same `id`) or to different objects with equal values.
- **Immutability**: You can't mutate `10` or `"CF9"`. Writing `b = 20` doesn't change the `10` object — it rebinds `b` to a different object.
- **Small integer caching**: CPython pre-creates and reuses integer objects from **-5 to 256**, so `a = 10` and `b = 10` share one object.
- **String interning**: Short, identifier-like string literals are often cached, so `"CF9"` and `"CF9"` may share one object.

---

## 4. Lecture Outline

### 0:00–0:08 — The `print_id` Helper
- A small function that prints `id(name) = ...`.

### 0:08–0:18 — Two Names, One Integer
- `a = 10` and `b = 10` report the **same** id (caching).

### 0:18–0:26 — Rebinding `b`
- After `b = 20`, `b`'s id changes; `a` stays the same.

### 0:26–0:34 — Interned Strings
- `str1` and `str2` (both `"CF9"`) report the **same** id.

---

## 5. Code Demos

```python
def print_id(variable_name, variable):
    """Prints the id of the given variable."""
    print(f"id({variable_name}) = {id(variable)}")

def main():
    a = 10
    b = 10

    print_id("a", a)
    print_id("b", b)        # same id as a (small-int caching)

    print("Now I change the value of b.")
    b = 20
    print_id("a", a)        # unchanged
    print_id("b", b)        # new id
    print(a, b)             # 10 20

    str1 = "CF9"
    str2 = "CF9"
    print_id("str1", str1)
    print_id("str2", str2)  # same id as str1 (interning)

if __name__ == '__main__':
    main()
```

**Expected output** (the exact numbers are machine-specific; what matters is which ids *match*):

```
id(a) = 140234...001
id(b) = 140234...001      <- same as a
Now I change the value of b.
id(a) = 140234...001      <- unchanged
id(b) = 140234...537      <- new object
10 20
id(str1) = 140234...888
id(str2) = 140234...888   <- same as str1
```

> 💡 **Why do `a` and `b` start with the same id?** CPython keeps a cache of small integer objects (−5 through 256). Both `a = 10` and `b = 10` are handed the *same* pre-built `10` object, so their ids match. Try `a = 1000; b = 1000` and you'll often see **different** ids, because 1000 is outside the cache.

> ⚠️ **Don't rely on interning for comparisons.** The fact that `"CF9" is "CF9"` may be `True` is a CPython optimisation, not a language guarantee. To compare *values*, always use `==`, never `is`. Use `is` only to check identity (most commonly `x is None`).

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `id(x)` return?
- a) The value of `x`
- b) A unique identifier for the object during its lifetime
- c) The type of `x`
- d) The size of `x` in bytes

<details>
<summary>Solution</summary>

**Answer:** b) A unique identity for the object (in CPython, its memory address).
</details>

---

### 2. (Level 1, Short Answer)
After `b = 20`, why does `a` still report its original id?

<details>
<summary>Solution</summary>

Integers are immutable. `b = 20` doesn't modify the `10` object — it rebinds the name `b` to a *different* object (`20`). The name `a` still points to the original `10`, so its id is unchanged.
</details>

---

### 3. (Level 2, Coding)
Predict whether the ids match, then test: `x = 256; y = 256` and `x = 257; y = 257`.

<details>
<summary>Solution</summary>

```python
x = 256; y = 256
print(id(x) == id(y))   # True  (256 is in the cache)

x = 257; y = 257
print(id(x) == id(y))   # often False (257 is outside the -5..256 cache)
```
</details>

---

### 4. (Level 2, Short Answer)
What is the difference between `is` and `==`?

<details>
<summary>Solution</summary>

`is` checks **identity** — whether two names point to the same object (compares ids). `==` checks **value/content** — whether two objects are considered equal. Two different objects can be `==` while not being `is`.
</details>

---

### 5. (Level 3, Coding)
Build a string at runtime so it is **not** interned, and show that `is` returns `False` while `==` returns `True`.

<details>
<summary>Solution</summary>

```python
a = "CF9"
b = "CF" + str(9)        # built at runtime, not a literal -> usually not interned
print(a == b)            # True  (same content)
print(a is b)            # usually False (different objects)
```
This is the clearest demonstration of why you compare strings with `==`, not `is`.
</details>

---

## 7. Further Reading

- [Python Docs: `id`](https://docs.python.org/3/library/functions.html#id)
- [Python Docs: `is` (Identity comparisons)](https://docs.python.org/3/reference/expressions.html#is)
- [Python Docs: `sys.intern`](https://docs.python.org/3/library/sys.html#sys.intern)

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
