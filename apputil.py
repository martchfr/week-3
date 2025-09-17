import seaborn as sns
import pandas as pd


def fibonacci(n):
    # Function internal variables
    seq = [0, 1] 
    iterator = 2
    a = 0
    b = 1

    def recursive(iterator, a, b):
        # Exit function
        if iterator == n + 1:
            return
        
        # Get next value in list and append
        x = seq[a] + seq[b]
        seq.append(x)

        # Increment on variables for next call
        iterator+=1
        a+=1
        b+=1

        recursive(iterator, a, b)

    recursive(iterator, a, b)
    return seq
