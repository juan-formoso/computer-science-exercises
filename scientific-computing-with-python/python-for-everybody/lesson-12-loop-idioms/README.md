# Loop idioms

## Making "smart" loops

The trick is "knowing" something about the whole loop when you are stuck writing code that only sees one entry at a time.

- Set some variables to initial values

- `for thing in data:`

  - Look for something or do something to each entry separately, updating a variable.

- Look at the variables.

### Question

**Below is code to find the smallest value from a list of values. One line has an error that will cause the code to not work as expected. Which line is it?:**

```
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
```

- [ ] 3

- [ ] 4

- [x] 6

- [ ] 7
