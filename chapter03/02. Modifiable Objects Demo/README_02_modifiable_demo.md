# 🔗 References, Aliasing & Mutability

This lesson is the mutable counterpart to the previous one. It shows that assigning one list to another name (`new_list = original_list`) does **not** copy the list — both names point to the *same* object. Mutating through one name is visible through the other.

---

## 1. Learning Objectives

- Understand that assignment binds a **name** to an object, it does not copy.
- Recognise **aliasing**: two names referring to one mutable object.
- See that mutating a list through one alias is visible through all aliases.
- Confirm with `id()` that two aliases share an identity, while a separately-built list does not.

---

## 2. Prerequisites

- Familiarity with `id()` and identity (see `01_immutable_demo.py`).
- Comfort with lists and index assignment (`lst[0] = 100`).

---

## 3. Key Concepts

- **Assignment = binding, not copying**: `new_list = original_list` makes `new_list` a second name for the *same* list object.
- **Aliasing**: Both names alias one object, so `original_list[0] = 100` also changes `new_list`.
- **Same id**: Aliases report the same `id()`.
- **Equal content ≠ same object**: `temp_list = [100, 2, 3]` has the same content as `original_list` but is a **different** object with a **different** id.
- **Mutability**: Lists are mutable — you can change their contents in place without creating a new object.

---

## 4. Lecture Outline

### 0:00–0:08 — Two Names, One List
- `new_list = original_list` then compare ids → identical.

### 0:08–0:18 — Mutating Through One Alias
- `original_list[0] = 100` changes what `new_list` shows too.

### 0:18–0:28 — A Separately-Built List
- `temp_list = [100, 2, 3]` has equal content but a different id.

---

## 5. Code Demos

```python
def print_id(variable_name, variable):
    """Prints the id of the given variable."""
    print(f"id({variable_name}) = {id(variable)}")

def main():
    original_list = [1, 2, 3]
    new_list = original_list          # NOT a copy — a second name for the same list

    print_id("original_list", original_list)
    print_id("new_list", new_list)    # same id as original_list

    original_list[0] = 100            # mutate in place

    print(f"original list: {original_list}")   # [100, 2, 3]
    print(f"new list: {new_list}")             # [100, 2, 3]  <- changed too!

    print("------------------")
    temp_list = [100, 2, 3]           # a brand-new object, equal content
    print_id("original_list", original_list)
    print_id("temp_list", temp_list)  # DIFFERENT id

if __name__ == '__main__':
    main()
```

**Expected output** (ids are machine-specific; focus on which match):

```
id(original_list) = 1402...640
id(new_list) = 1402...640        <- same object
original list: [100, 2, 3]
new list: [100, 2, 3]            <- the alias sees the change
------------------
id(original_list) = 1402...640
id(temp_list) = 1402...992       <- different object, equal content
```

> 💡 **The mental model.** A variable is a label stuck onto a box (the object). `new_list = original_list` sticks a *second* label on the *same* box. Changing what's inside the box is visible no matter which label you read it through.

> 🛠️ **How to get a real copy.** If you want an independent list, copy it explicitly:
> ```python
> new_list = original_list.copy()      # or list(original_list), or original_list[:]
> ```
> Now mutating `original_list` leaves `new_list` alone. (Note: these are *shallow* copies — nested objects are still shared.)

---

## 6. Exercises

### 1. (Level 1, MCQ)
After `b = a` where `a = [1, 2]`, what is `id(a) == id(b)`?
- a) `True`
- b) `False`
- c) Depends on the values
- d) Error

<details>
<summary>Solution</summary>

**Answer:** a) `True`. `b = a` creates an alias; both names point to the same list.
</details>

---

### 2. (Level 1, Short Answer)
Why does changing `original_list[0]` also change `new_list`?

<details>
<summary>Solution</summary>

Because `new_list` is not a copy — it's a second name for the very same list object. There is only one list; both names see every change to it.
</details>

---

### 3. (Level 2, Coding)
Make `new_list` an independent copy so that mutating `original_list` does **not** affect it. Prove it.

<details>
<summary>Solution</summary>

```python
original_list = [1, 2, 3]
new_list = original_list.copy()    # independent shallow copy
original_list[0] = 100
print(original_list)   # [100, 2, 3]
print(new_list)        # [1, 2, 3]  unchanged
```
</details>

---

### 4. (Level 2, Short Answer)
`temp_list = [100, 2, 3]` has the same content as `original_list`. Will `temp_list is original_list` be `True`?

<details>
<summary>Solution</summary>

No — it will be `False`. They are two distinct objects (different ids). `temp_list == original_list` would be `True` (equal content), but `is` checks identity, not content.
</details>

---

### 5. (Level 3, Coding)
Write a function `append_item(lst, item)` that appends to the list it receives, and show that the caller's original list is modified (because the list is passed by reference).

<details>
<summary>Solution</summary>

```python
def append_item(lst, item):
    lst.append(item)        # mutates the caller's list in place

data = [1, 2]
append_item(data, 3)
print(data)   # [1, 2, 3]  — the original was changed
```
This is why passing mutable objects to functions can have side effects: the function receives the same object, not a copy.
</details>

---

## 7. Further Reading

- [Python FAQ: How do I write a function with output parameters (call by reference)?](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)
- [Python Docs: `copy` module (shallow vs deep)](https://docs.python.org/3/library/copy.html)
- [Python Docs: Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)

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
