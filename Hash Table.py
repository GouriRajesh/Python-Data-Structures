class HashTable:
    def __init__(self, size = 7):

        ''' We create a list whose length is a prime number so that it increases the 
        randomness of the hashed keys and decreases collision'''

        # Default value of size is set to 7 unless parameter value is passed
        self.data_map = [None] * size

    def hash(self, key):
        # Initialize to 0
        my_hash = 0

        # For every letter in key
        for letter in key :

            ''' my_hash + ordinal (letter) => ASCII value of letter * any prime number %length of data map
            Remainder would be a number from 0 to 6 which is the length of our data_map '''

            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def print_table(self):
        for index,value in enumerate(self.data_map) :
            print(index, ':', value)

    def set_item(self, key, value):
        hashed_address = self.hash(key)

        # When it is None, initialize with empty list
        if self.data_map[hashed_address] == None:
            self.data_map[hashed_address] = []

        # Append to empty list or existing list
        self.data_map[hashed_address].append([key,value])

    def get_item(self, key):
        # Get hashed address of key
        hashed_address = self.hash(key)

        # If address is empty, return None
        if self.data_map[hashed_address] == None:
            return None
        else:
            # Loop through the list at address
            for _ ,item in enumerate(self.data_map[hashed_address]):
                # Key is present in 0 index of sub-list
                list_key = item[0]
                if list_key == key:
                    # Value is present in 1 index of sub-list
                    list_val = item[1]
                    return list_val
                
    # Return a list of all the keys in the hash table
    def get_keys(self):
        keys_list = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for _ ,item in enumerate(self.data_map[i]):
                    # Key is present in 0 index of sub-list
                    list_key = item[0]
                    keys_list.append(list_key)
                        
        return keys_list


#------------------- PRINT OPERATIONS -------------------
# Create a new HT
ht = HashTable()
# Print the hash table
ht.print_table()
# Set the item
ht.set_item('bolts', 1400)
ht.set_item('washers', 50)
ht.set_item('lumber', 70)

ht.print_table()

# Get item using key
print('Item value : ', ht.get_item('bolts'))

# Get list of all keys in the HT
print('List of keys are :', ht.get_keys())