# 🎓 Student Enrollment with Flexible Arguments

This lesson demonstrates a flexible enrollment function using `*students`, keyword-only parameters, default values, and `**kwargs`.

---

## 1. Learning Objectives

- Use `*students` for multiple names.
- Use keyword-only parameters.
- Use default values.
- Collect extra metadata with `**kwargs`.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, loops, and simple terminal execution.

---

## 3. Key Concepts

- **`*students`**: Collects positional student names into a tuple.
- **Keyword-only parameter**: A parameter passed by name after `*students`.
- **Default value**: A value used when the caller does not provide one.
- **`**kwargs`**: Additional named information as a dictionary.

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
def enroll_student(*students, min_grade=50, department="Computer Science", **kwargs):
    print(f"Min grade: {min_grade}")
    print(f"Department: {department}")

    print("\nEnrolled Students:")
    for student in students:
        print(f" - {student}")

    print("\nAdditional Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print("---End of enrollment---")

def main():
    enroll_student("Alice", "Bob")
    print("------------------------")
    enroll_student("Helen", "Carol", "Nick", academic_year=2026, semester="Fall")
    print("------------------------")
    enroll_student("John", "Dave", min_grade=70, department="Maths", academic_year=2026, semester="Spring")
```

---

## 6. Expected Output

```text
Min grade: 50
Department: Computer Science

Enrolled Students:
 - Alice
 - Bob

Additional Information:
---End of enrollment---
```


## Formatting Note

In the original script, the `Additional Information` heading is indented inside the student loop. For cleaner output, it is better to print it after the student loop, as shown above.


---

## 7. Exercises

### 1. Level 1 — MCQ
What does `*students` collect?

- a) Student names passed positionally
- b) Only grades
- c) Keyword arguments
- d) A dictionary

<details>
<summary>Solution</summary>

**Answer:** a) Student names passed positionally.
</details>

---

### 2. Level 2 — Coding
Enroll three students in the `Physics` department.

<details>
<summary>Solution</summary>

```python
enroll_student("Anna", "Nick", "Maria", department="Physics", semester="Winter")
```
</details>

---

## 8. Further Reading

- [Python Docs: Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)

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
