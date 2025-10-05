
import pandas as pd
import numpy as np

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)


def fibonacci(n, i=2, fib_sequence=None):
    """Returns a list of Fibonacci numbers up to n recursively"""
    # Determines conditions for returning the fibonacci sequence
    if n < 2:
        return 1
    if i == n:
        return fib_sequence[n-1]
    
    # Sets up the fibonacci sequence
    if fib_sequence is None:
        fib_sequence = [1, 1]

    # Adds last two values in fib_sequence to get the next value
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fibonacci(n, i + 1, fib_sequence)

def to_binary(n, binary_sequence=None):
    """Returns the binary representation of n recursively"""

    # Sets up binary sequence
    if binary_sequence is None:
        binary_sequence = []

    # Determines condition for returning binary representation
    if n < 2:
        binary_sequence.append(n)
        return "".join(str(digit) for digit in binary_sequence[::-1])
    
    # Appends each remainder to binary_sequence and iterates
    else:
        binary_sequence.append(n % 2)
        return to_binary(n // 2, binary_sequence)

def task_1():
    # Replace ? in gender values with NaN
    df_bellevue.replace({'gender': {'?': np.nan}}, inplace=True)

    # Return the number of missing values per column in ascending order
    return list((df_bellevue.shape[0] - df_bellevue.count()).sort_values().index)

def task_2():
    # Create a year column from the date_in column
    df_bellevue['year'] = df_bellevue['date_in'].str[:4].astype(int)

    # Return a DataFrame with the total number of admissions per year
    return df_bellevue.groupby('year')['year'].count().rename("total_admissions").reset_index()

def task_3():
    # Calculate the average age within each gender group
    return df_bellevue.groupby('gender')['age'].mean().round(1)

def task_4():
    # Return the top 5 most common professions
    return list(df_bellevue['profession'].value_counts().sort_values(ascending=False).head(5).index)