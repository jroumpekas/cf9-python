# 🔀 Three Ways to Check "Is It q or Q?" — `or`, `.upper()`, and `in`

This short lesson compares three idioms for the same task: checking whether a character is `q` or `Q`. It builds toward the most **Pythonic** approach — membership testing with `in`.

---

## 1. Learning Objectives

- Combine conditions with the boolean `or` operator.
- Normalise case with `str.upper()` before comparing.
- Use the **`in`** operator to test membership in a tuple.
- Appreciate why the `in` version is the cleanest and most extensible.

---

## 2. Prerequisites

- Comfort with `if` / `else`.
- Familiarity with strings and string methods.
- Awareness of tuples `('q', 'Q')`.

---

## 3. Key Concepts

- **`or`**: `a or b` is `True` if either side is `True`. `choice == 'q' or choice == 'Q'` checks both literals explicitly.
- **`str.upper()`**: Returns an uppercase copy, so `choice.upper() == 'Q'` matches both cases with one comparison.
- **`in`**: `choice in ('q', 'Q')` is `True` if `choice` equals any element of the tuple. This is the idiomatic, readable choice.
- **Extensibility**: To accept more options, the `in` form only needs a longer tuple — `('q', 'Q', 'exit')` — while the `or` chain grows long and repetitive.

---

## 4. Lecture Outline

### 0:00–0:07 — The Explicit `or`
- `if choice == 'q' or choice == "Q":`

### 0:07–0:14 — Normalising with `.upper()`
- `if choice.upper() == 'Q':`

### 0:14–0:22 — The Pythonic `in`
- `if choice in ('q', 'Q'):` — commented "Pythonian!" in the source, and rightly so.

---

## 5. Code Demos

```python
choice = 'q'

# 1) explicit `or`
if choice == 'q' or choice == "Q":
    print("OK")
else:
    print("Not OK")

# 2) normalise case with .upper()
if choice.upper() == 'Q':
    print("OK")
else:
    print("Not OK")

# 3) membership with `in`  (the Pythonic way!)
if choice in ('q', 'Q'):
    print("OK")
else:
    print("Not OK")
```

**Expected output:**

```
OK
OK
OK
```

> 💡 **Which one should you reach for?** All three are correct. `.upper()` is great when *any* casing is acceptable. `in` shines when you have a fixed set of allowed values — and reads almost like English: "if choice in these options".

> ⚠️ **A subtle trap with `.upper()`.** `choice.upper() == 'Q'` works only because you compare against the **uppercase** literal. If you accidentally wrote `choice.upper() == 'q'`, it would always be `False`, since `.upper()` never produces a lowercase letter.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `'a' in ('a', 'b', 'c')` evaluate to?
- a) `True`
- b) `False`
- c) `'a'`
- d) Error

<details>
<summary>Solution</summary>

**Answer:** a) `True`. `'a'` is one of the tuple's elements.
</details>

---

### 2. (Level 1, Short Answer)
Rewrite `if x == 'y' or x == 'Y' or x == 'yes':` using the `in` operator.

<details>
<summary>Solution</summary>

```python
if x in ('y', 'Y', 'yes'):
    ...
```
</details>

---

### 3. (Level 2, Coding)
Using `.lower()`, write a check that accepts `"YES"`, `"Yes"`, `"yes"`, or `"yEs"` as agreement.

<details>
<summary>Solution</summary>

```python
answer = "Yes"
if answer.lower() == "yes":
    print("Agreed")
```
</details>

---

### 4. (Level 2, Coding)
Combine `.lower()` and `in` to accept any casing of `"q"` or `"quit"`.

<details>
<summary>Solution</summary>

```python
choice = "QUIT"
if choice.lower() in ("q", "quit"):
    print("Quitting")
```
</details>

---

### 5. (Level 3, Short Answer)
Why is the `in` form generally preferred over a long `or` chain as the number of accepted values grows?

<details>
<summary>Solution</summary>

It is shorter, less error-prone (you don't repeat `choice ==` each time), easier to read, and trivial to extend — you just add another item to the tuple/list/set. Membership testing against a `set` is also faster for large collections.
</details>

---

## 7. Further Reading

- [Python Docs: Boolean Operations (`or`)](https://docs.python.org/3/reference/expressions.html#boolean-operations)
- [Python Docs: Membership Test Operations (`in`)](https://docs.python.org/3/reference/expressions.html#membership-test-operations)
- [Python Docs: `str.upper`](https://docs.python.org/3/library/stdtypes.html#str.upper)

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
