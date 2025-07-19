## Comparison Operators

In programming, we often need to compare values to make decisions. For example, is a user old enough to enter a site? Is the password correct? These are all yes/no questions.

In Python, we ask these questions using **comparison operators**. Every comparison you make will evaluate to one of two answers: `True` or `False`. These are our **boolean** data types.

---

### **Equality Operators**

These check if two values are the same or different.

* **Equal to `==`**: Checks if the values on both sides are equal.
    * `5 == 5` results in `True`.
    * `5 == 6` results in `False`.

* **Not equal to `!=`**: Checks if the values are *not* equal.
    * `5 != 6` results in `True`.
    * `"hello" != "hello"` results in `False`.

> **CRITICAL NOTE:** A single equals sign (`=`) is for **assigning** a value to a variable (e.g., `my_age = 24`). A double equals sign (`==`) is for **comparing** if two things are equal. You will almost certainly mix these up, I still make this mistake all the time, and end up spending way longer than I should trying to figure out why my code isn't running.

---

### **Magnitude Operators**

These check how values relate to each other in size. They work for numbers and also for strings (alphabetical order).

* **Greater than `>`**: Is the left value bigger than the right?
    * `10 > 5` results in `True`.

* **Less than `<`**: Is the left value smaller than the right?
    * `10 < 5` results in `False`.

* **Greater than or equal to `>=`**: Is the left value bigger than or equal to the right?
    * `5 >= 5` results in `True`.
    * `5 >= 4` results in `True`.

* **Less than or equal to `<=`**: Is the left value smaller than or equal to the right?
    * `4 <= 5` results in `True`.
    * `5 <= 4` results in `False`.

---

### **Quick Example**

Let's see these in action with variables.

```python
owen_age = 24
voting_age = 18
char_age = 28

# Ask some questions and print the True/False answers
print(f"Is Owen old enough to vote? {owen_age >= voting_age}")
# Expected: True

print(f"Are char and owen the same age? {owen_age == char_age}")
# Expected: False

print(f"Is char older than owen? {char_age > owen_age}")
# Expected: False