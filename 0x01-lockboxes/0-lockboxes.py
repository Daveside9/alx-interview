#!/usr/bin/python3
def canUnlockAll(boxes):
    # We use a set to keep track of the box numbers that we can open
    # We start with box 0, since it is already unlocked
    unlocked_boxes = {0}

    # We use a queue to keep track of the keys that we find
    keys_queue = boxes[0]

    # We process the keys until there are no more
    while keys_queue:
        key = keys_queue.pop(0)
        # If the key opens a box that we haven't opened before, we add it to the set of unlocked boxes
        if key not in unlocked_boxes and key < len(boxes):
            unlocked_boxes.add(key)
            keys_queue.extend(boxes[key])
    
    # If we managed to unlock all boxes, then the set of unlocked boxes should contain all box numbers
    return len(unlocked_boxes) == len(boxes)
