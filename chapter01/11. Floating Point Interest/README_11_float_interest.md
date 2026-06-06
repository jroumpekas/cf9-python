# 💰 Formatting Money: Floats, Underscores, and `:,.2f`

This lesson computes a simple interest amount and formats it as currency. It introduces two readability features: underscores inside numeric literals (`215_000.73`) and f-string number formatting with a thousands separator and fixed decimals (`{value:,.2f}`).

---

## 1. Learning Objectives

- Use underscores in numeric literals to make large numbers readable.
- Multiply floats to compute a result (interest = amount × rate).
- Format a number with a thousands separator using `:,`.
- Limit a number to two decimal places using `.2f`.
- Combine both into the currency format `:,.2f` inside an f-string.

---

## 2. Prerequisites

- Familiarity with float variables and multiplication.
- Basic f-string usage.
- Understanding that money is usually shown with two decimals.

---

## 3. Key Concepts

- **Numeric underscores**: `215_000.73` is exactly `215000.73`; the `_` is ignored by Python and only helps humans read the value.
- **`amount * rate`**: Standard float multiplication.
- **`:,`**: A format specifier that inserts commas as thousands separators.
- **`.2f`**: Fixed-point formatting with two digits after the decimal point.
- **`:,.2f`**: The two combined — grouped thousands *and* two decimals, ideal for currency.

---

## 4. Lecture Outline

### 0:00–0:06 — Readable Numbers with Underscores
- `amount = 215_000.73` and why underscores help.

### 0:06–0:12 — Computing Interest
- `rate = 0.25`, then `interest = amount * rate`.

### 0:12–0:20 — Formatting the Result
- Building `f"Total interest: ${interest:,.2f}"`.
- What each part of `:,.2f` contributes.

---

## 5. Code Demos

```python
amount = 215_000.73

rate = 0.25

interest = amount * rate

print(f"Total interest: ${interest:,.2f}")
```

**Expected output:**

```
Total interest: $53,750.18
```

> 💡 The raw product is `53750.1825`. The `:,.2f` formatter groups the thousands with a comma and rounds to two decimal places, giving `53,750.18`. The `$` is just literal text in the f-string.

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is the value of `1_000_000`?
- a) `1000000`
- b) `"1_000_000"`
- c) A syntax error
- d) `1`

<details>
<summary>Solution</summary>

**Answer:** a) `1000000`. Underscores in numeric literals are purely cosmetic.
</details>

---

### 2. (Level 1, Short Answer)
What does the `.2f` part of `{x:,.2f}` control?

<details>
<summary>Solution</summary>

It formats `x` as a fixed-point number with exactly two digits after the decimal point.
</details>

---

### 3. (Level 2, Coding)
Given `price = 1234.5`, print it as `$1,234.50`.

<details>
<summary>Solution</summary>

```python
price = 1234.5
print(f"${price:,.2f}")
```
</details>

---

### 4. (Level 2, Coding)
Compute 15% of `89_990.00` and print it formatted as currency with a euro sign, e.g. `€13,498.50`.

<details>
<summary>Solution</summary>

```python
amount = 89_990.00
result = amount * 0.15
print(f"€{result:,.2f}")
```
</details>

---

### 5. (Level 3, Coding)
Ask the user for an amount and an interest rate (as a percentage, e.g. 5 for 5%), then print the interest formatted as `$X,XXX.XX`.

<details>
<summary>Solution</summary>

```python
amount = float(input("Amount: "))
percent = float(input("Rate (%): "))
interest = amount * (percent / 100)
print(f"Total interest: ${interest:,.2f}")
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
- [PEP 515: Underscores in Numeric Literals](https://peps.python.org/pep-0515/)
- [Python Tutorial: Formatted String Literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

---

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Dimitris - jimroumpi@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a> (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>
