# 🐍 Python Functions & Functional Programming Practice — Files 01–18

This repository contains a structured collection of **18 Python practice scripts**.

The examples start from basic function concepts, type annotations, scope, lists, and parameters, and gradually move toward more advanced topics such as `*args`, `**kwargs`, recursion, lambda functions, `map()`, `filter()`, and `reduce()`.

The purpose of this chapter is to help beginners understand how Python functions work in real examples and how small scripts can be organized, tested, and improved.

---

## 📚 Repository Overview

| # | Script | Main Topic |
|---|--------|------------|
| 01 | `01_type_annotation.py` | Type annotations, docstrings, runtime validation |
| 02 | `02_generic_func.py` | Generic functions, `TypeVar`, `Sequence`, `Optional` |
| 03 | `03_function_scope.py` | Function scope and local variables |
| 04 | `04_list_demo.py` | List mutation with `.append()` |
| 05 | `05_list_duplicate.py` | List duplication and nested object references |
| 06 | `06_list_shallow.py` | Shallow copy with list slicing |
| 07 | `07_optional_params.py` | Optional/default parameters |
| 08 | `08_variable_length_arguments.py` | Variable-length arguments with `*args` |
| 09 | `09_list_unpacking.py` | List unpacking and starred expressions |
| 10 | `10_keyword_args.py` | Keyword arguments and dictionary unpacking with `**kwargs` |
| 11 | `11_facto_rec_demo.py` | Recursive factorial |
| 12 | `12_fibo_rec.py` | Recursive Fibonacci |
| 13 | `13_lambda_demo.py` | Lambda functions |
| 14 | `14_filter_even_nums.py` | Filtering values with `filter()` |
| 15 | `15_map_demo.py` | Transforming values with `map()` |
| 16 | `16_map_filter_lambda.py` | Combining `map()`, `filter()`, and `lambda` |
| 17 | `17_reduce_demo.py` | Factorial with `functools.reduce()` |
| 18 | `18_reduce_factorial_wow.py` | Step-by-step factorial with `reduce()` |

---

## 🎯 Learning Objectives

By completing these examples, you will be able to:

- Write functions with parameters and return values.
- Use Python type annotations.
- Understand the difference between documentation and runtime validation.
- Use docstrings and inspect function metadata.
- Explain local and global scope.
- Understand how mutable objects behave when passed into functions.
- Create shallow copies of lists.
- Understand nested list references.
- Use optional/default parameters.
- Pass a variable number of arguments with `*args`.
- Pass keyword arguments with `**kwargs`.
- Unpack lists and dictionaries.
- Use recursion for factorial and Fibonacci examples.
- Write simple lambda functions.
- Use `filter()` to keep selected values.
- Use `map()` to transform values.
- Combine `map()`, `filter()`, and `lambda`.
- Use `functools.reduce()` for rolling calculations.

---

## 🧠 Key Concepts Covered

### 1. Type Annotations

Type annotations describe what types a function expects and what it returns.

```python
def my_add(a: float | int, b: float | int) -> float | int:
    return a + b
```

Annotations help developers, editors, and static analysis tools understand your code better.

---

### 2. Runtime Validation

Type annotations are hints. They do not automatically prevent wrong values at runtime.

```python
if not isinstance(a, (int, float)):
    raise TypeError("Value must be int or float")
```

---

### 3. Generic Functions

Generic functions allow the same function to work with different types while keeping type information.

```python
from typing import Sequence, TypeVar

T = TypeVar("T")

def first(seq: Sequence[T]) -> T:
    return seq[0]
```

---

### 4. Function Scope

Variables created inside a function are local to that function.

```python
def add_numbers(x: int, y: int) -> int:
    x = 100
    return x + y
```

Changing `x` inside the function does not change the original variable passed into the function.

---

### 5. Mutable Lists

Lists are mutable, which means they can be changed in place.

