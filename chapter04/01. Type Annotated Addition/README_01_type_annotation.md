# 🏷️ Type Annotations & Function Documentation

This lesson demonstrates how to use type annotations, docstrings, runtime type checking, and Python documentation helpers.

---

## 1. Learning Objectives

- Use type annotations with int, float, and union types.
- Write and read function docstrings.
- Validate arguments at runtime with isinstance().
- Raise and handle TypeError.
- Inspect __annotations__, __doc__, and help().

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- **Type annotations**: Hints that describe the expected types of parameters and return values.
- **Union type**: float | int means that a value may be either a float or an integer.
- **Docstring**: Documentation written inside a function.
- **Runtime validation**: Actual code that checks values while the program runs.
- **Exception handling**: Using try / except to handle errors safely.

---

## 4. Lecture Outline

### 1. Define my_add(a, b) with type annotations.
### 2. Check that both arguments are numeric.
### 3. Raise TypeError for invalid inputs.
### 4. Print annotations, docs, and help output.

---

## 5. Code Demo

```python
def my_add(a: float | int, b: float | int) -> float | int:
    """
    Add two numbers and returns the result.
 
    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add.
   
    Returns:
        int | float: The sum of a and b.
 
    Raises:
        TypeError: If either a or b is not integer or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both a and b must be integers or floats")
   
    return a + b

def main():
    print(my_add(10, 20))
    print(my_add(5, 7.1))

    try:
        print(my_add("Hello", "CF9"))
    except TypeError as e:
        print(e)

    print(f"Annotations: {my_add.__annotations__}")
    print(f"Docs: {my_add.__doc__}")


print("----------------------------")
help(my_add)    

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output / Notes

```text
30
12.1
Both a and b must be integers or floats
Annotations: {...}
Docs: ...
```

---

## 7. Exercises

### 1. Exercise
What does a type annotation do?

<details>
<summary>Solution</summary>

It gives type hints to developers, editors, and type checkers. It does not automatically enforce types at runtime.
</details>

---

### 2. Exercise
Why does my_add("Hello", "CF9") raise TypeError?

<details>
<summary>Solution</summary>

Because the function explicitly checks that both arguments are int or float.
</details>

---

### 3. Exercise
Add a check that rejects bool values.

<details>
<summary>Solution</summary>

Use: if isinstance(a, bool) or isinstance(b, bool): raise TypeError("Booleans are not allowed")
</details>


---

## 8. Further Reading

- https://docs.python.org/3/library/typing.html
- https://docs.python.org/3/library/functions.html#isinstance
- https://docs.python.org/3/library/functions.html#help

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

