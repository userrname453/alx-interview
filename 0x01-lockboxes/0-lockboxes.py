def canUnlockAll(boxes):
    n = len(boxes)
    unlocked_boxes = set([0])  # Start with the first box unlocked
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_box = keys.pop()  # Get the next box to process
        for key in boxes[current_box]:
            if key not in unlocked_boxes and key < n:
                unlocked_boxes.add(key)
                keys.append(key)  # Add this new key to the stack

    # Check if we have unlocked all boxes
    return len(unlocked_boxes) == n
