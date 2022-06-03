# Definite Loops

- Quite often we have a **list** of items of the **lines in a file** - effectively a **finite set** of things.

- We can write a loop to run the loop once for each of the items in a set using the Python `for` construct.

- These loops are called **"definite loops"** because they execute an exact number of times.

- We say that **"definite loops iterate through the members of a set"**

## A Simple Definite Loop

- Definite loops (for loops) have explicit **iteration variables** that change each time thorugh a loop. These **iteration variables** move through the sequence or set.

```
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

-------------------------------
Ouput:

5
4
3
2
1
Blastoff!
```

**"i" is going to be assigned 5 times to each value of the list**

- See example.py to more details...

## Looking at In...

- The **iteration variable** "iterates" through the **sequence** (ordered set).

- The **block(body)** of code is executed once for each value **in** the sequence.

- The **iteration variable** moves through all of the values **in** the **sequence**.

```
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

--------------------------------
Iteration variable: i
Five-element sequence: [5, 4, 3, 2, 1]
```

### Question

**How many lines will the following code print?:**

```
for i in [2, 1, 5]:
    print(i)
```

- [ ] 1

- [ ] 2

- [x] 3

- [ ] 5
