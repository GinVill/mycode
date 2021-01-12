#!/usr/bin/python3

# create a custom function for sorting
# the fuction take_second will always return
# what is in the second position
# take the second element for sort
def take_second(secondplacewins):
    # the value of secondplacewins[1] - 'antelope', ' ', 'banana'
    return secondplacewins[1]

# random list of tuples
puzzle = [(3, "antelope"), ("Alta", " "), ("Research", "banana", 3.14159265359, "pi")]

# sort list with our custom key take_second
sorted_list = sorted(puzzle, key = take_second)

# print list
print('Sorted list:', sorted_list)

