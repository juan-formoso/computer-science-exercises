# Variables, Expressions and Statements

## Constants

* **Fixed values** such as numbers, letters, and strings, are called **"constants"** because their value does not change

* Numeric **constants** are as you expect

* String **constants** use single quotes (') or double quotes (")

```
>>> print(123)
123
>>> print(98.6)
98.6
>>> print("Hello World")
Hello World
```

## Variables

* A **variable** is a named place in the memory where a programmer can store data and later retrieve the data using the **variable** "name".

* Programmers get to choose the names of the **variables**.

* You can change the contents of a **variable** in a later statement.

## Python Variable Name Rules

* Must start with a letter or underscore _
* Must consist of letters, nuumbers and underscores
* Case sensitive

  > Good: spam eggs spam23 speed
  > Bad: 23spam, #sign, var_12
  > Different: spam, Spam, SPAM

## Mnemonic Variable Names

* Since we programmers are given a choice in how we choose our variable names, there is a bit of "best practice"

* We name variables to help us remember what we intend to store in them ("**mnemonic**" = "memory aid")

* This can confuse beginning students because well-named variables often "sound" so good that they must be keywords

Option 1
```
x1q3z9ocd = 35.0
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ocd * x1q3z9afd
print(x1q3p9afd)
```

Option 2
```
a = 35.0
b = 12.50
c = a * b
print(c)
```

Option 3
```
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)
```

## Assignment Statements

* We assign a value to a variable using the assignment statement (=)

* An assignment statement consists of an *expression on the right-hand side* and a **variable** to store the result

```x = 3.9 * x * (1 - x)```
