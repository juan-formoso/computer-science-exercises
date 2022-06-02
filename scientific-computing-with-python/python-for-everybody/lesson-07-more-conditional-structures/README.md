# More Conditional Steps

## Multi-way Puzzles

- Which will never print regardless of the value for x?

* [ ] <br>

```
if x < 2:
    print("Below 2")
elif x >= 2:
    print("Two or more")
else:
    print("Something else")
```

- [x] <br>

```
if x < 2:
    print("Below 2")
elif x < 20:
    print("Below 20")
elif x < 10:
    print("Below 10")
else:
    print("Something else")
```

**This will happen because if a number is below 20 but it's also below 10 it will never reach the third condition because it will stop in the seconde one.**

## The try / except Structure

- You surround a dangerous section of code with `try` and `except`

- If the code in the `try` works - the `except` is skipped

- If the code in the `try` fails - it jumps to the `except` section

```
astr = "Bob"
try:
    print("Hello")
    istr = int(astr)
    print("There")
except:
    istr = -1

print("Done", istr)
```

**Check `notry.py`, `tryexcept.py` and `sample.py` to see in more details**

### Question

- Given the following code:

```
temp = "5 degrees"
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
```

Which line/lines should be surrounded by `try` block?

- [ ] **1**

- [ ] **3**

- [x] **3,4**

- [ ] **4**

- [ ] **None**

ANSWER: the code should be like this

```
temp = "5 degrees"
cel = 0

try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print("Please enter a number: ")
```
