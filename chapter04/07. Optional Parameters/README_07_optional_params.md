# ⚙️ Optional Parameters Demo

This lesson demonstrates default parameter values, required arguments, positional calls, and keyword arguments.

---

## 1. Learning Objectives

- Define default parameter values.
- Distinguish required and optional parameters.
- Call functions with positional arguments.
- Call functions with keyword arguments.
- Understand missing-argument errors.

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- **Required parameter**: A parameter that must receive a value.
- **Optional parameter**: A parameter with a default value.
- **Default value**: A value used when the caller omits the argument.
- **Positional argument**: Matched by position.
- **Keyword argument**: Matched by parameter name.

---

## 4. Lecture Outline

### 1. Define add(a, b, c=0).
### 2. Define full_opt_add(a=0, b=0, c=0).
### 3. Call functions positionally.
### 4. Call a function with keyword arguments in a different order.

---

## 5. Code Demo

```python
def add(a: int, b: int, c: int = 0) -> int:
    return a + b + c

def full_opt_add(a: int = 0, b: int = 0, c: int = 0) -> int:
    return a + b + c

def main():
    print(add(10, 20)) #30
    print(add(10))

    print(full_opt_add(1, 2, 3))
    print(full_opt_add(c = 3, a = 2, b = 1))

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output / Notes

```text
Important: print(add(10)) raises TypeError because b is required. Replace it with print(add(10, 0)) or use full_opt_add(10).
```

---

## 7. Exercises

### 1. Exercise
Which parameter is optional in add(a, b, c=0)?

<details>
<summary>Solution</summary>

Only c is optional.
</details>

---

### 2. Exercise
Why does add(10) fail?

<details>
<summary>Solution</summary>

Because the required parameter b is missing.
</details>

---

### 3. Exercise
Create multiply(a, b=1).

<details>
<summary>Solution</summary>

def multiply(a: int, b: int = 1) -> int: return a * b
</details>


---

## 8. Further Reading

- https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
- https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

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

