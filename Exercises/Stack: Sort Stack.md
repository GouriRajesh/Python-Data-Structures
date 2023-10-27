The `sort_stack` function takes a single argument, a `Stack` object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 

The function should use the `pop`, `push`, `peek`, and `is_empty` methods of the `Stack` object.

Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.

This will use the Stack class we created using List.

The function should perform the following tasks:

1. Create a new instance of the `Stack` class called `sorted_stack`.

2. While the input stack is not empty, perform the following:

* Pop the top element from the input stack and store it in a variable `temp`.

* While the `sorted_stack` is not empty and its top element is greater than `temp`, pop the top element from `sorted_stack` and push it back onto the input stack.

* Push the `temp` variable onto the `sorted_stack`.

3. Once the input stack is empty, transfer the elements back from `sorted_stack` to the input stack. To do this, while `sorted_stack` is not empty, pop the top element from `sorted_stack` and push it onto the input stack.

Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original stack, due to the nested loops used to compare the elements.  However, the function should only use one additional stack, which could be useful in situations where memory is limited.