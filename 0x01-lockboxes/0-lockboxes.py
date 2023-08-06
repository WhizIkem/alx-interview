#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    num_boxes = len(boxes)
    visited = [False] * num_boxes #Initialize all boxes as unvisited
    visited[0] = True # Mark first box as visited

    stack = [0] # Initialize stack with first box

    while stack:
        current_box = stack.pop() # Take the top box from the stack

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                # If the key is valid and the box has not been visited, mark it as visited and add it to the stack
                visited[key] = True
                stack.append(key)

    return all(visited) # Return True if all boxes have been visited, False otherwise
