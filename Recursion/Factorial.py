def factorial(num) :
    if num == 1:
        return 1
    return num * factorial(num-1)
    
# ----------------- PRINT OPERATIONS -----------------
a = 5
print('Factorial of', a , 'is :', factorial(a))