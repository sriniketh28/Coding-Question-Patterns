from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_level_order_successor(root, data):
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        if currentNode.data == data:
            break
    return queue[0] if queue else None
        

root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.right.left = Node(10)
root.left.left = Node(9)
root.right.right = Node(5)
root.right.left.left = Node(12)

result = find_level_order_successor(root, 12)
if result:
    print(result.data)

result = find_level_order_successor(root, 9)
if result:
    print(result.data)

