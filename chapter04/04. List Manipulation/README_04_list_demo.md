# 📋 List Mutation Demo

This lesson demonstrates that lists are mutable and can be changed inside a function.

---

## 1. Learning Objectives

- Understand that lists are mutable.
- Pass a list into a function.
- Modify the list with append().
- Use List[Any] for mixed-type lists.
- Iterate through a list with for.

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- **Mutable object**: An object that can be changed in place.
- **List**: A mutable ordered collection.
- **append()**: Adds an element to the end of a list.
- **Any**: A type hint for values of any type.
- **Side effect**: A function changes an object outside its local scope.

---

## 4. Lecture Outline

### 1. Create a mixed list.
### 2. Define append_to_list().
### 3. Append CF9 friends.
### 4. Print every item in the modified list.

---

## 5. Code Demo

```python
from typing import List, Any

my_list = [1, 2, "hello", [3,4,5]]

def append_to_list(li: List[Any], element: Any) -> None:
    li.append(element)

append_to_list(my_list, 'CF9 friends')


for item in my_list:
    print(item, end=", ")
```

---

## 6. Expected Output / Notes

```text
1, 2, hello, [3, 4, 5], CF9 friends,
```

---

## 7. Exercises

### 1. Exercise
What does append() do?

<details>
<summary>Solution</summary>

It adds an item to the end of the list.
</details>

---

### 2. Exercise
Why does my_list change?

<details>
<summary>Solution</summary>

The function receives a reference to the same list object.
</details>

---

### 3. Exercise
Create remove_last(li).

<details>
<summary>Solution</summary>

Use li.pop().
</details>


---

## 8. Further Reading

- https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- https://docs.python.org/3/library/typing.html#typing.Any

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

