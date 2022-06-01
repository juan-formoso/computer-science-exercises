# Conditional Statements

## Comparison Operators

- **Boolean expressions** ask a question and produce a Yes or No result which we use to control program flow

- **Boolean expressions** using **comparison operators** evaluate to True / False or Yes / No

- Comparison operators look at variables but do not change the variables

| **Python** | **Meaning**              |
| :--------- | :----------------------: |
| <          | Less than                |
| <=         | Less than or Equal to    |
| ==         | Equal to                 |
| >=         | Greater than or Equal to |
| >          | Greater than             |
| !=         | Not equal                |


**Remember: "=" is used for assignment**

## Indentation

- **Increase indent** indent after an **if** statement or **for** statement (after : )

- **Maintain indent** to indicate the **scope** of the block (which lines are affected by the **if/for**)

- **Reduce indent** back to the level of the **if** statement or **for** statement to indicate the end of the block

- **Blank lines** are ignored - they do not affect **indentation**

- **Comments** on a line by themselves are ignored with regard to **indentation**

### Warning: Turn Off Tabs!!!

- Atom automatically uses spaces for files with ".py" extension (nice!)

- Most text editor can turn **tabs** into **spaces** - make sure to enable this feature

  - NotePad++: Settings -> Preferences -> Language Menu/**Tab** Settings

  - TextWrangler: TextWrangler -> Preferences -> Editor Defaults

- Python cares a **lot** about how far a line is indented. If you mix **tabs** and **spaces**, you may get "**indentation errors**" even if everything looks fine

**increase / maintain** after ir or for
**decrease** to indicate end of block

```
x = 5
if x > 2:
    print("Bigger than 2")
    print("Still bigger")
print("Done with 2")

for i in range(5):
    print(i)
    if i > 2:
        print("Bigger than 2")
    print("Done with i", i)
print("All Done")
```

**Think about begin/end blocks**

## Two-way Decisions

- Sometimes we want to do one thing if a logical expression is true and something else if the expression is false

- It is like a fork in the road - we must choose **one or the other** path but not both

**With else:**

```
x = 4

if x > 2:
    print("Bigger")
    else:
        print("Smaller")

print "All done"
```

**Visualize Blocks**

### Question

Which code is indented correctly to "Yes" if **x = 0** and **y = 10** ?

- [ ] <br>

```
if 0 == x:
if y == 10:
print("Yes")
```

- [ ] <br>

```
if 0 == x:
    if y == 10:
    print("Yes")
```

- [ ] <br>

```
if 0 == x:
if y == 10:
    print("Yes")
```

- [ ] <br>

```
if 0 == x:
    if y == 10:
        print("Yes")
```
