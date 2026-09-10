# 📄 File Operations CRUD Demo

This lesson demonstrates basic file handling and CRUD operations using `open()`, `with`, and the `os` module.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `36_file_operations.py` | Performs create, read, update, and delete operations on a text file. |

---

## 1. Learning Objectives

- Check if a file exists with `os.path.isfile()`.
- Create a file with write mode.
- Read file contents.
- Append content to a file.
- Delete a file with `os.remove()`.
- Handle file errors safely.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **File CRUD**: Create, read, update, and delete operations.
- **`with open()`**: Safely opens and closes files.
- **File modes**: `w` writes, `a` appends, and `r` reads.
- **`os.path.isfile()`**: Checks whether a path points to a valid file.
- **Exceptions**: Handles file-related errors gracefully.

---

## 4. Code Demo

```python
import os

def create_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

def update_file(file_path, content):
    if os.path.isfile(file_path):
        with open(file_path, "a") as f:
            f.write(content)

def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
```

---

## 5. Expected Output / Behaviour

```text
Creating 'example.txt':
File 'example.txt' created successfully with content.
Reading 'example.txt':
Contents: This is the initial content of the file.
Updating 'example.txt':
File 'example.txt' updated successfully with new content.
Deleting 'example.txt':
File 'example.txt' deleted successfully.
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
