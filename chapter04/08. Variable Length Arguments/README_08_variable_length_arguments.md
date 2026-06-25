# 🧮 Variable-Length Arguments with *args

This lesson demonstrates how to use *args to accept any number of positional arguments.

---

## 1. Learning Objectives

- Understand what *args collects.
- Calculate a sum with sum().
- Calculate an average with sum() and len().
- Handle the no-arguments case safely.
- Unpack a list into function arguments.

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- ***args**: Collects extra positional arguments into a tuple.
- **Argument unpacking**: Uses *list_name to pass list items as separate arguments.
- **sum()**: Adds numeric values.
- **len()**: Counts items.
- **Guard clause**: Handles a special case early.

---

## 4. Lecture Outline

### 1. Define my_add(*args).
### 2. Define my_avg(*args).
### 3. Return 0 for empty input.
### 4. Use my_avg(*ages) to unpack a list.

---

## 5. Code Demo

```python
def my_add(*args: int) -> int:
    """
    Calculate the sum of an arbitrary number of integers.

    Parameters:
    *args (int): A variable-length argument list of integers.

    Returns:
    int: The sum of the provided integers.
    """
    # result = 0
    # for arg in args:
    #   result += arg
    # return result
    return sum(args)  # Utilizing Python's built-in sum function for efficiency and readability.

def my_avg(*args: int) -> float:
    """
    Calculate the average of an arbitrary number of integers.

    Parameters:
    *args (int): A variable-length argument list of integers.

    Returns:
    float: The average of the provided integers. Returns 0 if no arguments are provided to avoid division by zero.
    """
    if not args:  # Check if args is empty to prevent division by zero.
        return 0
    return sum(args) / len(args)  # Using built-in sum function and len function for concise code.

def main():
    # List of ages to be averaged
    ages = [27, 35, 42, 18, 20]
    # Printing the average of a list of ages using unpacking argument lists
    print("Average age:", my_avg(*ages))

    # Directly passing numbers to calculate their average
    print("Average of 1, 2, 3, 4, 5:", my_avg(1, 2, 3, 4, 5))

    # Example to demonstrate handling with no inputs
    print("Average with no inputs:", my_avg())  # Should return 0

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output / Notes

```text
Average age: 28.4
Average of 1, 2, 3, 4, 5: 3.0
Average with no inputs: 0
```

---

## 7. Exercises

### 1. Exercise
What does *args collect?

<details>
<summary>Solution</summary>

Extra positional arguments as a tuple.
</details>

---

### 2. Exercise
Why does my_avg() return 0?

<details>
<summary>Solution</summary>

To avoid division by zero.
</details>

---

### 3. Exercise
Create my_max(*args).

<details>
<summary>Solution</summary>

Return None if args is empty, otherwise return max(args).
</details>


---

## 8. Further Reading

- https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
- https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

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

