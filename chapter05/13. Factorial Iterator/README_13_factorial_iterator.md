# 🔢 Factorial Iterator Demo

This lesson demonstrates how to build a **custom iterator class** that generates factorial values from `0!` up to `n!`.

The example uses Python's iterator protocol with `__iter__()` and `__next__()`, and it also shows how `next()` manually consumes values from an iterator.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `13_facto_iter_demo.py` | Custom iterator class that produces factorial values one by one. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Understand how a custom iterator works.
- Implement `__iter__()` and `__next__()`.
- Use `next()` manually.
- Raise `StopIteration` when the iterator is exhausted.
- Handle invalid input with `ValueError`.
- Generate factorial values step by step.
- Understand that an iterator remembers its current state.

---

## 2. Prerequisites

- Classes.
- Methods.
- Basic factorial logic.
- Exceptions.
- `next()`.
- Iterator protocol.

---

## 3. Key Concepts

### Iterator Protocol

A Python iterator must implement:

```python
def __iter__(self):
    return self

def __next__(self):
    ...
```

The `__iter__()` method returns the iterator object itself.  
The `__next__()` method returns the next value or raises `StopIteration`.

---

### Factorial Logic

Factorial means multiplying all positive integers from `1` up to a number.

```text
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

---

### Iterator State

The iterator stores its current progress using instance variables:

```python
self.result = 1
self.order = 0
```

Each call to `next()` updates the internal state and returns the next factorial value.

---

## 4. Lecture Outline

### 0:00–0:10 — Class Initialization
- Define `FactoIterator`.
- Validate that `n` is not negative.
- Initialize `result` and `order`.

### 0:10–0:22 — Iterator Protocol
- Implement `__iter__()` and `__next__()`.

### 0:22–0:35 — Special Case for `0!`
- Return `1` when `order == 0`.

### 0:35–0:45 — Manual Iteration
- Use `next(facto_iter)` to consume values one by one.

---

## 5. Code Demo

```python
class FactoIterator:
    def __init__(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        self.n = n
        self.result = 1
        self.order = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.order > self.n:
            raise StopIteration

        if self.order == 0:
            self.order += 1
            return 1

        self.result *= self.order
        self.order += 1
        return self.result

def main():
    facto_iter = FactoIterator(5)

    a = next(facto_iter)
    print(f"a = {a}")

    b = next(facto_iter)
    print(f"b = {b}")

    print("-----------------")

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output

```text
a = 1
b = 1
-----------------
```

The first `next()` returns `0!`, which is `1`.  
The second `next()` returns `1!`, which is also `1`.

---

## 7. Suggested Full Iteration Version

To print all factorial values from `0!` to `5!`, you can add a `for` loop:

```python
def main():
    facto_iter = FactoIterator(5)

    for factorial in facto_iter:
        print(factorial)
```

Expected output:

```text
1
1
2
6
24
120
```

---

## 8. Important Note About Iterator Consumption

If you call:

```python
a = next(facto_iter)
b = next(facto_iter)
```

and then run:

```python
for factorial in facto_iter:
    print(factorial)
```

the `for` loop will continue from where the iterator stopped.  
It will not restart from the beginning.

So this:

```python
facto_iter = FactoIterator(5)

print(next(facto_iter))
print(next(facto_iter))

for factorial in facto_iter:
    print(factorial)
```

prints:

```text
1
1
2
6
24
120
```

The iterator remembers its state.

---

## 9. Exercises

### 1. Level 1 — MCQ

What does `__next__()` do?

- a) It creates a new class.
- b) It returns the next value from the iterator.
- c) It deletes the iterator.
- d) It converts the iterator to a list.

<details>
<summary>Solution</summary>

**Answer:** b) It returns the next value from the iterator.
</details>

---

### 2. Level 1 — Short Answer

Why is `0!` equal to `1`?

<details>
<summary>Solution</summary>

By mathematical definition, the factorial of zero is `1`. It also keeps factorial formulas consistent.
</details>

---

### 3. Level 2 — Coding

Modify `main()` to print all factorial values from `0!` to `7!`.

<details>
<summary>Solution</summary>

```python
def main():
    facto_iter = FactoIterator(7)

    for factorial in facto_iter:
        print(factorial)
```
</details>

---

### 4. Level 2 — Short Answer

Why does the iterator raise `StopIteration`?

<details>
<summary>Solution</summary>

It raises `StopIteration` when `self.order > self.n`, meaning there are no more factorial values to return.
</details>

---

### 5. Level 3 — Challenge

Modify the iterator so it returns both the order and the factorial value, for example:

```text
0! = 1
1! = 1
2! = 2
```

<details>
<summary>Solution</summary>

```python
def __next__(self):
    if self.order > self.n:
        raise StopIteration

    current_order = self.order

    if self.order == 0:
        self.order += 1
        return current_order, 1

    self.result *= self.order
    self.order += 1
    return current_order, self.result
```
</details>

---

## 10. Further Reading

- [Python Docs: Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)
- [Python Docs: `iter`](https://docs.python.org/3/library/functions.html#iter)
- [Python Docs: `next`](https://docs.python.org/3/library/functions.html#next)

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
