# 🔁 Iterators, `iter()`, `next()`, and `StopIteration`

This lesson group contains two related scripts about Python's iterator protocol.

The first script demonstrates how built-in iterators work with `iter()` and `next()`.  
The second script implements a custom iterator class using `__iter__()` and `__next__()`.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `12_deep_understanding.py` | Manual iteration over a list using `iter()`, `next()`, and `StopIteration`. |
| `12_simple_iterator.py` | Custom iterator class that implements the iterator protocol. |

---

## 1. Learning Objectives

By studying these examples, you will be able to:

- Understand what an iterator is.
- Convert an iterable into an iterator using `iter()`.
- Get values one by one using `next()`.
- Understand when and why `StopIteration` is raised.
- Build a custom iterator class.
- Implement `__iter__()` and `__next__()`.
- Understand why an exhausted iterator does not restart automatically.

---

## 2. Prerequisites

- Lists.
- Loops.
- Classes.
- Methods.
- Exceptions.
- `try / except`.

---

## 3. Key Concepts

### Iterable

An **iterable** is an object that can be looped over.

Examples:

```python
numbers = [10, 20, 30, 40, 50]
```

A list is iterable.

---

### Iterator

An **iterator** is an object that returns values one at a time.

```python
iterator = iter(numbers)
```

The iterator remembers its current position.

---

### `next()`

The `next()` function asks the iterator for the next value.

```python
item = next(iterator)
```

---

### `StopIteration`

When there are no more items, Python raises `StopIteration`.

```python
except StopIteration:
    print("No more items...")
```

A `for` loop handles this automatically behind the scenes.

---

### Iterator Protocol

A custom iterator needs two methods:

```python
def __iter__(self):
    return self

def __next__(self):
    ...
```

- `__iter__()` returns the iterator object.
- `__next__()` returns the next item or raises `StopIteration`.

---

## 4. Lecture Outline

### 0:00–0:10 — Built-in Iterators
- Start with a list of numbers.
- Convert the list to an iterator using `iter()`.

### 0:10–0:22 — Manual Iteration
- Use `next()` inside a `while True` loop.
- Catch `StopIteration`.

### 0:22–0:35 — Custom Iterator
- Create a class called `SimpleIterator`.

### 0:35–0:45 — Iterator Exhaustion
- Show that after the first loop, the same iterator is exhausted.

---

## 5. Code Demo 1 — Manual Iteration

```python
numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

while True:
    try:
        print("Calling next()...")
        item = next(iterator)
        print("Got item:", item)
    except StopIteration:
        print("No more items... StopIteration raised.")
        break
```

---

## 6. Expected Output 1

```text
Calling next()...
Got item: 10
Calling next()...
Got item: 20
Calling next()...
Got item: 30
Calling next()...
Got item: 40
Calling next()...
Got item: 50
Calling next()...
No more items... StopIteration raised.
```

---

## 7. Code Demo 2 — Custom Iterator

```python
class SimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

def main():
    numbers = [10, 20, 30, 40, 50]

    iterator = SimpleIterator(numbers)

    for item in iterator:
        print(item, end=" ")

    print("--------------------")

    for item in iterator:
        print(item, end=" ")

    print("--------------------")
```

---

## 8. Expected Output 2

```text
10 20 30 40 50 --------------------
--------------------
```

The second loop prints nothing because the iterator has already been consumed.

---

## 9. Why the Second Loop Prints Nothing

The iterator stores its current position in:

```python
self.index
```

After the first loop finishes, `self.index` equals the length of the list.

So when the second loop starts, `__next__()` immediately raises:

```python
StopIteration
```

To loop again, create a new iterator:

```python
iterator = SimpleIterator(numbers)
```

---

## 10. `for` Loop Behind the Scenes

This:

```python
for item in numbers:
    print(item)
```

roughly works like this:

```python
iterator = iter(numbers)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```

So `for` loops are a cleaner way to work with iterators.

---

## 11. Exercises

### 1. Level 1 — MCQ

What does `iter(numbers)` return?

- a) A copy of the list.
- b) An iterator object.
- c) The first number.
- d) The length of the list.

<details>
<summary>Solution</summary>

**Answer:** b) An iterator object.
</details>

---

### 2. Level 1 — Short Answer

What happens when there are no more items?

<details>
<summary>Solution</summary>

The iterator raises `StopIteration`.
</details>

---

### 3. Level 2 — Coding

Create a new iterator after the first loop so the numbers print twice.

<details>
<summary>Solution</summary>

```python
iterator = SimpleIterator(numbers)

for item in iterator:
    print(item, end=" ")

print()

iterator = SimpleIterator(numbers)

for item in iterator:
    print(item, end=" ")
```
</details>

---

### 4. Level 2 — Coding

Modify `SimpleIterator` so it starts from the last item and moves backwards.

<details>
<summary>Solution</summary>

```python
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            result = self.data[self.index]
            self.index -= 1
            return result
        raise StopIteration
```
</details>

---

### 5. Level 3 — Challenge

Create an iterator that returns only even numbers.

<details>
<summary>Solution</summary>

```python
class EvenIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1

            if result % 2 == 0:
                return result

        raise StopIteration
```
</details>

---

## 12. Further Reading

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

🔗 *Note: These are Python scripts and require a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
