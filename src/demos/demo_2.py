"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(node):
    """
    we want the input node (the "head") to become the new tail 
    we want the old tail to become the new head 
    three pointers, prev_node, current_node, forward_node 
    """
    current_node = node 
    prev_node = None 
    forward_node = None 

    while current_node:
        # set `forward_node` to current node's `next`
        forward_node = current_node.next 

        # switch the direction of `current`'s arrow 
        current_node.next = prev_node 

        # update our pointers
        prev_node = current_node
        current_node = forward_node

    # we need to return the new head, which the `prev` pointer is referring to 
    return prev_node

def print_ll(node):
    # set your `current_node` variable to the starting node 
    current_node = node 

    # keep moving `current_node` in a loop 
    # while current_node is not none
    while current_node is not None: 
        # print the 'current_node' value
        print(current_node.value)
        # traverse the the next node
        current_node = current_node.next 

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')
f = LinkedListNode('F')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print_ll(a)
print("---")
new_head = reverse(a)

print_ll(new_head)
