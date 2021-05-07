from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_level_averages(root):
        result = []
        if root is None:
            return result
        
        queue = deque()
        queue.append(root)
        while queue:
            currentLevelSum = 0
            currentLevelSize = len(queue)
            for _ in range(currentLevelSize):
                currentNode = queue.popleft()
                currentLevelSum += currentNode.data
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(currentLevelSum/currentLevelSize)
        return result
        
    

root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.left.right = Node(2)
root.right.left = Node(10)
root.right.right = Node(5)

print(find_level_averages(root))

