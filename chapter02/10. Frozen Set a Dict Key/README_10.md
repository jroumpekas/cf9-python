# 📂 Python Dictionary Operations Demonstration 🔄

Welcome to the Python Dictionary Operations Demonstration! This script provides an example of using Python dictionaries with diverse key-value pairs, including immutable keys and nested data structures. It’s a great starting point for understanding Python’s flexible and powerful dictionary type.

## Script Overview 📘

The script demonstrates:
- Creating a dictionary with various types of keys and values.
- Using immutable objects (like `frozenset`) as dictionary keys.
- Representing complex data with nested structures.

### 💻 Script Code

```python
# Define a dictionary with diverse key-value pairs
sym = {
    frozenset({1, 2, 3}): "Hello",  # Immutable frozenset as a key
    "key1": "value1",  # String key with string value
    "key2": 10,  # String key with integer value
    3: [1, 2, 3],  # Integer key with list value
    4: {1: "one", 2: "two"}  # Integer key with nested dictionary as value
}

# Print the entire dictionary
print(sym)
```

## Key Features 🌟

- **Diverse Key-Value Pairs**: Learn how dictionaries support keys and values of various types.
- **Immutable Keys**: Understand the use of immutable objects, such as `frozenset`, as dictionary keys.
- **Nested Structures**: Explore how to store nested data structures like lists and dictionaries as values in a dictionary.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `10_dictionary_operations_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `10_dictionary_operations_demo.py`.
5. Run the script with the command: `python 10_dictionary_operations_demo.py`.

## Usage Example 📋

Executing the script demonstrates the creation and usage of a Python dictionary with diverse key-value pairs. The output showcases the dictionary’s contents, highlighting its flexibility and support for complex data types.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Dimitris Roumpekas - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*
---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a> (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>