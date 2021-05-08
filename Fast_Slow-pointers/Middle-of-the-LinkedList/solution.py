class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle_of_linked_list(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(find_middle_of_linked_list(head).data)

head.next.next.next.next.next = Node(6)

print(find_middle_of_linked_list(head).data)

