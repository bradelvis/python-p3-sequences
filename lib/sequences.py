#!/usr/bin/env python3

def print_fibonacci(length):
    '''Prints the Fibonacci sequence up to the length provided.'''
    if length <= 0:
        print("[]")  # Print an empty list for invalid length
        return
    
    # Start with the first two numbers in the Fibonacci sequence
    fib_sequence = [0, 1]

    # If length is 1, we only want the first number
    if length == 1:
        print("[0]")  # Print the list with only the first Fibonacci number
        return
    
    # Generate the Fibonacci sequence up to the desired length
    for i in range(2, length):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    # Print the sequence
    print(fib_sequence[:length])
