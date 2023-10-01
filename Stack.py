# Stacks can be implemented using a list by inserting and deleting from the end only
# But, we will be making use of a Linked List to implement stack
# The direction of the linked list is facing downwards

# Creating class for a new node + constructor
class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None

# Creating class for stack + constructor + methods
class Stack:
    def __init__(self, value) :
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        print('The stack is: ')
        temp = self.top
        while temp is not None :
            print(temp.value)
            temp = temp.next
    
    # Insert node/element to stack
    def push(self,value) :
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


    # Delete node/element from stack
    def pop(self) :
        if self.height == 0:
            return None
        else:
            popped_element = self.top.value
            temp =  self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1

        return popped_element
    

#------------------- PRINT OPERATIONS -------------------
#Create a new stack
st = Stack(2)
#Print elements in the stack
st.print_stack()
#Print height of the stack
print('Height: ', st.height)

# Insert element into stack
st.push(4)
st.print_stack()
print('Height: ', st.height)

# Remove element from stack
print('Popped element: ', st.pop())
st.print_stack()
print('Height: ', st.height)