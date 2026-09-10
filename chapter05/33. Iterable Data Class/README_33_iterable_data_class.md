# 📚 Iterable Data Collection Class

This lesson shows how Python special methods make a custom class behave like a built-in collection.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `33_iterable_data_class.py` | Makes a custom collection iterable, indexable, sliceable, unpackable, and sized. |

---

## 1. Learning Objectives

- Implement `__iter__()`.
- Implement `__getitem__()`.
- Implement `__len__()`.
- Implement `__repr__()`.
- Support iteration, indexing, slicing, and unpacking.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **`__iter__()`**: Allows use in a `for` loop.
- **`__getitem__()`**: Allows indexing and slicing.
- **`__len__()`**: Allows `len(collection)`.
- **`__repr__()`**: Provides a readable representation.

---

## 4. Code Demo

```python
class DataCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"DataCollection({self.data})"
```

---

## 5. Expected Output / Behaviour

```text
DataCollection object: DataCollection([1, 2, 3, 4])
Iterating over collection:
1
2
3
4
Unpacked values: 1 2 3 4
Slice of collection: [2, 3]
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
