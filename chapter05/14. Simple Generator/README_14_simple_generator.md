# ⚙️ Simple Generator with `yield`

This lesson demonstrates how to create a simple Python **generator function** using `yield`.

A generator is a special kind of iterator. It produces values one at a time and remembers where it stopped between calls.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `14_simple_generator.py` | Simple generator function that yields three values step by step. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Understand what `yield` does.
- Create a generator function.
- Call a generator function and receive a generator object.
- Use `next()` to resume generator execution.
- Understand how generator state is preserved.
- Compare generators with custom iterator classes.

---

## 2. Prerequisites

- Functions.
- `print()`.
- `next()`.
- Basic iterator knowledge.

---

## 3. Key Concepts

### Generator Function

A function becomes a generator function when it contains `yield`.

```python
def simple_generator():
    yield 1
```

Calling this function does **not** execute it immediately.  
It returns a generator object.

---

### `yield`

The `yield` keyword:

- returns a value to the caller,
- pauses the function,
- saves the local state,
- resumes from the same point on the next `next()` call.

---

### Generator Object

When you call a generator function:

```python
gen = simple_generator()
```

you get a generator object.

The code inside the function starts only when you call:

```python
next(gen)
```

---

## 4. Lecture Outline

### 0:00–0:10 — What is `yield`?
- Explain that `yield` pauses and resumes a function.

### 0:10–0:20 — Generator Function
- Define `simple_generator()`.

### 0:20–0:32 — Manual Calls with `next()`
- Call `next(gen)` three times.

### 0:32–0:42 — Preserved State
- Show that the function continues after the previous `yield`.

---

## 5. Code Demo

```python
def simple_generator():
    print("First value")
    yield 1

    print("Second value")
    yield 2

    print("Third value")
    yield 3

def main():
    gen = simple_generator()

    print(next(gen))
    print(next(gen))
    print(next(gen))

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output

```text
First value
1
Second value
2
Third value
3
```

Each call to `next(gen)` runs the generator until the next `yield`.

---

## 7. What Happens Step by Step

### First call

```python
print(next(gen))
```

The generator starts executing:

```python
print("First value")
yield 1
```

Output:

```text
First value
1
```

---

### Second call

```python
print(next(gen))
```

The generator resumes after the first `yield`:

```python
print("Second value")
yield 2
```

Output:

```text
Second value
2
```

---

### Third call

```python
print(next(gen))
```

The generator resumes after the second `yield`:

```python
print("Third value")
yield 3
```

Output:

```text
Third value
3
```

---

## 8. What Happens After the Last `yield`

If you call `next(gen)` a fourth time:

```python
print(next(gen))
```

Python raises:

```text
StopIteration
```

This means the generator has no more values to produce.

---

## 9. Generator vs Iterator Class

| Generator | Custom Iterator Class |
|----------|------------------------|
| Uses `yield` | Uses `__iter__()` and `__next__()` |
| Shorter syntax | More explicit control |
| Automatically remembers state | You manually store state with attributes |
| Great for simple sequences | Better for complex iterator behavior |

---

## 10. Suggested `for` Loop Version

Generators can also be used directly inside `for` loops:

```python
def main():
    for value in simple_generator():
        print(value)
```

Output:

```text
First value
1
Second value
2
Third value
3
```

The `for` loop automatically handles `StopIteration`.

---

## 11. Exercises

### 1. Level 1 — MCQ

What keyword turns a function into a generator?

- a) `return`
- b) `break`
- c) `yield`
- d) `continue`

<details>
<summary>Solution</summary>

**Answer:** c) `yield`.
</details>

---

### 2. Level 1 — Short Answer

Does a generator function execute immediately when called?

<details>
<summary>Solution</summary>

No. Calling a generator function returns a generator object. Execution starts when `next()` is called.
</details>

---

### 3. Level 2 — Coding

Add a fourth yielded value.

<details>
<summary>Solution</summary>

```python
def simple_generator():
    print("First value")
    yield 1

    print("Second value")
    yield 2

    print("Third value")
    yield 3

    print("Fourth value")
    yield 4
```
</details>

---

### 4. Level 2 — Coding

Create a generator that yields numbers from `1` to `5`.

<details>
<summary>Solution</summary>

```python
def numbers_generator():
    for number in range(1, 6):
        yield number
```
</details>

---

### 5. Level 3 — Challenge

Create a generator that yields factorial values from `0!` to `n!`.

<details>
<summary>Solution</summary>

```python
def factorial_generator(n):
    result = 1

    for order in range(0, n + 1):
        if order == 0:
            yield 1
        else:
            result *= order
            yield result
```
</details>

---

## 12. Further Reading

- [Python Docs: yield expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions)
- [Python Docs: Generator Types](https://docs.python.org/3/library/stdtypes.html#generator-types)
- [Python Docs: Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)

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
