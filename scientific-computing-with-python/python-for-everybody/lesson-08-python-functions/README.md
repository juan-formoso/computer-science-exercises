# Python Functions

## Stored (and reused) Steps

- Def creates a bit of code and record it like a macro and names it whatever you choose.

```
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

----------------------
Output:

Hello
Fun
Zip
Hello
Fun
```

## Functions

- There are two kinds of functions in Python.

  - **Built-in functions** that are provided as part of Python - print(), input(), type(), float(), int()...

  - **Functions that we define ourselves** and then use

- We treat the built-in function names as "new" **reserved words** (i.e., we avoid them as variable names)

## Function Definition

- In Python a **function** is some reusable code that takes **arguments**(s) as input, does some computation, and then returns a result or results.

- We define a **function** using the `def` reserved word.

- We call/invoke the **function** by using the function name, parentheses and **arguments** in an expression.

Example:
`big = max('Hello World)'`

**big = assignment**
**max = 'w'**
**'Hello World' = argument**

```
big = max('Hello World)'
print(big)
  w
tiny = min('Hello World')
print(tiny)
```

### Max Function

- A **function** is **some stored code** that we use. A function takes some **input** and produces an **output**.

```
big = max('Hello world')
print(big)
  w
```

**'Hello World'** (a string) -> max() function -> `'w'` a string

## Type Conversions

- When you put an integer and floating point in an expression, the integer is **implicitly** converted to a float.

- You can control this with the built-in functions int() and float().

```
print float(99) / 100
  0.99
i = 42
type(i)
  <class 'int'>
f = float(i)
print(f)
  42.0
type(f)
  <class 'float'>
print(1 + 2 * float(3) / 4 - 5)
  -2.5
```

## String Conversions

- You can also use `int()` and `float()` to convert between strings and integers.

- You will get an **error** if the string does not contain numeric characters.

```
sval = '123'
type(sval)
  <class 'str'>
print(sval + 1)
  Traceback (most recent call last):
    File"<stdin>", line 1, in <module>
  TypeError: cannot concatenate 'str' and 'int'
ival = int(sval)
type(ival)
  <class 'int'>
print(ival + 1)
  124
nsv = 'hello bob'
niv = int(nsv)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: invalid literal for int()
```

### Question

**What is the purpose of the "def" keyword in Python?**

- [ ] It is slang that means "The following code is really cool."

- [ ] It indicates the start of a function.

- [ ] It indicates that the following indented section of code is to be stored for later.

- [x] It indicates the start of a function, and the following indented section of code is to be stored later.

- [ ] None of the above.
