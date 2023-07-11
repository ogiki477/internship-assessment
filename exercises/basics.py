from typing import List

def collatz(n: int) -> List[int]:
    sequence = [n]  # Start with n as the first value in the sequence
    while n != 1:  # Continue until n becomes 1
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:  # If n is odd
            n = 3 * n + 1
        sequence.append(n)  # Add the new value of n to the sequence
    return sequence


    """
    You're given a positive integer n. Write an algorithm that does the following:
        - If n is even, the algorithm divides n by 2. This is the new value of n
        - If n is odd, the algorithm multiplies it by 3 and adds 1. This is the new value of n.
        - The algorithm repeats this until n == 1.

    Implement this algorithm in this function and return a list of all the intermediate values of n.
    For example, if n = 3, the sequence of values is: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    So, your function would return: [3, 10, 5, 16, 8, 4, 2, 1]
    """



def distinct_numbers(numbers: List[int]) -> int:
    distinct = set(numbers)
    return len(distinct)
    

    
    """
    You are given a list of integers (the list could be empty), calculate the number of distinct/unique values in the list.

    E.g if numbers = [2, 3, 2, 2, 3], then the answer is 2 since there are only 2 unique numbers: 2 and 3.
    """
    pass 
