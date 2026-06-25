# 🧩 List Duplication & Nested References

This lesson shows what happens when a list containing another list is duplicated with the * operator.

---

## 1. Learning Objectives

- Duplicate a list with *.
- Use id() to inspect object identity.
- Understand repeated references to nested lists.
- Compare top-level reassignment with nested mutation.
- Recognize shallow-copy-like behavior.

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- **List duplication**: my_list * 2 repeats the elements.
- **Nested list**: A list stored inside another list.
- **Reference**: A pointer-like relationship between a name/container and an object.
- **Mutable nested object**: An inner list that can be modified in place.
- **Shared object**: Two positions can refer to the same inner list.

---

## 4. Lecture Outline

### 1. Print ids of original list items.
### 2. Create new_list = my_list * 2.
### 3. Change a top-level item.
### 4. Change an item inside the nested list.

---

## 5. Code Demo

```python
my_list = [1, 2, "hello", [3, 4, 5]]

print("At the start")
for item in my_list:
    print(f"{item} : {id(item)}")

# Create a new list by repeating the original list twice
new_list = my_list * 2
print(f"New list: {new_list}")
print("--------------")

new_list[0] = 100
print(f"Duplicated list: {new_list}")

new_list[3][0] = 300
print(f"Modifieded list: {new_list}")
```

---

## 6. Expected Output / Notes

```text
Both appearances of the nested list show [300, 4, 5] after new_list[3][0] = 300.
```

---

## 7. Exercises

### 1. Exercise
What does my_list * 2 do?

<details>
<summary>Solution</summary>

It repeats the list elements twice.
</details>

---

### 2. Exercise
Why do both nested lists change?

<details>
<summary>Solution</summary>

They point to the same inner list object.
</details>

---

### 3. Exercise
How do you avoid shared nested lists?

<details>
<summary>Solution</summary>

Use copy.deepcopy() when you need fully independent nested objects.
</details>


---

## 8. Further Reading

- https://docs.python.org/3/tutorial/datastructures.html
- https://docs.python.org/3/library/copy.html

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

