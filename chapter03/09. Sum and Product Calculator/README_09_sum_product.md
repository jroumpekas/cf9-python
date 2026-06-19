# ➕✖️ Sum and Product of 1…N (Returning a Tuple)

This lesson computes both the **sum** and the **product** of the numbers from 1 to N in a single function, returning both results as a **tuple**. It reinforces the accumulator pattern and shows clean input validation with a manually `raise`d exception.

---

## 1. Learning Objectives

- Maintain two accumulators in one loop (sum and product).
- Initialise accumulators correctly (`0` for sum, `1` for product).
- Return multiple values as a **tuple** and unpack them.
- Validate input and `raise ValueError` for out-of-range values.
- Format large numbers with thousands separators using `:,`.

---

## 2. Prerequisites

- Comfort with `for` loops and `range`.
- Familiarity with `try`/`except` and `int(input(...))`.
- Awareness of tuples and unpacking.

---

## 3. Key Concepts

- **Two accumulators**: `total_sum` starts at `0` (additive identity); `total_product` starts at `1` (multiplicative identity). Starting the product at `0` would wrongly zero everything.
- **Returning a tuple**: `return total_sum, total_product` packs two values; `a, b = func()` unpacks them.
- **Manual `raise`**: `if upper_bound <= 0: raise ValueError` funnels the bad-value case into the same `except` that catches non-integers.
- **`:,` formatting**: `f"{total_product:,}"` inserts thousands separators (e.g. `3,628,800`).

---

## 4. Lecture Outline

### 0:00–0:10 — The Two Accumulators
- Initialise `0` and `1`, then loop `range(1, upper_bound + 1)`.

### 0:10–0:18 — Returning Both Results
- `return total_sum, total_product`.

### 0:18–0:28 — Validation & Output
- `raise ValueError` for non-positive input; format with `:,`.

---

## 5. Code Demos

```python
def calculate_sum_and_product(upper_bound):
    """Return (sum, product) of the numbers 1..upper_bound."""
    total_sum = 0
    total_product = 1
    for i in range(1, upper_bound + 1):
        total_sum += i
        total_product *= i
    return total_sum, total_product

def main():
    try:
        upper_bound = int(input("Please insert a positive int: "))
        if upper_bound <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    total_sum, total_product = calculate_sum_and_product(upper_bound)
    print(f"Sum (1 - {upper_bound}): {total_sum:,}")
    print(f"Product (1 - {upper_bound}): {total_product:,}")

if __name__ == "__main__":
    main()
```

**Example run:**

```
Please insert a positive int: 10
Sum (1 - 10): 55
Product (1 - 10): 3,628,800
```

> 💡 **The identity-element rule.** A sum accumulator starts at `0` because adding `0` changes nothing; a product accumulator starts at `1` because multiplying by `1` changes nothing. Starting the product at `0` would make the result always `0`.

> 🧩 **One `except` for two problems.** Non-integer input makes `int()` raise `ValueError` automatically; a non-positive value is rejected by the manual `raise ValueError`. Both land in the same handler, keeping the validation tidy.

---

## 6. Exercises

### 1. (Level 1, MCQ)
Why is `total_product` initialised to `1`?
- a) Style preference
- b) Because `1` is the multiplicative identity (multiplying by it changes nothing)
- c) To skip the number 1
- d) It's a bug; it should be `0`

<details>
<summary>Solution</summary>

**Answer:** b) `1` is the multiplicative identity. Starting at `0` would make every product `0`.
</details>

---

### 2. (Level 1, Short Answer)
What does `return total_sum, total_product` actually return?

<details>
<summary>Solution</summary>

A single tuple `(total_sum, total_product)`. The comma creates the tuple; the caller can unpack it with `a, b = ...`.
</details>

---

### 3. (Level 2, Coding)
Note that the product of `1..upper_bound` is just `upper_bound!`. Verify for `upper_bound = 5`.

<details>
<summary>Solution</summary>

```python
s, p = calculate_sum_and_product(5)
print(s, p)   # 15 120   (120 = 5!)
```
</details>

---

### 4. (Level 2, Coding)
Unpack only the sum and ignore the product using the conventional throwaway name.

<details>
<summary>Solution</summary>

```python
total_sum, _ = calculate_sum_and_product(10)
print(total_sum)   # 55
```
`_` is the idiomatic "I don't need this value" placeholder.
</details>

---

### 5. (Level 3, Coding)
Replace the loops with built-ins: `sum()` for the sum and `math.prod()` for the product.

<details>
<summary>Solution</summary>

```python
import math

def calculate_sum_and_product(upper_bound):
    nums = range(1, upper_bound + 1)
    return sum(nums), math.prod(nums)
```
`math.prod` (Python 3.8+) is the multiplicative counterpart to `sum`.
</details>

---

## 7. Further Reading

- [Python Docs: `math.prod`](https://docs.python.org/3/library/math.html#math.prod)
- [Python Tutorial: Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Docs: Format String Syntax (`:,`)](https://docs.python.org/3/library/string.html#format-string-syntax)

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
