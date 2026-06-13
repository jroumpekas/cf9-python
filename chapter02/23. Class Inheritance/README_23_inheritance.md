# 🧬 Inheritance, `super()`, and Access Levels (Public / Protected / Private)

This final lesson of the chapter demonstrates **inheritance** — a `Derived` class building on a `Base` class — and the three conventional access levels in Python: **public**, **protected** (`_`), and **private** (`__`). The clever twist is how name mangling keeps the parent's and child's "private" attributes completely separate.

---

## 1. Learning Objectives

- Create a subclass with `class Derived(Base):`.
- Call the parent constructor with `super().__init__()`.
- Distinguish the three access conventions: `public`, `_protected`, `__private`.
- Understand **name mangling**: `__private` becomes `_ClassName__private`.
- Explain why the child's `__private` does **not** overwrite the parent's.

---

## 2. Prerequisites

- Comfort with classes, `__init__`, and methods (lessons `20`–`22`).
- Awareness of the private `__` convention and name mangling.

---

## 3. Key Concepts

- **Inheritance**: `Derived(Base)` automatically gains all of `Base`'s attributes and methods.
- **`super().__init__()`**: Runs the parent's constructor so the inherited attributes get set up.
- **Public** (`self.public`): Accessible anywhere — `base.public`.
- **Protected** (`self._protected`): A single underscore is a *convention* meaning "internal use"; Python doesn't enforce it, but you can still read `base._protected`.
- **Private** (`self.__private`): Double underscore triggers **name mangling** — stored as `_Base__private` (in `Base`) or `_Derived__private` (in `Derived`). The two never collide.
- **Why methods see their own class's version**: A method defined in `Base` that reads `self.__private` is mangled at *definition time* to `self._Base__private`, so it always reads `Base`'s copy — even when called on a `Derived` object.

---

## 4. Lecture Outline

### 0:00–0:08 — The `Base` Class
- Three attributes (public, protected, private) plus a private method.

### 0:08–0:18 — The `Derived` Class
- `super().__init__()` then its **own** `__private`.

### 0:18–0:30 — Accessing Everything from `main`
- Reading public/protected/private through getters.

### 0:30–0:40 — The Two Separate `__private` Values
- `get_private()` (Base) vs `get_derived_private()` (Derived).

---

## 5. Code Demos

```python
class Base:
    def __init__(self):
        self.__private = "I am private"        # mangled to _Base__private
        self._protected = "I am protected"
        self.public = "I am public"

    def __private_method(self):                # mangled to _Base__private_method
        return "This is private"

    def get_private(self):
        return self.__private                  # reads _Base__private

    def call_private_method(self):
        return self.__private_method()         # calls _Base__private_method


class Derived(Base):
    def __init__(self):
        super().__init__()                     # set up Base's attributes first
        self.__private = "I am private in Derived"   # mangled to _Derived__private

    def get_derived_private(self):
        return self.__private                  # reads _Derived__private


def main():
    base = Base()
    derived = Derived()

    print(base.public)                # I am public
    print(base._protected)            # I am protected
    print(base.get_private())         # I am private
    print(base.call_private_method()) # This is private
    print("-----------------")
    print(derived.public)             # I am public
    print(derived._protected)         # I am protected
    print(derived.get_private())      # I am private          (Base's copy!)
    print(derived.get_derived_private())  # I am private in Derived

if __name__ == "__main__":
    main()
```

**Expected output:**

```
I am public
I am protected
I am private
This is private
-----------------
I am public
I am protected
I am private
I am private in Derived
```

> 💡 **The headline result: `derived.get_private()` prints `"I am private"`, not `"I am private in Derived"`.** This surprises almost everyone. Here's why: `get_private` is defined in `Base`, so its `self.__private` was mangled to `self._Base__private` at definition time. Meanwhile, `Derived.__init__` set `self._Derived__private`. The two are different attributes living side by side on the same object — so the `Base` method keeps reading the `Base` value, and `get_derived_private` (defined in `Derived`) reads the `Derived` value. Name mangling deliberately prevents a subclass from accidentally clobbering a parent's private data.

> 🔓 **Protected is a gentleman's agreement.** `base._protected` works fine from outside — the single underscore is purely a *hint* to other programmers that they shouldn't rely on it. Python does not block it.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What does `super().__init__()` do inside `Derived.__init__`?
- a) Creates a new Base object
- b) Runs `Base`'s constructor so inherited attributes are initialised
- c) Deletes the parent class
- d) Nothing

<details>
<summary>Solution</summary>

**Answer:** b) It runs the parent's constructor, setting up `public`, `_protected`, and `_Base__private` on the current object.
</details>

---

### 2. (Level 1, Short Answer)
What is the actual (mangled) attribute name behind `self.__private` inside the `Base` class?

<details>
<summary>Solution</summary>

`_Base__private`. Python prepends `_ClassName` to any `__name` defined inside a class.
</details>

---

### 3. (Level 2, Short Answer)
Why does `derived.get_private()` return `"I am private"` rather than `"I am private in Derived"`?

<details>
<summary>Solution</summary>

`get_private` is defined in `Base`, so its reference to `self.__private` is mangled to `self._Base__private`. The derived object's `__init__` set a *separate* attribute `_Derived__private`. They don't overlap, so the Base method still reads the Base value.
</details>

---

### 4. (Level 2, Coding)
From outside the class, read the derived object's private value directly (using the mangled name).

<details>
<summary>Solution</summary>

```python
derived = Derived()
print(derived._Derived__private)   # I am private in Derived
print(derived._Base__private)      # I am private
```
This proves the two private values coexist on the same object.
</details>

---

### 5. (Level 3, Coding)
Add a method `describe(self)` to `Base` that returns all three values in one string, and confirm a `Derived` object inherits it.

<details>
<summary>Solution</summary>

```python
class Base:
    def __init__(self):
        self.__private = "I am private"
        self._protected = "I am protected"
        self.public = "I am public"

    def describe(self):
        return f"{self.public} | {self._protected} | {self.__private}"

class Derived(Base):
    pass

print(Derived().describe())
# I am public | I am protected | I am private
```
`Derived` inherits `describe` without redefining it.
</details>

---

## 7. Further Reading

- [Python Tutorial: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Python Docs: `super`](https://docs.python.org/3/library/functions.html#super)
- [Python Tutorial: Private Variables & Name Mangling](https://docs.python.org/3/tutorial/classes.html#private-variables)
- [PEP 8: Naming Conventions](https://peps.python.org/pep-0008/#descriptive-naming-styles)

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
