class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(has_cycle(head))

head.next.next.next.next.next = head.next.next

print(has_cycle(head))

