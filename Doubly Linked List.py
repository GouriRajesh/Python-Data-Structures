#Creating class for a new node + constructor
class DoublyNode :
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

#Creating class for doubly linked list + constructor + methods
class DoublyLinkedList :
    def __init__(self,value) :
        new_node = DoublyNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) :
        temp = self.head
        print('The Doubly Linked List is : ')
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Add node to end of DLL
    def append(self,value) :
        #Create a new node
        new_node = DoublyNode(value)

        # Case 1: When DLL is empty i.e length=0
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # Case2: When nodes are present in DLL
        else:  
            #Next of last node points to new node and prev of new node points to previously last node
            self.tail.next = new_node
            new_node.prev = self.tail
            #Tail is new node
            self.tail = new_node
            #Increase length
            
        self.length += 1
        return new_node.value
    
    # Remove node from end of DLL
    def pop(self) : 
        # Case 1: When DLL is empty i.e length=0
        if self.head is None:
            return None
        
        # Case2: When 1 node is present in DLL
        elif self.length == 1:
            popped_element = self.head.value
            self.head = None
            self.tail = None
            
        # Case3: When nodes are present in DLL
        else:
            # Get the last element which is popped
            popped_element = self.tail.value
            # Get last second node
            temp = self.tail.prev
            self.tail.next = None
            self.tail.prev = None
            temp.next = None
            self.tail = temp
            
        self.length -= 1
        return popped_element
    
    # Add node to start of DLL
    def prepend(self,value) :
        new_node = DoublyNode(value)

        # Case 1: When DLL is empty i.e length=0
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # Case2: When nodes are present in DLL
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.length += 1
        return new_node.value
    
    # Remove node from start of DLL
    def pop_first(self) :
        # Case 1: When DLL is empty i.e length=0
        if self.head is None:
            return None
        
        # Case2: When 1 node is present in DLL
        elif self.length == 1:
            popped_element = self.head.value
            self.head = None
            self.tail = None
            
        # Case3: When nodes are present in DLL
        else:
            # Get the first element which is popped
            popped_element = self.head.value
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
           
        self.length -= 1
        return popped_element
    
    # Return node at index of DLL
    def get(self,index) :
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            # Optimized version for DLL
            # Index is present in 1st half of DLL
            if index < self.length/2:
                # Here the variable is _ and not i because we are not using the variable inside the loop
                for _ in range(index):
                    temp = temp.next
            # Index is present in 2nd half of DLL
            else:
                temp = self.tail
                for _ in range(self.length-1-index):
                    temp = temp.prev
        return temp
                
    # Set the value of node at particular index in DLL  
    def set_value(self, index, value) :
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp.value
        return None
        
    # Insert new node at given index in DLL
    def insert(self, index, value) :
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = DoublyNode(value)
            temp_before = self.get(index-1)
            temp_after = temp_before.next

            new_node.prev = temp_before
            new_node.next = temp_after
            temp_before.next = new_node
            temp_after.prev = new_node

        self.length += 1
        return new_node.value
        
    # Remove a node from particular index in DLL
    def remove(self, index) :
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp.value
    
    # Reverse a DLL
    def reverse(self) :
        temp = None
        current = self.head

        # Swap next and prev for all nodes 
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev



#---------------------------- PRINT OPERATIONS----------------------------
# Create a new DLL
dll = DoublyLinkedList(1)
# Print DLL
dll.print_list()
# Print length of DLL
print('Length: ', dll.length)

# Append new node to end of DLL
dll.append(2)
dll.print_list()
print('Length: ', dll.length)

# Pop node from end of DLL
print('Popped element is: ',dll.pop())
dll.print_list()
print('Length: ', dll.length)

# Add new node to start of DLL
print('Prepend: ', dll.prepend(0))
dll.print_list()
print('Length: ', dll.length)

# Remove node from start of DLL
print('Popped first is: ',dll.pop_first())
dll.print_list()
print('Length: ', dll.length)

dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
dll.append(7)
dll.append(8)
dll.append(9)
dll.append(10)

dll.print_list()
print('Length: ', dll.length)

# Get element at index 8
print('Element at index: ',dll.get(8).value)

# Set new value of node at index 1
print('Set new element at index: ',dll.set_value(1,25))
dll.print_list()
print('Length: ', dll.length)

# Insert new node at index 2
print('New node at index: ',dll.insert(2,26))
dll.print_list()
print('Length: ',dll.length)

# Remove node at index 1
print('Removed: ', dll.remove(1))
dll.print_list()
print('Length: ',dll.length)

# Reverse the DLL
dll.reverse()
dll.print_list()
print('Length: ',dll.length)
