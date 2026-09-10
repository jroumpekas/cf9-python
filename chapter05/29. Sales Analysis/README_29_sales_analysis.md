# 📈 Sales Analysis with Dictionaries and Comprehensions

This lesson demonstrates a realistic sales-analysis workflow using lists, dictionaries, comprehensions, formatting, and aggregate calculations.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `29_sales_analysis.py` | Performs monthly sales analysis with filtering, discounts, taxes, totals, averages, max, and min. |

---

## 1. Learning Objectives

- Create monthly sales data.
- Build a dictionary with `dict(zip(...))`.
- Validate empty or mismatched data.
- Filter high-sales months.
- Apply discounts and taxes.
- Find best and worst months.

---

## 2. Prerequisites

- Basic Python syntax.
- Functions and variables.
- Lists, dictionaries, classes, or modules depending on the example.
- Terminal usage to run Python scripts.

---

## 3. Key Concepts

- **`zip()`**: Combines months and sales values.
- **Filtering**: Keeps months with sales above a target.
- **Dictionary transformation**: Creates discounted and tax dictionaries.
- **Aggregates**: Uses sum, average, max, and min for analysis.

---

## 4. Code Demo

```python
monthly_sales = dict(zip(months, sales))

high_sales_months = {
    month: value
    for month, value in monthly_sales.items()
    if value >= 15_000
}

discounted_sales = {
    month: value * 0.9 if value > 20_000 else value
    for month, value in monthly_sales.items()
}
```

---

## 5. Expected Output / Behaviour

```text
Monthly Sales (in thousands): {...}
High Sales Months (>= 15,000): {...}
Discounted Sales (10% discount for sales > 20,000): {...}
Total Annual Sales: ...
Best Month: ...
Worst Month: ...
```


---

## 6. Exercises

### 1. Level 1 — Short Answer
Explain the main idea of this script in your own words.

<details>
<summary>Solution</summary>

The script demonstrates one focused Python concept through a small runnable example.
</details>

---

### 2. Level 2 — Coding
Add one extra test case to the script and run it again.

<details>
<summary>Solution</summary>

Add one more function call or one more input example inside `main()`.
</details>

---

## 7. Further Reading

- [Python Docs: Tutorial](https://docs.python.org/3/tutorial/)
- [Python Docs: Standard Library](https://docs.python.org/3/library/)

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
