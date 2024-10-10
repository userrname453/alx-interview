#!/usr/bin/python3
'''A module for determining if all boxes can be unlocked.'''

def canUnlockAll(boxes):
    '''Determines if all the boxes can be unlocked. Each box contains keys 
    (indices) that unlock other boxes. The first box is initially unlocked.
    
    Args:
        boxes (list of lists): A list where each element is a list of keys (box indices).
        
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''
    total_boxes = len(boxes)  # Total number of boxes
    unlocked_boxes = set([0])  # Set of boxes that have been unlocked, starting with the first
    keys_to_check = set(boxes[0]).difference(set([0]))  # Keys found in the first box, excluding the first box itself

    while len(keys_to_check) > 0:  # Loop while there are still keys to check
        current_key = keys_to_check.pop()  # Get a key from the keys_to_check set
        if current_key < 0 or current_key >= total_boxes:  # Ignore invalid box indices
            continue
        if current_key not in unlocked_boxes:  # If this box has not been unlocked yet
            keys_to_check = keys_to_check.union(boxes[current_key])  # Add new keys from this box
            unlocked_boxes.add(current_key)  # Mark this box as unlocked
    
    return total_boxes == len(unlocked_boxes)  # All boxes are unlocked if the number of unlocked boxes matches the total
