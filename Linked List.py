#Creating class for a new node + constructor
class Node:
    def __init__(self,value) :
        self.value = value
        self.next = None

#Creating class for linked list + constructor + methods
class LinkedList:
    def __init__(self,value) :
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) :
        temp = self.head
        print('The Linked List is : ')
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Add node to end of LL
    def append(self,value) :
        #Create a new node
        new_node = Node(value)

        # Case 1: When LL is empty i.e length=0
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # Case2: When nodes are present in LL
        else:  
            #Next of last node points to new node (Prev was None)
            self.tail.next = new_node
            #Tail is new node
            self.tail = new_node
            #Increase length
            
        self.length += 1
        return new_node.value

    # Remove node from end of LL
    def pop(self) : 
        # Case 1: When LL is empty i.e length=0
        if self.head is None:
            return None
        
        # Case2: When 1 node is present in LL
        elif self.length == 1:
            popped_element = self.head.value
            self.head = None
            self.tail = None
            
        # Case3: When nodes are present in LL
        else:
            temp = self.head
            # Get last second node
            while temp.next is not self.tail :
                temp = temp.next
            # Get the last element which is popped
            popped_element = temp.next.value
            self.tail = temp
            self.tail.next = None
            
        self.length -= 1
        return popped_element
    
    # Add node to start of LL
    def prepend(self,value) :
        new_node = Node(value)

        # Case 1: When LL is empty i.e length=0
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # Case2: When nodes are present in LL
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        return new_node.value

    # Remove node from start of LL
    def pop_first(self) :
        # Case 1: When LL is empty i.e length=0
        if self.head is None:
            return None
        
        # Case2: When 1 node is present in LL
        elif self.length == 1:
            popped_element = self.head.value
            self.head = None
            self.tail = None
            
        # Case3: When nodes are present in LL
        else:
            # Get the first element which is popped
            popped_element = self.head.value
            temp = self.head
            self.head = self.head.next
            temp.next = None
           
        self.length -= 1
        return popped_element
    
    # Return node at index of LL
    def get(self,index) :
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            # Here the variable is _ and not i because we are not using the variable inside the loop
            for _ in range(index):
                temp = temp.next
            return temp

    # Set the value of node at particular index in LL  
    def set_value(self, index, value) :
        temp = self.get(index)
        temp.value = value
        
        return temp.value
    
    # Insert new node at given index in LL
    def insert(self, index, value) :
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        return new_node.value
    
    # Remove a node from particular index in LL
    def remove(self, index) :
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            prev = self.get(index-1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
        self.length -= 1
        return temp.value
    
    # Reverse a linked list
    def reverse(self) :
        # Step 1 : Reverse head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # Step 2 : create two pointers after and before temp which move togther
        after = temp.next
        before = None # Initially
        # Step 3 : Flip all the connections
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


#------------------- PRINT OPERATIONS -------------------
# Create a new LL
ll = LinkedList(5)
# Append to end of LL
ll.append(10)
# Print LL
ll.print_list()
# Print length of LL
print('Length: ',ll.length)
# Pop from end of LL
print('Popped: ',ll.pop())
ll.print_list()
print('Length: ',ll.length)
# Add to start of LL
ll.prepend(2)
ll.print_list()
print('Length: ',ll.length)
# Remove from start of LL
print('Popped First: ',ll.pop_first())
ll.print_list()
print('Length: ',ll.length)
# Append to end of LL
ll.append(20)
ll.print_list()
print('Length: ',ll.length)
# Get element at index 1
print('Element at index: ',ll.get(1).value)
# Set new value of node at index 1
print('Set new element at index: ',ll.set_value(1,25))
ll.print_list()
# Insert new node at index 1
print('New node at index: ',ll.insert(1,23))
ll.print_list()
print('Length: ',ll.length)
# Remove node at index 1
print('Removed: ', ll.remove(1))
ll.print_list()
print('Length: ',ll.length)
# Reverse the LL
ll.reverse()
ll.print_list()
print('Length: ',ll.length)