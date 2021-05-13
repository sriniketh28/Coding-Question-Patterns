class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def has_path(root, sum):
    if root is None:
        return False
    if root.data == sum and root.left is None and root.right is None:
        return True
    return has_path(root.left, sum - root.data) or has_path(root.right, sum - root.data)
    
root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)

print(has_path(root, 23))
print(has_path(root, 16))
