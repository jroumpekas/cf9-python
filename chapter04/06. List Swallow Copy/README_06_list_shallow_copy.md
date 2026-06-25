# 🪞 Shallow Copy Demo

This lesson demonstrates shallow copying with list slicing and shows why nested lists can still be shared.

---

## 1. Learning Objectives

- Create a shallow copy using [:].
- Compare objects with is.
- Understand outer list independence.
- Understand shared nested mutable objects.
- Explain why nested changes affect both lists.

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- **Shallow copy**: A new outer container with references to the same inner objects.
- **Slicing [:]**: A common way to copy the outer list.
- **is**: Checks object identity.
- **Nested mutation**: Changing an inner list in place.
- **Shared reference**: Two lists refer to the same inner object.

---

## 4. Lecture Outline

### 1. Create my_list.
### 2. Create new_list = my_list[:].
### 3. Check identity with is.
### 4. Modify top-level and nested values.

---

## 5. Code Demo

```python
my_list = [1, 2, "hello", [3, 4, 5]]

new_list = my_list[:]

print(f"Are new_list and my_List the same object: {my_list is new_list}")

new_list[0] = 100

print(my_list)
print(new_list)

new_list[3][0] = 300 

print(my_list)
print(new_list)
```

---

## 6. Expected Output / Notes

```text
my_list is new_list is False, but changing new_list[3][0] also changes my_list[3][0].
```

---

## 7. Exercises

### 1. Exercise
What does my_list[:] create?

<details>
<summary>Solution</summary>

A shallow copy.
</details>

---

### 2. Exercise
Why is my_list is new_list false?

<details>
<summary>Solution</summary>

Because the outer list is a new object.
</details>

---

### 3. Exercise
Why does the nested list change in both?

<details>
<summary>Solution</summary>

The inner list is shared.
</details>


---

## 8. Further Reading

- https://docs.python.org/3/library/copy.html
- https://docs.python.org/3/tutorial/datastructures.html

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

