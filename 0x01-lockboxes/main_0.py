#!/usr/bin/python3

# Import the canUnlockAll function from the module 0-lockboxes
canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Test case 1
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

# Test case 2
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

# Test case 3
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
