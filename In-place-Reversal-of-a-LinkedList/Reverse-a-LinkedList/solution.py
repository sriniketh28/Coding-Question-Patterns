class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next

def reverse_linked_list(head):
    current, previous, next = head, None, None
    while(current):
        next = current.next
        current.next = previous
        previous = current
        current = next
    head = previous
    return head

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

print_linked_list(head)
print("\n")
print_linked_list(reverse_linked_list(head))
