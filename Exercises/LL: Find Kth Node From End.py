class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


# WRITE FIND_KTH_FROM_END FUNCTION HERE #

def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for i in range(k):
        if fast is None:
            return None  # List is shorter than k
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)

"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""