```python
def append_to_list(li, element):
    li.append(element)
```

If you pass a list into this function, the original list changes.

---

### 6. Shallow Copy

A shallow copy creates a new outer list, but nested mutable objects can still be shared.

```python
new_list = my_list[:]
```

This means the outer lists are different objects, but nested lists inside them may still point to the same object.

---

### 7. Optional Parameters

A default value makes a parameter optional.

```python
def add(a: int, b: int, c: int = 0) -> int:
    return a + b + c
```

Here, `c` is optional, but `a` and `b` are still required.

---

### 8. `*args`

`*args` allows a function to accept many positional arguments.

```python
def my_avg(*args: int) -> float:
    if not args:
        return 0
    return sum(args) / len(args)
```

---

### 9. List Unpacking

List unpacking allows values to be assigned to variables in one line.

```python
a, b, *rest = [1, 2, 3, 4, 5]
```

After this:

```text
a = 1
b = 2
rest = [3, 4, 5]
```

---

### 10. `**kwargs`

`**kwargs` collects keyword arguments into a dictionary.

```python
def get_results(products, **kwargs):
    return [
        product for product in products
        if product[0] == kwargs.get("brand")
    ]
```

You can also unpack a dictionary when calling a function:

```python
criteria = {"brand": "lenovo", "price": 100}
get_results(products, **criteria)
```

---

### 11. Recursion

Recursion happens when a function calls itself.

```python
def factorial(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)
```

Every recursive function needs a base case.

---

### 12. Lambda Functions

A lambda is a short anonymous function.

```python
power_to = lambda base, exp: base ** exp
```

Equivalent normal function:

```python
def power_to(base, exp):
    return base ** exp
```

---

### 13. `filter()`

`filter()` keeps only values that satisfy a condition.

```python
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

---

### 14. `map()`

`map()` transforms every item in an iterable.

```python
cap_cities = map(lambda city: city.title(), cities)
```

---

### 15. `reduce()`

`reduce()` applies a rolling calculation to values until one result remains.

```python
from functools import reduce

