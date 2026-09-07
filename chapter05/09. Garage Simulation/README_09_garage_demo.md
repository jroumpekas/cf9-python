# 🚗 Garage Simulation with `deque` and `match/case`

This lesson demonstrates a small menu-driven garage simulation using Python's `collections.deque`.

The garage behaves like a queue: cars enter at the end and leave from the front.

---

## 📁 File Included

| File | Description |
|------|-------------|
| `09_garage_demo.py` | Menu-driven garage simulation using `deque`, functions, input validation, and `match/case`. |

---

## 1. Learning Objectives

By studying this example, you will be able to:

- Use `deque` from the `collections` module.
- Add items with `.append()`.
- Remove items with `.popleft()`.
- Build a menu-driven terminal program.
- Use `match/case` for menu choices.
- Validate numeric user input with `try / except`.
- Split program logic into reusable functions.

---

## 2. Prerequisites

- Lists or collections.
- Functions.
- Loops.
- `input()`.
- `try / except`.
- Basic `match/case`.

---

## 3. Key Concepts

### `deque`

A `deque` is a double-ended queue from Python's `collections` module.

```python
from collections import deque
```

It allows efficient adding and removing from both ends.

---

### Queue Behaviour

This garage works like a queue:

- cars enter at the back,
- cars leave from the front.

```python
garage.append(car_name)
garage.popleft()
```

---

### Menu Loop

The program runs inside a `while True` loop until the user chooses to exit.

```python
while True:
    ...
```

---

### `match/case`

The user's choice is handled with pattern matching.

```python
match choice:
    case 1:
        add_car_to_garage(...)
    case 2:
        remove_car_from_garage(...)
```

---

## 4. Lecture Outline

### 0:00–0:10 — Garage Data Structure
- Create a `deque` to represent the garage.

### 0:10–0:22 — Add and Remove Cars
- Use `.append()` and `.popleft()`.

### 0:22–0:35 — Menu System
- Read user input and handle invalid choices.

### 0:35–0:48 — Program Structure
- Split logic into `display`, `add`, `remove`, and `main`.

---

## 5. Code Demo

```python
from collections import deque

def display_garage(garage: deque) -> None:
    if garage:
        print("\nCurrent cars in the garage:")
        for i, car in enumerate(garage, 1):
            print(f"{i}. {car}")
    else:
        print("\nThe garage is empty.")

def add_car_to_garage(garage: deque, max_capacity: int) -> None:
    if len(garage) < max_capacity:
        car_name = input("Enter the name or ID of the car: ")
        garage.append(car_name)
        print(f"{car_name} has entered the garage.")
    else:
        print("The garage is full! Cannot add more cars.")

def remove_car_from_garage(garage: deque) -> None:
    if garage:
        car_left = garage.popleft()
        print(f"{car_left} has left the garage.")
    else:
        print("The garage is empty! No cars to remove.")
```

---

## 6. Example Program Flow

```text
Options:
1. Add a car to the garage
2. Remove the first car from the garage
3. Display the garage state
4. Exit
Select an option (1-4): 1
Enter the name or ID of the car: ABC-123
ABC-123 has entered the garage.
```

Then if the user displays the garage:

```text
Current cars in the garage:
1. ABC-123
```

---

## 7. Why `deque` Is a Good Fit

A normal list can also be used, but removing from the front with `pop(0)` is inefficient for large lists.

With `deque`, removing from the front is designed to be efficient:

```python
garage.popleft()
```

This makes `deque` a better choice for queue-like structures.

---

## 8. Exercises

### 1. Level 1 — MCQ

Which method removes the first car from the garage?

- a) `.append()`
- b) `.remove_last()`
- c) `.popleft()`
- d) `.clear_first()`

<details>
<summary>Solution</summary>

**Answer:** c) `.popleft()`
</details>

---

### 2. Level 1 — Short Answer

Why does the garage have a `max_capacity`?

<details>
<summary>Solution</summary>

To prevent adding more cars than the garage can hold.
</details>

---

### 3. Level 2 — Coding

Change the garage capacity from `5` to `3`.

<details>
<summary>Solution</summary>

```python
max_capacity = 3
```
</details>

---

### 4. Level 2 — Coding

Add an option to clear the whole garage.

<details>
<summary>Solution</summary>

```python
def clear_garage(garage: deque) -> None:
    garage.clear()
    print("Garage cleared.")
```

Then add it to the menu and `match/case`.
</details>

---

### 5. Level 3 — Challenge

Add timestamps when a car enters and leaves the garage.

<details>
<summary>Solution</summary>

You can import `datetime` and print the current time when adding or removing a car.

```python
from datetime import datetime

print(f"{car_name} entered at {datetime.now().isoformat()}")
```
</details>

---

## 9. Further Reading

- [Python Docs: collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
- [Python Docs: match statement](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)

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
