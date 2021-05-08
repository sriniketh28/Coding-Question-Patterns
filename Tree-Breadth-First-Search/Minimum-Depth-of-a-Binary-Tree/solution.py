from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_minimum_depth(root):
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    minimum_depth = 0
    while queue:
        minimum_depth += 1
        for _ in range(len(queue)):
            currentNode = queue.popleft()
            if currentNode.left is None and currentNode.right is None:
                return minimum_depth
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        

root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.right.left = Node(10)
root.right.right = Node(5)

print(find_minimum_depth(root))

root.left.left = Node(9)
root.right.left.left = Node(11)

print(find_minimum_depth(root))

