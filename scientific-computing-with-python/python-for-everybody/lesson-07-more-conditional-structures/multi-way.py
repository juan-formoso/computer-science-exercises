import random

x = random.randint(1, 20)

if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print('large')

print('done')
