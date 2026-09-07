# 📊 Average Calculator with `*args`

This lesson demonstrates a compact average calculator using `*args` and a ternary conditional expression.

---

## 1. Learning Objectives

- Use `*args` to accept many numeric values.
- Calculate averages with `sum()` and `len()`.
- Avoid division by zero.
- Use a ternary conditional expression.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, loops, and simple terminal execution.

---

## 3. Key Concepts

- **`*args`**: Collects positional arguments into a tuple.
- **Average**: `sum(values) / count`.
- **Guard condition**: Handles empty input safely.
- **Ternary expression**: `value_if_true if condition else value_if_false`.

---

## 4. Lecture Outline

### 0:00–0:08 — Introduce the Example
- Read the input data and identify the goal of the script.

### 0:08–0:20 — Main Logic
- Walk through the important Python concepts used in the code.

### 0:20–0:32 — Output and Behaviour
- Run the script and explain the result.

### 0:32–0:40 — Improvements
- Discuss small fixes, cleaner structure, or extra validation.

---

## 5. Code Demo

```python
def avg(*args):
    return sum(args) / len(args) if args else 0

def main():
    print(avg())
    print(avg(10))
    print(avg(10, 20))

if __name__ == "__main__":
    main()
```

---

## 6. Expected Output

```text
0
10.0
15.0
```


---

## 7. Exercises

### 1. Level 1 — Short Answer
Why does `avg()` return `0` when no values are provided?

<details>
<summary>Solution</summary>

To avoid division by zero.
</details>

---

### 2. Level 2 — Coding
Round the result to two decimal places.

<details>
<summary>Solution</summary>

```python
def avg(*args):
    return round(sum(args) / len(args), 2) if args else 0
```
</details>

---

## 8. Further Reading

- [Python Docs: sum](https://docs.python.org/3/library/functions.html#sum)
- [Python Docs: Conditional Expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
