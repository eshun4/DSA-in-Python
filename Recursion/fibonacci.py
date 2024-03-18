"""
This function calculates the fibonacci sequence of a given numerical value.

One is implemented with no memoization and the other is implemented with memoization 
which is a way of reusing an already calcukated value
stored in a variable. In other words an example of caching.

"""

def fibonacci_nomemo(num):
    """ It's not efficient because it uses too many computational resources.
    I'm talking about too many calculations.    
    """
    if num < 0:
        return None
    elif num <= 1:
        return num
    else:
        return fibonacci_nomemo(num - 1) + fibonacci_nomemo(num - 2)
    
def fibonacci_withmemo(num, memo={0:0, 1:1}):
    """
    This is an efficient version because of the use of memoization.
    """
    if num < 0:
        return None
    elif num <= 1:
        return num
    else:
        memo[num] = fibonacci_withmemo(num - 1, memo) + fibonacci_withmemo(num - 2, memo)
    return memo[num]

if __name__ == "__main__":
    # Test cases for fibonacci_nomemo
    print(fibonacci_nomemo(0))  # Expected output: 0
    print(fibonacci_nomemo(1))  # Expected output: 1
    print(fibonacci_nomemo(2))  # Expected output: 1
    print(fibonacci_nomemo(3))  # Expected output: 2
    print(fibonacci_nomemo(4))  # Expected output: 3
    print(fibonacci_nomemo(5))  # Expected output: 5
    print(fibonacci_nomemo(-1)) # Expected output: None

    # Test cases for fibonacci_withmemo
    print(fibonacci_withmemo(0))  # Expected output: 0
    print(fibonacci_withmemo(1))  # Expected output: 1
    print(fibonacci_withmemo(2))  # Expected output: 1
    print(fibonacci_withmemo(3))  # Expected output: 2
    print(fibonacci_withmemo(4))  # Expected output: 3
    print(fibonacci_withmemo(5))  # Expected output: 5
    print(fibonacci_withmemo(-1)) # Expected output: None


                
