"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.
Example:
The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.
```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
x.next = y
y.next = z
delete_node(y)
```
*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(delete_this_node):
    # Your code here
    # set my next to the node that i want to delete(s) next
    next = delete_this_node.next
    # does this node exist?
    if next:
        # set this nodes value to the value of the next node
        delete_this_node.value = next.value
        # set this nodes next to its next(s) next
        delete_this_node.next = next.next
    else:
        raise Exception("This technique deose not work for the last node in the list")



x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)