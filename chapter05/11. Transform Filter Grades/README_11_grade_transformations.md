# 🎓 Grade Transformations with List & Dictionary Comprehensions

This lesson group contains three related scripts that progressively improve the same idea:  
**transforming, filtering, categorizing, and analyzing student grades**.

The examples start with a simple list comprehension demo and then evolve into a more complete grade-processing workflow using functions, lists, and dictionaries.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `11_transform_grades.py` | Simple first version that upscales grades using list comprehension. |
| `11_improve_01.py` | Improved list-based version with functions for upscaling, filtering, categorizing, and averaging grades. |
| `11_improve_02.py` | Dictionary-based version that connects student names with their grades. |

---

## 1. Learning Objectives

By studying these examples, you will be able to:

- Use list comprehensions to transform numeric values.
- Use conditional expressions inside comprehensions.
- Filter grades based on pass/fail rules.
- Categorize grades into passed, failed, and honors groups.
- Calculate averages safely.
- Use dictionary comprehensions to keep student names connected with grades.
- Compare list-based and dictionary-based approaches.

---

## 2. Prerequisites

- Lists.
- Dictionaries.
- Functions.
- Conditional expressions.
- List comprehensions.
- Dictionary comprehensions.
- Basic arithmetic.

---

## 3. Key Concepts

### Grade Upscaling

Grades less than or equal to `9` are increased by `1`, while `10` remains unchanged.

```python
upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
```

Example:

```text
[7, 5, 9, 10, 3] → [8, 6, 10, 10, 4]
```

---

### Filtering Passed Grades

A student passes when the grade is greater than or equal to `5`.

```python
passed = [grade for grade in grades if grade >= 5]
```

---

### Categorizing Grades

Grades can be separated into three groups:

- **Passed**: grade from `5` to `9`
- **Failed**: grade below `5`
- **Honors**: grade equal to `10`

```python
passed = [grade for grade in grades if grade >= 5 and grade < 10]
failed = [grade for grade in grades if grade < 5]
honors = [grade for grade in grades if grade == 10]
```

---

### Calculating Average

The average is calculated only if the list is not empty.

```python
return sum(grades) / len(grades) if grades else 0
```

This avoids division by zero.

---

### Dictionary Comprehension

The dictionary version keeps the student's name together with the grade.

```python
return {
    name: (grade + 1 if grade <= 9 else grade)
    for name, grade in students_grades.items()
}
```

This is more realistic because in real applications we usually need to know **which student** received each grade.

---

## 4. Lecture Outline

### 0:00–0:08 — Simple Grade Upscaling
- Start with `11_transform_grades.py`.
- Use a basic list comprehension.

### 0:08–0:20 — Functional Decomposition
- Move to `11_improve_01.py`.
- Split the logic into smaller functions.

### 0:20–0:32 — Categorization
- Separate grades into passed, failed, and honors.

### 0:32–0:45 — Dictionary-Based Version
- Move to `11_improve_02.py`.
- Keep student names connected with their grades.

---

## 5. Code Demos

### Simple Version

```python
def main():
    grades = [7, 5, 9, 10, 3]

    upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
    print(f"Upscaled grades: {upscaled_grades}")
```

---

### Improved List-Based Version

```python
def upscale_grades(grades):
    return [grade + 1 if grade <= 9 else grade for grade in grades]

def filter_passed(grades):
    return [grade for grade in grades if grade >= 5]

def categorize_grades(grades):
    passed = [grade for grade in grades if grade >= 5 and grade < 10]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]
    return passed, failed, honors

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
```

---

### Dictionary-Based Version

```python
def upscale_grades(students_grades):
    return {
        name: (grade + 1 if grade <= 9 else grade)
        for name, grade in students_grades.items()
    }

def filter_grades(students_grades):
    return {
        name: grade
        for name, grade in students_grades.items()
        if grade >= 5
    }

def categorize_grades(students_grades):
    passed = {
        name: grade
        for name, grade in students_grades.items()
        if 5 <= grade < 10
    }

    failed = {
        name: grade
        for name, grade in students_grades.items()
        if grade < 5
    }

    honors = {
        name: grade
        for name, grade in students_grades.items()
        if grade == 10
    }

    return passed, failed, honors
```

