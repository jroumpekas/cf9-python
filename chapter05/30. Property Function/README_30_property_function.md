# 👤 `property()` Function Demo

This lesson demonstrates encapsulation using Python’s built-in `property()` function.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `30_property_function.py` | Manages a `name` attribute with getter, setter, deleter, and `property()`. |

---

## 1. Learning Objectives

- Create getter, setter, and deleter methods.
- Use `property()` to expose a managed attribute.
- Validate property assignment.
- Delete an attribute.
- Add dynamic instance attributes.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Getter**: Controls reading the value.
- **Setter**: Controls assigning a new value.
- **Deleter**: Controls deleting the value.
- **Dynamic attributes**: Adds `friends` directly to the instance.

---

## 4. Code Demo

```python
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name if hasattr(self, "_name") else "Name attribute has been deleted"

    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name, "This is the name property")
```

---

## 5. Expected Output / Behaviour

```text
Getting name: John
Setting name: Getting name: Jane
Deleting name
Name attribute has been deleted
Printing friends:
 - Bob
 - Alice
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