result = reduce(lambda x, y: x * y, range(1, n + 1))
```

This can be used to calculate factorials.

---

## 🗂️ Suggested Folder Structure

```text
python-functions-practice/
├── 01_type_annotation.py
├── 02_generic_func.py
├── 03_function_scope.py
├── 04_list_demo.py
├── 05_list_duplicate.py
├── 06_list_shallow.py
├── 07_optional_params.py
├── 08_variable_length_arguments.py
├── 09_list_unpacking.py
├── 10_keyword_args.py
├── 11_facto_rec_demo.py
├── 12_fibo_rec.py
├── 13_lambda_demo.py
├── 14_filter_even_nums.py
├── 15_map_demo.py
├── 16_map_filter_lambda.py
├── 17_reduce_demo.py
├── 18_reduce_factorial_wow.py
└── README.md
```

---

## ⚙️ Requirements

To run the scripts, you need:

- Python 3.10 or newer
- A code editor such as VS Code or PyCharm
- Basic terminal usage

Most examples use only built-in Python features.

The `reduce()` examples use:

```python
from functools import reduce
```

No external packages are required.

---

## ▶️ How to Run

Open the terminal inside the project folder and run a script.

```bash
python 01_type_annotation.py
```

or:

```bash
python3 01_type_annotation.py
```

On Windows, you can also use:

```bash
py 01_type_annotation.py
```

---

## 🧪 Example Runs

### 01 — Type Annotation Demo

```bash
python 01_type_annotation.py
```

Possible output:

```text
30
12.1
Both a and b must be integers or floats
Annotations: {'a': float | int, 'b': float | int, 'return': float | int}
```

---

### 08 — Variable-Length Arguments

```bash
python 08_variable_length_arguments.py
```

Expected output:

```text
Average age: 28.4
Average of 1, 2, 3, 4, 5: 3.0
Average with no inputs: 0
```

---

### 11 — Recursive Factorial

```bash
python 11_facto_rec_demo.py
```

Example input:

```text
Please insert an integer: 5
```

Expected output:

```text
5! = 120
```

---

### 14 — Filter Even Numbers

```bash
python 14_filter_even_nums.py
```

Expected output:

```text
2    4    6    8    10
```

---

### 15 — Map Demo

```bash
python 15_map_demo.py
```

Expected output:

```text
London
Paris
Athens
Barcelona
```

---

### 18 — Reduce Factorial

```bash
python 18_reduce_factorial_wow.py
```

Example input:

```text
Give an int to calc facto: 5
```

Expected output:

```text
5! = 120
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
24 * 5 = 120
Final result: 120
```

---

## 🧭 Recommended Study Path

A good order to study the scripts is:

1. **01–03**: Start with type annotations, generic functions, and function scope.
2. **04–06**: Learn how lists behave, especially with mutation and copying.
3. **07–10**: Practice function parameters, `*args`, unpacking, and `**kwargs`.
4. **11–12**: Study recursion through factorial and Fibonacci.
5. **13–16**: Learn lambda functions, `map()`, and `filter()`.
6. **17–18**: Finish with `reduce()` and step-by-step factorial calculations.

---

## ✅ Practice Checklist

Use this checklist while studying:

- [ ] I can write a function with type annotations.
- [ ] I understand that annotations are not runtime validation by themselves.
- [ ] I can raise and catch a `TypeError`.
- [ ] I can explain what local scope means.
- [ ] I understand how mutable lists behave inside functions.
- [ ] I can create a shallow copy of a list.
- [ ] I understand why nested lists can still be shared.
- [ ] I can define optional/default parameters.
- [ ] I can use keyword arguments.
- [ ] I can use `*args`.
- [ ] I can use `**kwargs`.
- [ ] I can unpack lists into variables.
- [ ] I can unpack a dictionary into keyword arguments.
- [ ] I can write a simple recursive function.
- [ ] I can explain the base case of recursion.
- [ ] I can write a lambda expression.
- [ ] I can use `filter()` to keep values.
- [ ] I can use `map()` to transform values.
- [ ] I can use `reduce()` for a rolling calculation.

---

## ⚠️ Known Notes / Small Fixes

### 07 — Optional Parameters

In `07_optional_params.py`, this call causes an error:

```python
print(add(10))
```

because `b` is required. Only `c` has a default value.

A corrected version would be:

```python
print(add(10, 0))
```

---

### 12 — Fibonacci Main Function

In `12_fibo_rec.py`, the Fibonacci function is defined, but `main()` contains only:

```python
pass
```

To test it, you can add:

```python
def main():
    for i in range(10):
        print(f"fibo({i}) = {fibo(i)}")
```

---

### 16 — Typo in `.title()`

In `16_map_filter_lambda.py`, the method is written as:

```python
city.tittle()
```

The correct method is:

```python
city.title()
```

---

## 🚀 Possible Improvements

Some useful improvements for this collection:

- Add input validation for all scripts that use `input()`.
- Add more examples inside each `main()` function.
- Replace repeated code with helper functions.
- Add unit tests with `pytest`.
- Add screenshots of terminal output.
- Add one README inside each script folder.
- Add comments explaining the most difficult lines.
- Compare recursive solutions with iterative solutions.
- Add performance notes for recursion and `reduce()`.

---

## 📖 Further Reading

- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Docs: More on Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Docs: Typing](https://docs.python.org/3/library/typing.html)
- [Python Docs: Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Python Docs: map](https://docs.python.org/3/library/functions.html#map)
- [Python Docs: filter](https://docs.python.org/3/library/functions.html#filter)
- [Python Docs: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and improvements.

---

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

---

## Contact 📧

Dimitris - jimroumpi@gmail.com

🔗 *Note: These are Python scripts and require a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a>
  (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
