# 🧠 Inner Functions & Grade Calculation

This lesson demonstrates inner functions through a grade calculator. The outer function calculates a weighted average and returns both the numeric average and the letter grade.

---

## 1. Learning Objectives

- Define functions inside another function.
- Calculate a weighted average.
- Use conditional logic for grade boundaries.
- Return multiple values as a tuple.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, loops, and simple terminal execution.

---

## 3. Key Concepts

- **Inner function**: A function defined inside another function.
- **Weighted average**: Different scores contribute different percentages.
- **Tuple return**: A function can return more than one value.
- **Grade mapping**: Numeric scores are converted into letter grades.

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
from typing import List, Tuple, Union

def calculate_grade(assignment_scores: List[Union[int, float]], mid_score: Union[int, float], final_score: Union[int, float]) -> Tuple[float, str]:
    def weighted_average():
        assignment_score = sum(assignment_scores) / len(assignment_scores)
        return (assignment_score * 0.4) + (mid_score * 0.3) + (final_score * 0.3)

    def determine_grade(average: float) -> str:
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "E"

    average = weighted_average()
    grade = determine_grade(average)
    return average, grade

def main():
    final_average, final_grade = calculate_grade([85, 90, 88, 92], 92, 84)
    print(f"The final grade is: {final_grade} with average: {final_average}")
```

---

## 6. Expected Output

```text
The final grade is: B with average: 88.1
```


## ⚠️ Known Issue in the Original Script

The original script has small variable-name typos, such as `grage`, `final_avrage`, and `final_averge`. The demo above uses the corrected names: `grade` and `final_average`.


---

## 7. Exercises

### 1. Level 1 — Short Answer
Why is `weighted_average()` placed inside `calculate_grade()`?

<details>
<summary>Solution</summary>

Because it is helper logic used only by `calculate_grade()`, so keeping it inside makes the code organized.
</details>

---

### 2. Level 2 — Coding
Add an `F` grade for averages below 50.

<details>
<summary>Solution</summary>

```python
elif average >= 50:
    return "E"
else:
    return "F"
```
</details>

---

## 8. Further Reading

- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

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
