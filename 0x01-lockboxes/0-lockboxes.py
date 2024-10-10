#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    discovered_boxes = set([0])
    hidden_box = set(boxes[0]).difference(set([0]))
    while len(hidden_box) > 0:
        boxIdx = hidden_box.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in discovered_boxes:
            hidden_box = hidden_box.union(boxes[boxIdx])
            discovered_boxes.add(boxIdx)
    return n == len(discovered_boxes)
