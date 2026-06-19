# 🌟 Armstrong Numbers (Digit Iteration & Powers)

This lesson checks whether a number is an **Armstrong number** (also called a narcissistic number): one equal to the sum of its own digits, each raised to the power of the digit count. For example, `371 = 3³ + 7³ + 1³`.

---

## 1. Learning Objectives

- Turn a number into its digits by converting it to a string.
- Iterate over the characters of a string.
- Raise each digit to a power with `**`.
- Accumulate a running total and compare it to the original number.

---

## 2. Prerequisites

- Comfort with functions returning booleans.
- Familiarity with `str()`, `int()`, `len()`, and `for` loops.
- Awareness of `try`/`except` for input.

---

## 3. Key Concepts

- **Digits via string**: `str(n)` lets you loop over each digit character; `int(digit)` converts it back to a number.
- **The power is the digit count**: `power = len(digits)`. For a 3-digit number, each digit is cubed.
- **Accumulator pattern**: `total += int(digit) ** power` builds the sum digit by digit.
- **The test**: `n == total` — an Armstrong number equals that sum.

---

## 4. Lecture Outline

### 0:00–0:10 — Decomposing into Digits
- `digits = str(n)`, `power = len(digits)`.

### 0:10–0:20 — Summing the Powered Digits
- Loop, `total += int(digit) ** power`.

### 0:20–0:28 — The Verdict & Input Guard
- `return n == total`; `main` validates input first.

---

## 5. Code Demos

```python
def is_armstrong_number(n):
    """Return True if n equals the sum of its digits each raised to the digit count."""
    digits = str(n)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    return n == total

def main():
    # Example: 371 = 3^3 + 7^3 + 1^3
    try:
        num = int(input("Please insert an int: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

if __name__ == "__main__":
    main()
```

**Example runs:**

```
Please insert an int: 371
371 is an Armstrong number.

Please insert an int: 372
372 is not an Armstrong number.
```

> 💡 **The string trick.** Converting `371` to `"371"` lets you walk its digits with a simple `for` loop, no integer math (`% 10`, `// 10`) required. Each character is converted back with `int(digit)` before being raised to the power.

> 🔢 **Single-digit numbers are all Armstrong.** For `n = 5`, `power = 1` and `5 ** 1 == 5`, so every single digit (0–9) trivially qualifies. The three-digit Armstrong numbers are 153, 370, 371, and 407 — a fun set to test.

---

## 6. Exercises

### 1. (Level 1, MCQ)
For `n = 153`, what is `power`?
- a) 1
- b) 2
- c) 3
- d) 153

<details>
<summary>Solution</summary>

**Answer:** c) 3 — there are three digits, so each is cubed.
</details>

---

### 2. (Level 1, Short Answer)
Why is `153` an Armstrong number?

<details>
<summary>Solution</summary>

Because `1³ + 5³ + 3³ = 1 + 125 + 27 = 153`, which equals the original number.
</details>

---

### 3. (Level 2, Coding)
Compute the Armstrong sum for `9474` and check whether it qualifies.

<details>
<summary>Solution</summary>

```python
print(is_armstrong_number(9474))   # True
# 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474
```
</details>

---

### 4. (Level 2, Coding)
Print all Armstrong numbers between 100 and 999.

<details>
<summary>Solution</summary>

```python
for n in range(100, 1000):
    if is_armstrong_number(n):
        print(n)        # 153, 370, 371, 407
```
</details>

---

### 5. (Level 3, Coding)
Rewrite `is_armstrong_number` using a generator expression with `sum()` instead of an explicit loop.

<details>
<summary>Solution</summary>

```python
def is_armstrong_number(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)
```
The generator feeds each powered digit straight into `sum()` — a compact, Pythonic version of the accumulator loop.
</details>

---

## 7. Further Reading

- [Python Docs: `pow` and the `**` operator](https://docs.python.org/3/library/functions.html#pow)
- [Python Docs: `sum`](https://docs.python.org/3/library/functions.html#sum)
- [Python Tutorial: `for` Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

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
