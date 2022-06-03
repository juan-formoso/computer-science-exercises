# Finding the largest value

largest_so_far = -1

print('Before', largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(the_num, largest_so_far)

print('After', largest_so_far)

"""
$ python3 largest.py
Before -1
9 9
41 41
41 12
41 3
74 74
74 15
After 74
"""

# We make a variable that contains the largest value we have seen so far. If the current number we are looking at is larger, it is the new largest value we have seen so far.