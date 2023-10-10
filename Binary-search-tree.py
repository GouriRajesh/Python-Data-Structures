# Creating class for a new node + constructor
class Node:
    def __init__(self,value) :
        self.value = value
        self.left = None
        self.right = None

# Creating class for binary search tree + constructor + methods
class BinarySearchTree :
    def __init__(self) :
        # Create an empty bst initially 
        self.root = None

    # Insert into BST
    def insert(self,value) :
        # Step 1: Create a new node
        new_node = Node(value)
        # Step 2: If BST is empty
        if self.root == None:
            self.root = new_node
            return True
        # Nodes present in BST
        else:
            # Step 3: Compare new value with parent and move accordingly
            temp = self.root
            # We don't know how many times it runs the loop-recursion
            while (True) :
                # Step 4: Prevent duplicates from entering BST
                if new_node.value == temp.value:
                    return False
                # Step 5: If less move left if more move right. If empty insert else continue loop.
                elif new_node.value < temp.value:
                    if temp.left == None:
                        temp.left = new_node
                        return True
                    else:
                        temp = temp.left
                elif new_node.value > temp.value:
                    if temp.right == None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right

    # Search for value in BST
    def contains(self,value) :
        # When BST is empty (we skip these lines of code. It is handled by while loop)
        # if self.root == None:
        #     return False
            
        # Compare value with parent and move accordingly
        temp = self.root
        # Until temp is not none i.e item is present in BST
        while temp is not None :
            if value == temp.value:
                return True
            # If less move left if more move right
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False


#------------------- PRINT OPERATIONS -------------------
# Create a new BST
bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)

print(bst.contains(3))
print(bst.contains(5))