# 🔭 Function Scope Demo

This lesson shows how local function parameters work and why reassigning a parameter does not change the original global variable.

---

## 1. Learning Objectives

- Understand global and local variables.
- See that parameters are local names.
- Reassign a parameter inside a function.
- Return a calculated value.
- Observe that the original global variable remains unchanged.

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- **Global variable**: A variable defined outside a function.
- **Local variable**: A variable defined inside a function.
- **Parameter**: A local name that receives an argument value.
- **Scope**: The part of the program where a variable is visible.
- **Reassignment**: Binding a name to a new value.

---

## 4. Lecture Outline

### 1. Define global variables a and b.
### 2. Pass them into add_numbers(x, y).
### 3. Reassign x locally to 100.
### 4. Print the result and the original a.

---

## 5. Code Demo

```python
a = 10
b = 20

def add_numbers(x: int, y: int) -> int:
    x = 100
    return x + y

def main():
    result = add_numbers(a, b)

    print(result)
    print(f"a = {a}")

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output / Notes

```text
120
a = 10
```

---

## 7. Exercises

### 1. Exercise
Why is the result 120?

<details>
<summary>Solution</summary>

Inside the function, x becomes 100, so the function returns 100 + 20.
</details>

---

### 2. Exercise
Why does a remain 10?

<details>
<summary>Solution</summary>

Because x is local to the function and does not reassign the global name a.
</details>

---

### 3. Exercise
Rewrite add_numbers without changing x.

<details>
<summary>Solution</summary>

return x + y
</details>


---

## 8. Further Reading

- https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- https://docs.python.org/3/reference/executionmodel.html

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

