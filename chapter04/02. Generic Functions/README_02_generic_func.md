# 🧬 Generic Functions with TypeVar

This lesson introduces generic functions with TypeVar, Sequence, Any, List, and Optional.

---

## 1. Learning Objectives

- Understand what TypeVar represents.
- Write functions that preserve input/output type relationships.
- Use Sequence[T] for generic sequence parameters.
- Raise ValueError for empty sequences.
- Use Optional[str] for values that may be None.

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- **TypeVar**: A placeholder for a type used in generic functions.
- **Sequence[T]**: A read-only style sequence containing values of type T.
- **Any**: Allows values of any type.
- **Optional[str]**: A value that can be str or None.
- **Truthy / falsy**: Values that behave like True or False in conditions.

---

## 4. Lecture Outline

### 1. Import typing helpers.
### 2. Create T = TypeVar("T").
### 3. Build first() and last() generic helpers.
### 4. Count truthy values and handle optional strings.

---

## 5. Code Demo

```python
from typing import Sequence, TypeVar, List, Any, Optional
 
# Declare Generic Type Variable
T = TypeVar('T')
 
# More descriptive TypeVar names based on the intended type constraints
Number = TypeVar('Number', int, float)
 
def first(seq: Sequence[T]) -> T:
    if not seq:
        raise ValueError("Sequence is empty")
    return seq[0]
 
 
def last(seq: Sequence[T]) -> T:
    if not seq:
        raise ValueError("Sequence is empty")
    return seq[-1]
 
def count_truthy(elements: List[Any]) -> int:
    return sum(1 for element in elements if element)
 
 
def len_str(s: Optional[str] = None) -> int:
    return len(s) if s is not None else 0
    # return 0 if None else len(s)
 
def main():
    # [1, "hello", 0, False, None, 100, 3.14]
    pass
 
if __name__ == "__main__":
    main()
```

---

## 6. Expected Output / Notes

```text
The main() function currently contains pass, so no output appears unless you add test calls.
```

---

## 7. Exercises

### 1. Exercise
What does first([10, 20, 30]) return?

<details>
<summary>Solution</summary>

It returns 10.
</details>

---

### 2. Exercise
Why do first() and last() check if not seq?

<details>
<summary>Solution</summary>

Because empty sequences have no first or last item.
</details>

---

### 3. Exercise
Create second(seq).

<details>
<summary>Solution</summary>

Check len(seq) < 2 and then return seq[1].
</details>


---

## 8. Further Reading

- https://docs.python.org/3/library/typing.html#typing.TypeVar
- https://docs.python.org/3/library/typing.html#typing.Sequence
- https://docs.python.org/3/library/typing.html#typing.Optional

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

---

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

---

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>

