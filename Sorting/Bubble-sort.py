def bubble_sort(my_list) :
    # How many times to loop? : All the elements i.e length of list -1 index 
    # Start at max index, go upto 0, decrement by 1 each loop
    for i in range(len(my_list)-1, 0, -1) :
        # How many comparisions? : No. of uncompared elements after each outer loop
        for j in range(i) :
            # If first element > second element
            if my_list[j] > my_list[j+1] :
                # Swap elements
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


# ----------------- PRINT OPERATIONS -----------------
a = [4,2,6,5,1,3]
print('List before bubble sort: ', a)
print('List after bubble sort: ', bubble_sort(a))