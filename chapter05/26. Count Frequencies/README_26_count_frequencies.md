# 🍎 Counting Frequencies in Multiple Ways

This lesson compares multiple ways to count how often each item appears in a list.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `26_count_frequencies.py` | Counts item frequencies using dictionary comprehension, loops, `.get()`, and `Counter`. |

---

## 1. Learning Objectives

- Count frequencies with a dictionary comprehension.
- Count frequencies with a manual loop.
- Use `.get()` for default counts.
- Use `collections.Counter`.
- Sort counts with `.most_common()`.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **Frequency**: The number of times an item appears.
- **Manual loop**: Updates a dictionary one item at a time.
- **`.get()`**: Gets an existing count or returns a default.
- **`Counter`**: A built-in counting helper from `collections`.

---

## 4. Code Demo

```python
from collections import Counter

my_list = ["apple", "banana", "kiwi", "apple", "banana", "kiwi", "kiwi"]

frequency_dict = {item: my_list.count(item) for item in set(my_list)}
print(frequency_dict)

counter = Counter(my_list)
print(counter.most_common())
```

---

## 5. Expected Output / Behaviour

```text
{'apple': 2, 'banana': 2, 'kiwi': 3}
[('kiwi', 3), ('apple', 2), ('banana', 2)]
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
