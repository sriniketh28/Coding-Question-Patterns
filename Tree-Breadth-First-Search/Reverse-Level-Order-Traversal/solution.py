from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reverse_level_order_traversal(root):
    result = deque()
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        currentLevel = []
        for _ in range(len(queue)):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.data)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.appendleft(currentLevel)
    return list(result)
        
        
    

root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)

print(reverse_level_order_traversal(root))

