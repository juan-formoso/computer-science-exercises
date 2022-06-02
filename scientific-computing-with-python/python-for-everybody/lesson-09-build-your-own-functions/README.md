# Build our Own Functions

- We create a new function using the `def` keyword followed by optional parameteres in parentheses

- We indent the body of the function

- This **defines** the function but **does not** execute the body of the function

```
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
```

## Definitions and Uses

- Once we have **defined** a function, we can **call** (or **invoke**) it as many times as we like

- This is **store** and **reuse** pattern

## Arguments

- An **argument** is a value we pass into the **function** as its **input** when we call the function.

- We use **arguments** so we can direct the **function** to do different kinds of work when we call it at **different** times.

- We put the **arguments** in parentheses after the **name** of the function

`big = max('Hello world')` > 'Hello world' is an argument.

## Parameters

- A **parameter** is a variable which we use **in** the function **definition**. It is a "handle" that allows the code in the function to access the **arguments** for a particular function invocation.

## Return values

- Often a function will take its arguments, do some computation, and **return** a value to be used as the value of the function call in the **calling expression**. The **return** keyword is used for this.

- A "fruitful" **function** is one that produces a **result** (or **return value**)

- The **return** statement ends the **function** execution and "sends back" the **result** of the **function**

## Arguments, Parameters and Results

```
def max(inp):
    blah
    blah
    for x in y:
        blah
        blah
    return 'w'
--------------------

Argument: 'Hello world'
Parameter: inp
Result: 'w'
```

## Multiple Parameters / Arguments

- We can define more than one **parameter** in the **function definition**.

- We simply add more **arguments** when we call the **function**.

- We match the number and order of arguments and parameters.

- If you don't pass any parameters you will get a 'Traceback'.

## Void (non-fruitful) Functions

- When a function does not return a value, we call it a **"void"** function.

- Functions that return values are "fruitful" functions.

- **Void** functions are "not fruitful".

## To function or not to function...

- Organize your code into "paragraphs" - capture a complete thought and "name it".

- Don't repeat yourself - make it work once and then reuse it.

- If something gets too long or complex, break it up into logical chunks and put those chunks in functions.

- Make a library of common stuff that you do over and over - perhaps share this with your friends...

### Question

What will the following Python program print out?:

```
def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()
```

- [ ] <br>

```
Zap
ABC
jane
fred
jane
```

- [ ] <br>

```
Zap
ABC
Zap
```

- [ ] <br>

```
ABC
Zap
jane
```

- [x] <br>

```
ABC
Zap
ABC
```

- [ ] <br>

```
Zap
Zap
Zap
```
