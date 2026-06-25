# 📦 List Unpacking Demo

This lesson demonstrates different ways to unpack list values into variables, including starred expressions.

---

## 1. Learning Objectives

- Unpack list values into variables.
- Ignore values with _.
- Collect remaining values with *rest.
- Use starred expressions at the beginning, middle, or end.
- Understand rest values with shorter lists.

---

## 2. Prerequisites

- Basic Python syntax.
- Comfort with variables and functions.
- Ability to run a `.py` file from an IDE or terminal.

---

## 3. Key Concepts

- **Unpacking**: Assigning iterable items to variables in one line.
- **_**: Convention for values intentionally ignored.
- **Starred expression**: Captures multiple values into a list.
- **Rest values**: The remaining values collected by *rest, *start, or *middle.
- **Value count**: Unpacking must have enough values for the required variables.

---

## 4. Lecture Outline

### 1. Basic unpacking into a, b, c, d, e.
### 2. Ignore values using _.
### 3. Collect remaining values with *rest.
### 4. Use starred expressions in different positions.

---

## 5. Code Demo

```python
my_list = [1, 2, 3, 4, 5] #list(range(1, 5))

a, b, c, d, e = my_list
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")

a, _, c, _, e = my_list
print(f"Unpacked values: a={a}, b={b}, c={c}, e={e}")

x, *rest =my_list
print(x)
print(rest)

*start, z = my_list
print(start)
print(z)

start, *middle, end = my_list
print(f"start: {start}")
print(f"middle: {middle}")
print(f"end:{end}")

my_list = [1, 2]

a, b, *rest = my_list
print(f"a: {a}")
print(f"b: {b}")
print(f"rest: {rest}")
```

---

## 6. Expected Output / Notes

```text
Unpacked values: a=1, b=2, c=3, d=4, e=5
Unpacked values: a=1, b=2, c=3, e=5
1
[2, 3, 4, 5]
[1, 2, 3, 4]
5
start: 1
middle: [2, 3, 4]
end:5
a: 1
b: 2
rest: []
```

---

## 7. Exercises

### 1. Exercise
What does x, *rest = my_list do?

<details>
<summary>Solution</summary>

x gets the first item and rest gets all remaining items.
</details>

---

### 2. Exercise
What does _ mean?

<details>
<summary>Solution</summary>

It is a convention for an ignored value.
</details>

---

### 3. Exercise
Unpack [10, 20, 30, 40] into first, middle, last.

<details>
<summary>Solution</summary>

first, *middle, last = [10, 20, 30, 40]
</details>


---

## 8. Further Reading

- https://docs.python.org/3/reference/simple_stmts.html#assignment-statements
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

