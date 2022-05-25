import random

x = random.randint(1, 10)
y = random.randint(1, 10)

if x > y:
  print(x, 'is greater than', y)
elif x == y:
  print(x, 'is equal to', y)
else:
    print(x, 'is less than', y)