---

## 6. Expected Output Example

For this list:

```python
grades = [7, 5, 9, 10, 3, 6, 8, 4, 10, 2]
```

Expected output:

```text
Original grades: [7, 5, 9, 10, 3, 6, 8, 4, 10, 2]
Upscaled grades (list comprehension): [8, 6, 10, 10, 4, 7, 9, 5, 10, 3]
Passed grades (list comprehension): [7, 5, 9, 10, 6, 8, 10]
Passed students: [7, 5, 9, 6, 8]
Failed students: [3, 4, 2]
Honors students: [10, 10]
Average grade: 6.40
```

---

## 7. List vs Dictionary Approach

| Approach | Best Use Case |
|----------|---------------|
| List of grades | When you only care about numeric values. |
| Dictionary of students and grades | When you need to preserve student names. |

Example list:

```python
grades = [7, 5, 9, 10, 3]
```

Example dictionary:

```python
students_grades = {
    "Alice": 7,
    "Bob": 5,
    "Charlie": 9
}
```

The dictionary version is more useful for real applications because it keeps the grade connected to the student.

---

## 8. Notes / Small Improvements

### `11_transform_grades.py`

This is a good first draft. It focuses only on one idea:

```python
grade + 1 if grade <= 9 else grade
```

The `TODO` comment can be completed later with filtering, categorizing, and average calculation.

---

### `11_improve_01.py`

This version is cleaner because each operation has its own function:

- `upscale_grades()`
- `filter_passed()`
- `categorize_grades()`
- `calculate_average()`

This is better structure and easier to test.

---

### `11_improve_02.py`

The dictionary version is a good next step, but the `main()` function currently defines the data and does not print the results.

A suggested complete `main()` would be:

```python
def main():
    students_grades = {
        "Alice": 7,
        "Bob": 5,
        "Charlie": 9,
        "David": 10,
        "Eve": 3,
        "Frank": 6,
        "Grace": 8,
        "Heidi": 4,
        "Ivan": 10,
        "Judy": 2
    }

    print("Original grades:", students_grades)
    print("Upscaled grades:", upscale_grades(students_grades))
    print("Passed grades:", filter_grades(students_grades))

    passed, failed, honors = categorize_grades(students_grades)
    print("Passed:", passed)
    print("Failed:", failed)
    print("Honors:", honors)

    print(f"Average: {calculate_average(students_grades):.2f}")
```

---

## 9. Exercises

### 1. Level 1 — MCQ

What does this expression do?

```python
grade + 1 if grade <= 9 else grade
```

- a) Adds 1 to every grade.
- b) Adds 1 only if the grade is less than or equal to 9.
- c) Subtracts 1 from every grade.
- d) Keeps only passing grades.

<details>
<summary>Solution</summary>

**Answer:** b) Adds 1 only if the grade is less than or equal to 9.
</details>

---

### 2. Level 1 — Short Answer

Why should grade `10` remain unchanged?

<details>
<summary>Solution</summary>

Because `10` is already the maximum grade. Upscaling it would create an invalid grade such as `11`.
</details>

---

### 3. Level 2 — Coding

Create a function that returns only failed grades from a list.

<details>
<summary>Solution</summary>

```python
def filter_failed(grades):
    return [grade for grade in grades if grade < 5]
```
</details>

---

### 4. Level 2 — Coding

Create a dictionary comprehension that keeps only students with grade `10`.

<details>
<summary>Solution</summary>

```python
honors = {
    name: grade
    for name, grade in students_grades.items()
    if grade == 10
}
```
</details>

---

### 5. Level 3 — Challenge

Create a function that returns a summary dictionary:

```python
{
    "average": 6.4,
    "passed_count": 7,
    "failed_count": 3,
    "honors_count": 2
}
```

<details>
<summary>Solution</summary>

```python
def summarize_grades(grades):
    passed = [grade for grade in grades if grade >= 5]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]

    return {
        "average": sum(grades) / len(grades) if grades else 0,
        "passed_count": len(passed),
        "failed_count": len(failed),
        "honors_count": len(honors)
    }
```
</details>

---

## 10. Further Reading

- [Python Docs: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python Docs: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Docs: Conditional Expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

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
