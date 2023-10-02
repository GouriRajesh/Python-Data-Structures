# merge is a helper function that takes 2 sorted lists and merges them in a sorted order
def merge(list1, list2) :
    merged_list = []
    i = 0
    j = 0

    # While both lists have elements present in them
    while i < len(list1) and j < len(list2) :
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append all remaining elements (if present) from list 1 to final list
    while i < len(list1) :
        merged_list.append(list1[i])
        i += 1

    # Append all remaining elements (if present) from list 2 to final list
    while j < len(list2) :
        merged_list.append(list2[j])
        j += 1
            
    return merged_list

# ------------------

def merge_sort(my_list) :

    # If list contains only 1 element
    if len(my_list) == 1:
        return my_list
    # Finding the middle index. Handles both odd and even elements using int()
    mid_index = int(len(my_list)/2)
    # Range from start to mid called recursively until 1 element is returned
    right = merge_sort(my_list[:mid_index])
    # Range from mid to end called recursively until 1 element is returned
    left = merge_sort(my_list[mid_index:])

    # Return merged list at each recursion
    return merge(left,right)


# ----------------- PRINT OPERATIONS -----------------
one = [1,2,7,8]
two = [3,4,5,6]
print('Lists before merge are: ')
print(one)
print(two)
print('List after merge is: ')
print(merge(one,two))

a = [4,2,6,5,1,3,5,3]
print('List before merge sort: ', a)
print('List after merge sort: ', merge_sort(a))

