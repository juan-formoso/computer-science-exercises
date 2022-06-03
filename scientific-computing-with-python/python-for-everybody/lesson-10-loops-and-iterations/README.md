# Loops and Iterations

## Repeated Steps

- Loops (repeated steps) have **iteration variables** that change each time through a loop. Often these **iteration variables** go through a sequence of numbers.

```
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)
```

## An Infinite Loop

- What is wrong with this loop?

```
n = 5
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!')
```

**This loop is going to run forever since `n` will be always equal to `5`.**]

## Breaking Out of a Loop

- The **break** statement ends the current loop and jumps to the statement immediately following the loop.

- It is like a loop test that can happen anywhere in the body of the loop.

```
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

---------------------------
Output:

> hello there
hello there
> finished
finished
> done
Done!
```

## Finishing an Iteration with continue

- The **continue** statement ends the current iteration and jumps to the top of the loop and starts the next iteration

```
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

---------------------------
Output:

> hello there
hello there
> # don't print this
> print this!
print this!
> done
Done!
```

## Indefinite Loops

- While loops are called **"indefinite loops"** because they keep going until a logical condition becomes **False**.

- The loops we have seen so far are pretty easy to examine to see if they will terminate or if they will be "infinite loops".

- Sometimes it is a little harder to be sure if a loop will terminate.

### Question

**What will the following code print out?:**

```

n = 0
while True:
if n == 3:
break
print(n)
n = n + 1

```

- [x] <br>

  0
  1
  2

- [ ] <br>

  0
  1
  2
  3

- [ ] <br>

  1
  2

- [ ] <br>

  1
  2
  3

```

```
