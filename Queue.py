# Queue can be implemented using a list by inserting on one end and deleting from the other end
# But, we will be making use of a Linked List to implement queue
# The direction of the linked list is facing right

# Creating class for a new node + constructor
class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None

# Creating class for stack + constructor + methods
class Queue:
    def __init__(self, value) :
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        print('The queue is: ')
        temp = self.first
        while temp is not None :
            print(temp.value)
            temp = temp.next

    # Insert node/element to queue
    def enqueue(self,value) :
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    # Delete node/element from queue
    def dequeue(self) :
        if self.length == 0:
            return None
        elif self.length == 1:
            removed_element = self.first.value
            self.first = None
            self.last = None
        else:
            removed_element = self.first.value
            temp =  self.first
            self.first = self.first.next
            temp.next = None
            
        self.length -= 1
        return removed_element
    

#------------------- PRINT OPERATIONS -------------------
#Create a new queue
qu = Queue(1)
#Print elements in the queue
qu.print_queue()
#Print length of the queue
print('Length: ', qu.length)

# Insert element into queue
qu.enqueue(2)
qu.print_queue()
print('Length: ', qu.length)

qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)

qu.print_queue()
print('Length: ', qu.length)

# Remove element from queue
print('Removed element: ', qu.dequeue())
qu.print_queue()
print('Length: ', qu.length)

qu.dequeue()
qu.dequeue()

qu.print_queue()
print('Length: ', qu.length)