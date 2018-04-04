# Whiteboard problem
# Print all the nodes in a linked list, given the head

def print_ll(head):
    head = current
    while current.data:
        print current.data
        current = current.next
