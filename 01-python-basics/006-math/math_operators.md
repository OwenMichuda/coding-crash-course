## Math Operators in Python

Math in Python is pretty intuitive: it works just like a calculator, but with a few extra operators that are incredibly useful once you know them.

---

### **Basic Arithmetic**

These are the ones you use every day.

* **Addition `+`**: Adds two numbers. `5 + 3` results in `8`.
* **Subtraction `-`**: Subtracts one number from another. `5 - 3` results in `2`.
* **Multiplication `*`**: Multiplies numbers. `5 * 3` results in `15`.
* **Division `/`**: Divides numbers. This *always* results in a **float** (a number with a decimal). `10 / 4` results in `2.5`.

### **Advanced Division**

This is where Python gives you more control over division.

* **Floor Division `//`**: Divides and then **chops off the decimal part**, giving you a whole number (an **integer**). It always rounds down. `10 // 4` results in `2`.
* **Modulo `%`**: This operator doesn't give you the result of the division, but the **remainder** left over. This is perfect for checking if a number is even or odd. `10 % 3` results in `1` (because 3 goes into 10 three times with a remainder of 1). For some reason, modulo comes up way more than you'd expect, so it's a good one to keep in the back of the birdbrain.

### **Exponents**

* **Exponentiation `**`**: This is how you do "to the power of." `3 ** 2` is the same as $3^2$, which results in `9`.

---

### **Quick Example**

Here's a look at all of them in action.

```python
a = 16
b = 5

print(f"Addition: {a + b}")          # 16 + 5 = 21
print(f"Subtraction: {a - b}")        # 16 - 5 = 11
print(f"Multiplication: {a * b}")     # 16 * 5 = 80
print(f"Division: {a / b}")          # 16 / 5 = 3.2
print(f"Floor Division: {a // b}")    # 16 // 5 = 3
print(f"Modulo: {a % b}")            # 16 % 5 = 1 (the remainder)
print(f"Exponent: {b ** 2}")         # 5 to the power of 2 = 25
```

---

### **A Note on Order of Operations**

**PEMDAS!!** Python follows it:

1.  **P**arentheses `()`
2.  **E**xponents `**`
3.  **M**ultiplication `*` and **D**ivision `/`, `//`, `%` (from left to right)
4.  **A**ddition `+` and **S**ubtraction `-` (from left to right)

Because of this, `5 + 2 * 3` is calculated as `5 + 6`, which gives `11`. If you want to force the addition to happen first, use parentheses: `(5 + 2) * 3` gives `21`.