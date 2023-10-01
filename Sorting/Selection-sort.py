def selection_sort(my_list) :
    # Loop through all elements of list
    for i in range(len(my_list)-1) :
        # Set min_value_index as the first element of each loop
        min_value_index = i
        # Compare elements from i+1 till end
        for j in range(i+1,len(my_list)) :
            # if current element < value of min_value_index element
            if my_list[j] < my_list[min_value_index] :
                # Update min_value_index to be index of current element
                min_value_index = j
        # Finally swap loop element with min_value_index element
        if i != min_value_index :
            temp = my_list[i]
            my_list[i] = my_list[min_value_index]
            my_list[min_value_index] = temp
    return my_list
            

# ----------------- PRINT OPERATIONS -----------------
a = [4,2,6,5,1,3,0,0]
print('List before selection sort: ', a)
print('List after selection sort: ', selection_sort(a))