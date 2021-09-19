def fibonacci(n):
    '''
    Returns the n term in the fibo sequence [1, 1, 2, 3, 5, 8...]
    '''  
    if n <= 1: # Base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # Recursive case


print(fibonacci(5))