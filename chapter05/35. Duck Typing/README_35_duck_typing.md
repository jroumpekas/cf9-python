# 🦆 Duck Typing and Polymorphism

This lesson demonstrates Python’s duck typing approach: behaviour matters more than exact inheritance type.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `35_duck_typing.py` | Demonstrates duck typing with classes that provide a `drive()` method. |

---

## 1. Learning Objectives

- Understand duck typing.
- Use polymorphic behaviour through a common method.
- Compare inheritance and behaviour-based design.
- Handle missing implementations.
- Use a function that accepts different object types.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Duck typing**: If an object has the needed method, it can be used.
- **Polymorphism**: Different objects respond to the same method call.
- **Inheritance**: `Car` and `Bicycle` inherit from `Vehicle`.
- **Behaviour-based design**: `Hoverboard` works because it has `drive()`.

---

## 4. Code Demo

```python
class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclasses should implement this!")

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Hoverboard:
    def drive(self):
        print("Hovering on a hoverboard")

def drive_vehicle(vehicle):
    try:
        vehicle.drive()
    except NotImplementedError:
        print(f"{vehicle.__class__.__name__} can't drive.")
```

---

## 5. Expected Output / Behaviour

```text
Driving a car
Riding a bicycle
Hovering on a hoverboard
Boat can't drive.
```


---

## 6. Exercises

### 1. Level 1 — Short Answer
Explain the main idea of this script in your own words.

<details>
<summary>Solution</summary>

The script demonstrates one focused Python concept through a small runnable example.
</details>

---

### 2. Level 2 — Coding
Add one extra test case to the script and run it again.

<details>
<summary>Solution</summary>

Add one more function call or one more input example inside `main()`.
</details>

---

## 7. Further Reading

- [Python Docs: Tutorial](https://docs.python.org/3/tutorial/)
- [Python Docs: Standard Library](https://docs.python.org/3/library/)

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
